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
