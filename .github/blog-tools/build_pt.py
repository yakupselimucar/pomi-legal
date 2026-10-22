#!/usr/bin/env python3
"""Ana sayfanın statik Portekizce (pt-BR) kopyasını üretir: pt/index.html.

Neden ayrı sayfa: index.html dili tarayıcıda JS ile değiştirir; arama motorları
ve yapay zeka tarayıcıları çoğunlukla yalnız ilk HTML'i okur. Brezilya'dan gelen
aramaların Portekizce içerik görebilmesi için çeviriler pt/ altında HTML'e
işlenir (hreflang ile ana sayfaya bağlı). Sayfa yine aynı betiği çalıştırır, yani
dil düğmeleri ve fetih haritası çalışmaya devam eder.

Kaynak tek: index.html içindeki `pt: { ... }` sözlüğü. Metin değişince:

    python3 .github/blog-tools/build_pt.py

Elle düzenlenen pt/index.html bir sonraki çalıştırmada ezilir.
"""
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
SITE = "https://pomifocus.com/"
PT_URL = SITE + "pt/"
ENTRY = re.compile(r"""(?:'([\w-]+)'|([A-Za-z_]\w*))\s*:\s*'((?:[^'\\]|\\.)*)'""")


def read_pt_dict(html):
    """index.html'deki `pt: {` bloğunu (plants hariç) {anahtar: metin} olarak döndürür."""
    start = html.index("      pt: {\n        title:")   # STORE.pt ile karışmasın
    end = html.index("plants: {", start)
    out = {}
    for m in ENTRY.finditer(html[start:end]):
        key = m.group(1) or m.group(2)
        out[key] = m.group(3).replace("\\'", "'")
    if "title" not in out or "heroTitle" not in out:
        sys.exit("pt sözlüğü okunamadı")
    return out


def esc_attr(s):
    return s.replace("&", "&amp;").replace('"', "&quot;")


def build():
    src = os.path.join(ROOT, "index.html")
    html = open(src, encoding="utf-8").read()
    pt = read_pt_dict(html)

    # 1) data-i18n içerikleri
    missing = []

    def fill(m):
        open_tag, tag, key, close = m.group(1), m.group(2), m.group(3), m.group(5)
        if key not in pt:
            missing.append(key)
            return m.group(0)
        return open_tag + pt[key] + close

    html = re.sub(r'(<(\w+)\b[^>]*\bdata-i18n="([\w-]+)"[^>]*>)(.*?)(</\2>)', fill, html, flags=re.S)
    if missing:
        sys.exit("pt'de eksik anahtar: " + ", ".join(sorted(set(missing))))

    def sub1(old, new, count=1):
        nonlocal html
        if html.count(old) < 1:
            sys.exit("bulunamadı: " + old[:70])
        html = html.replace(old, new, count)

    # 2) dil, başlık, açıklama, canonical, Open Graph
    sub1('<html lang="tr">', '<html lang="pt-BR">')
    sub1('<meta name="description" data-i18n-attr="description" content="',
         '<meta name="description" content="')
    html = re.sub(r'(<meta name="description" content=")[^"]*(")',
                  lambda m: m.group(1) + esc_attr(pt["description"]) + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:title" content=")[^"]*(")',
                  lambda m: m.group(1) + esc_attr(pt["title"]) + m.group(2), html, count=1)
    html = re.sub(r'(<meta property="og:description" content=")[^"]*(")',
                  lambda m: m.group(1) + esc_attr(pt["description"]) + m.group(2), html, count=1)
    sub1('<meta property="og:url" content="https://pomifocus.com/" />',
         f'<meta property="og:url" content="{PT_URL}" />')
    sub1('<meta property="og:locale" content="tr_TR" />', '<meta property="og:locale" content="pt_BR" />')
    sub1('<meta property="og:locale:alternate" content="en_US" />\n  <meta property="og:locale:alternate" content="pt_BR" />',
         '<meta property="og:locale:alternate" content="tr_TR" />\n  <meta property="og:locale:alternate" content="en_US" />')
    html = re.sub(r'  <link rel="alternate" hreflang="[^\n]*\n', '', html)   # ana sayfanın alternates'ı
    sub1('<link rel="canonical" href="https://pomifocus.com/" />',
         f'<link rel="canonical" href="{PT_URL}" />\n' + alternates())

    # 3) JSON-LD: sayfa adı/açıklaması/dili
    sub1('"name": "Pomi · Odaklan, bahçen büyüsün",', f'"name": "{pt["title"]}",')
    html = re.sub(r'("@type": "WebPage",.*?"url": ")https://pomifocus.com/(")',
                  lambda m: m.group(1) + PT_URL + m.group(2), html, count=1, flags=re.S)
    html = re.sub(r'("@id": "https://pomifocus.com/#webpage",\s*"url": ")[^"]*(")',
                  lambda m: m.group(1) + PT_URL + m.group(2), html, count=1)
    html = re.sub(r'("@id": "https://pomifocus.com/#webpage".*?"description": ")[^"]*(")',
                  lambda m: m.group(1) + pt["description"].replace('"', '\\"') + m.group(2), html, count=1, flags=re.S)
    html = re.sub(r'("@id": "https://pomifocus.com/#webpage".*?"inLanguage": ")tr(")',
                  lambda m: m.group(1) + "pt-BR" + m.group(2), html, count=1, flags=re.S)

    # 4) Dil düğmeleri: PT etkin
    sub1('<button class="lang-btn active" data-lang="tr"', '<button class="lang-btn" data-lang="tr"')
    sub1('<button class="lang-btn" data-lang="pt"', '<button class="lang-btn active" data-lang="pt"')

    # 5) Bu sayfa pt olarak açılır (kayıtlı tercih/tarayıcı dili sayfa dilini ezmesin)
    sub1("<script>document.documentElement.classList.add('js');</script>",
         "<script>document.documentElement.classList.add('js'); window.POMI_PAGE_LANG = 'pt';</script>")

    # 6) Göreli bağlantılar bir üst dizine; blog yazıları EN
    html = html.replace('href="blog/"', 'href="../blog/en.html"')
    html = re.sub(r'href="(?!https?:|mailto:|#|\.\./|data:|javascript:)([\w.-]+\.html)"',
                  r'href="../\1"', html)
    html = html.replace('href="./#', 'href="../#')

    out_dir = os.path.join(ROOT, "pt")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("pt/index.html yazıldı (%d anahtar)" % len(pt))


def alternates():
    return (f'  <link rel="alternate" hreflang="tr" href="{SITE}" />\n'
            f'  <link rel="alternate" hreflang="en" href="{SITE}" />\n'
            f'  <link rel="alternate" hreflang="pt-BR" href="{PT_URL}" />\n'
            f'  <link rel="alternate" hreflang="x-default" href="{SITE}" />')


if __name__ == "__main__":
    build()
