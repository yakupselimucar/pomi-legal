# Blog üretici

`blog/` altındaki tüm HTML sayfalar, `blog/feed.xml`, kökteki `sitemap.xml`, `llms-full.txt` ve `llms.txt`'nin Blog bölümü bu betikle üretilir.

```
python3 .github/blog-tools/build_blog.py
```

## Dosyalar

| Dosya | İçerik |
|---|---|
| `posts.py` | İlk yazılar (karşılaştırma, öğrenci araçları, Pomodoro nedir, study with me) |
| `posts_technique.py` | TR: odak teknikleri, günde kaç pomodoro, mola, erteleme, sesler, evden çalışma |
| `posts_students.py` | TR: sınav planı, telefon, çalışma teknikleri, Forest alternatifleri |
| `posts_product.py` | TR: Pomi rehberi, fetih haritası, oyunlaştırma |
| `posts_en.py` | EN çiftler (hreflang ile TR'ye bağlı) |
| `brand_mark.py` | Ana sayfadaki `pomi(1)` logosunun statik SVG hâli; index.html'deki ızgara değişirse yeniden üret |

## Yeni yazı eklemek

1. Uygun `posts_*.py` dosyasına `POSTS.append(dict(...))` bloğu ekle. Zorunlu alanlar: `slug, lang, section, date, date_human, rfc822, read, words, title, short, h1, lead, desc, keywords, tldr, body, faq`. İsteğe bağlı: `pair` (diğer dildeki slug), `related` (en fazla 3 slug), `sources` (kaynak listesi, `citation` şemasına da girer), `itemlist` (liste yazıları), `howto` (adım adım rehber).
2. Betiği çalıştır. Betik kırık iç bağlantı, eksik çift ve tekrarlanan slug için hata verir.
3. Commit + push; Search Console ve Bing'de sitemap'i yeniden gönder.

Elle düzenlenmiş HTML'ler betik çalışınca ezilir; içerik değişikliği her zaman `posts_*.py` üzerinden yapılmalı.

## Kurallar

- Odalar için her zaman "herkes kendi sayacıyla"; "ortak sayaç" yazma.
- Rakip uygulamalar için fiyat ve puan gibi değişken sayılar verme; "Eylül 2026 mağaza sayfalarına göre" notu yeterli.
- Her yazıda "Kısa cevap" kutusu + SSS zorunlu (yapay zeka özetleri için).
- Araştırma atıfı yapılıyorsa `sources` alanına yazar/yıl/başlık ekle.

## İngilizce ve Portekizce ana sayfa (`build_locales.py`)

`en/index.html` ve `pt/index.html`, `index.html` içindeki `en: { ... }` ve `pt: { ... }` sözlüklerinden üretilen statik kopyalardır (hreflang ile ana sayfaya bağlı; sitemap'te `en/`, `pt/`). Google JS ile değişen dili dizine almadığı için "pomodoro timer" gibi İngilizce aramalar ancak `/en/` ile eşleşir.

```
python3 .github/blog-tools/build_locales.py
```

`index.html`'de metin ya da yapı değişince bu betiği de çalıştır; elle düzenlenen `en/` ve `pt/` sayfaları ezilir. Yeni bir `data-i18n` anahtarı eklersen üç sözlüğe de ekle (eksikse betik hata verir). Dile göre değişen bağlantılar `data-i18n-href` ile işaretlenir.

## Açılış sayfaları (`landing_content.py`)

`/pomodoro-sayaci/`, `/pomodoro-timer/`, `/online-kutuphane/`, `/study-together/` sayfaları `build_blog.py` tarafından `landing_content.py`'deki içerikten üretilir; sayacın mantığı `assets/timer.js`, stili `blog/blog.css` sonundadır. Hedef aramalar: pomodoro sayacı / pomodoro timer, online kütüphane / birlikte ders çalış / study together online. Odalar davet koduyla açılır, yabancılarla eşleştirme yoktur; oda sohbeti vardır. Bu gerçeklerin dışına çıkma.
