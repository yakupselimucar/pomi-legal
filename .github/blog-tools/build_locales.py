#!/usr/bin/env python3
"""Ana sayfanın statik İngilizce ve Portekizce kopyalarını üretir: en/index.html, pt/index.html.

Neden ayrı sayfa: index.html dili tarayıcıda JS ile değiştirir; arama motorları
ve yapay zeka tarayıcıları çoğunlukla yalnız ilk HTML'i okur. "pomodoro timer",
"pomodoro app" gibi İngilizce ve Brezilya'dan gelen Portekizce aramalar ancak
kendi dilinde, kendi adresinde bir sayfa varsa eşleşir. Çeviriler en/ ve pt/
altında HTML'e işlenir (hreflang ile ana sayfaya bağlı). Sayfa yine aynı betiği
çalıştırır, yani dil düğmeleri ve fetih haritası çalışmaya devam eder.

Kaynak tek: index.html içindeki `en: { ... }` ve `pt: { ... }` sözlükleri. Metin değişince:

    python3 .github/blog-tools/build_locales.py

Elle düzenlenen en/index.html ve pt/index.html bir sonraki çalıştırmada ezilir.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SITE = "https://pomifocus.com/"
ENTRY = re.compile(r"""(?:'([\w-]+)'|([A-Za-z_]\w*))\s*:\s*'((?:[^'\\]|\\.)*)'""")

# dil → (html lang, og:locale, dizin)
LOCALES = {
    "en": ("en", "en_US", "en"),
    "pt": ("pt-BR", "pt_BR", "pt"),
}
TR_TITLE_JS = "Pomi: Pomodoro Sayacı & Birlikte Ders Çalış | PomiFocus"


def read_dict(html, lang):
    """index.html'deki `<lang>: {` çeviri bloğunu (plants hariç) {anahtar: metin} olarak döndürür."""
    start = html.index(f"      {lang}: {{\n        title:")   # STORE.pt ile karışmasın
    end = html.index("plants: {", start)
    out = {}
    for m in ENTRY.finditer(html[start:end]):
        key = m.group(1) or m.group(2)
        out[key] = m.group(3).replace("\\'", "'")
    if "title" not in out or "heroTitle" not in out:
        sys.exit(f"{lang} sözlüğü okunamadı")
    return out


def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def alternates():
    return (f'  <link rel="alternate" hreflang="tr" href="{SITE}" />\n'
            f'  <link rel="alternate" hreflang="en" href="{SITE}en/" />\n'
            f'  <link rel="alternate" hreflang="pt-BR" href="{SITE}pt/" />\n'
            f'  <link rel="alternate" hreflang="x-default" href="{SITE}" />')


def build(lang):
    html_lang, og_locale, folder = LOCALES[lang]
    url = SITE + folder + "/"
    html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    d = read_dict(html, lang)

    # 1) data-i18n içerikleri
    missing = []

    def fill(m):
        open_tag, tag, key, close = m.group(1), m.group(2), m.group(3), m.group(5)
        if key not in d:
            missing.append(key)
            return m.group(0)
        value = esc_attr(d[key]) if tag == "title" else d[key]
        return open_tag + value + close

    html = re.sub(r'(<(\w+)\b[^>]*\bdata-i18n="([\w-]+)"[^>]*>)(.*?)(</\2>)', fill, html, flags=re.S)
    if missing:
        sys.exit(f"{lang}'de eksik anahtar: " + ", ".join(sorted(set(missing))))

    # 1b) dile göre değişen bağlantılar (web sayacı, online kütüphane…)
    def fill_href(m):
        tag = m.group(0)
        key = re.search(r'data-i18n-href="([\w-]+)"', tag).group(1)
        if key not in d:
            sys.exit(f"{lang}'de eksik href anahtarı: {key}")
        return re.sub(r'href="[^"]*"', f'href="{d[key]}"', tag, count=1)

    html = re.sub(r'<a\b[^>]*\bdata-i18n-href="[\w-]+"[^>]*>', fill_href, html)

    def sub1(old, new, count=1):
        nonlocal html
        if html.count(old) < 1:
            sys.exit("bulunamadı: " + old[:70])
        html = html.replace(old, new, count)

    # 2) dil, başlık, açıklama, canonical, Open Graph
    sub1('<html lang="tr">', f'<html lang="{html_lang}">')
    sub1('<meta name="description" data-i18n-attr="description" content="',
         '<meta name="description" content="')
    html = re.sub(r'(<meta name="description" content=")[^"]*(")',
                  lambda m: m.group(1) + esc_attr(d["description"]) + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                  lambda m: m.group(1) + esc_attr(d["title"]) + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:description" content=")[^"]*(")',
                  lambda m: m.group(1) + esc_attr(d["description"]) + m.group(2), html, count=1)
    sub1('<meta property="og:url" content="https://pomifocus.com/" />',
         f'<meta property="og:url" content="{url}" />')
    others = [l for l in ("tr_TR", "en_US", "pt_BR") if l != og_locale]
    sub1('<meta property="og:locale" content="tr_TR" />\n  <meta property="og:locale:alternate" content="en_US" />\n  <meta property="og:locale:alternate" content="pt_BR" />',
         f'<meta property="og:locale" content="{og_locale}" />\n'
         f'  <meta property="og:locale:alternate" content="{others[0]}" />\n'
         f'  <meta property="og:locale:alternate" content="{others[1]}" />')
    html = re.sub(r'  <link rel="alternate" hreflang="[^\n]*\n', '', html)   # ana sayfanın alternates'ı
    sub1('<link rel="canonical" href="https://pomifocus.com/" />',
         f'<link rel="canonical" href="{url}" />\n' + alternates())

    # 3) JSON-LD: sayfa adı/açıklaması/dili
    sub1(f'"name": "{TR_TITLE_JS}",', f'"name": "{d["title"]}",')
    html = re.sub(r'("@id": "https://pomifocus.com/#webpage",\s*"url": ")[^"]*(")',
                  lambda m: m.group(1) + url + m.group(2), html, count=1)
    html = re.sub(r'("@id": "https://pomifocus.com/#webpage".*?"description": ")[^"]*(")',
                  lambda m: m.group(1) + d["description"].replace('"', '\\"') + m.group(2), html, count=1, flags=re.S)
    html = re.sub(r'("@id": "https://pomifocus.com/#webpage".*?"inLanguage": ")tr(")',
                  lambda m: m.group(1) + html_lang + m.group(2), html, count=1, flags=re.S)

    # 4) Dil düğmeleri: bu dil etkin
    sub1('<button class="lang-btn active" data-lang="tr"', '<button class="lang-btn" data-lang="tr"')
    sub1(f'<button class="lang-btn" data-lang="{lang}"', f'<button class="lang-btn active" data-lang="{lang}"')

    # 5) Bu sayfa kendi dilinde açılır (kayıtlı tercih/tarayıcı dili sayfa dilini ezmesin)
    sub1("<script>document.documentElement.classList.add('js');</script>",
         f"<script>document.documentElement.classList.add('js'); window.POMI_PAGE_LANG = '{lang}';</script>")

    # 6) Göreli bağlantılar bir üst dizine; blog yazıları EN
    html = html.replace('href="blog/"', 'href="../blog/en.html"')
    html = re.sub(r'href="(?!https?:|mailto:|#|\.\./|/|data:|javascript:)([\w.-]+\.html)"',
                  r'href="../\1"', html)
    html = html.replace('href="./#', 'href="../#')

    out_dir = os.path.join(ROOT, folder)
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{folder}/index.html yazıldı ({len(d)} anahtar)")


if __name__ == "__main__":
    for code in LOCALES:
        build(code)
