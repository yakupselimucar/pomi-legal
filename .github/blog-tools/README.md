# Blog üretici

`blog/` altındaki HTML sayfalar, `blog/index.html`, `blog/en.html` ve `blog/feed.xml` bu betikle üretilir.

Yeni yazı eklemek için:
1. `posts.py` içine yeni bir `POSTS.append(dict(...))` bloğu ekle (slug, lang, title, desc, tldr, body, faq).
2. `python3 .github/blog-tools/build_blog.py` çalıştır.
3. `sitemap.xml` ve `llms.txt` dosyasına yeni URL'yi elle ekle.
4. Commit + push; Search Console'da sitemap'i yeniden gönder.

Elle düzenlenmiş HTML'ler betik çalışınca ezilir; içerik değişikliği her zaman `posts.py` üzerinden yapılmalı.
