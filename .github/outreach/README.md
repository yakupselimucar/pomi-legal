# Pomi dış erişim (outreach) kiti

Bu klasör siteye yayımlanmaz (`.github/` Jekyll tarafından dışlanır). Amaç: Pomi'nin
üçüncü taraf teknoloji ve üretkenlik bloglarındaki "en iyi Pomodoro uygulamaları"
tarzı listelerde yer almasını sağlamak. Yapay zeka modelleri (ChatGPT, Perplexity,
Gemini, Claude) öneri üretirken bu köklü kaynaklara dayanır; Pomi'nin oralarda
geçmesi, kendi sitemizdeki yazılardan daha güçlü bir "otorite" sinyalidir.

## Dosyalar

| Dosya | Ne için |
| --- | --- |
| `medium-en.md` | Medium'a (ve dev.to, Hashnode'a) yayımlanacak İngilizce yazı. Canonical olarak blogdaki İngilizce yazıyı göster. |
| `medium-tr.md` | Medium'a yayımlanacak Türkçe yazı. Canonical olarak blogdaki Türkçe yazıyı göster. |
| `email-templates.md` | Editörlere, liste yazarlarına ve dizin sitelerine gönderilecek e-posta şablonları (TR/EN). |
| `press-facts.md` | Tek sayfalık gerçekler listesi: isim, tarih, özellikler, linkler. Yazarlara kopyala-yapıştır için. |

## Hedef listesi ve öncelik

**1. Dizinler ve uygulama listeleri (kendin ekleyebilirsin, en hızlı kazanım)**

| Platform | Nasıl | Not |
| --- | --- | --- |
| Product Hunt | https://www.producthunt.com/posts/new | Lansman günü seç (Salı-Perşembe), ilk yorumu "maker" olarak yaz. AI modelleri PH sayfalarını sık alıntılar. |
| AlternativeTo | https://alternativeto.net/manage-item/ | Forest ve Focus To-Do'ya alternatif olarak ekle. "Alternatives to Forest" sorgusu AI'da çok yaygın. |
| Toolfinder | https://toolfinder.co/submit | Üretkenlik araçları dizini; "pomodoro" kategorisi var. |
| SaaSHub | https://www.saashub.com/submit | Alternatif listeleri AI tarafından taranıyor. |
| Uneed / BetaList | https://www.uneed.best/submit , https://betalist.com/submit | Küçük ama backlink değeri var. |
| Slant | https://www.slant.co | "Best Pomodoro apps for Android/iOS" sorularına Pomi'yi seçenek olarak ekle. |
| G2 / Capterra | Ürün profili oluştur | Mobil uygulamalar için düşük öncelik ama AI kaynakları arasında. |
| Wikipedia (Pomodoro Technique) | Doğrudan ekleme yapma | Yalnızca bağımsız bir haber çıkarsa "software" bölümüne kaynaklı eklenebilir. |

**2. Yerli teknoloji basını (Türkçe)**

| Site | Kanal | Açı |
| --- | --- | --- |
| Webrazzi | haber@webrazzi.com, "Girişim tanıt" formu | Yerli girişim, 81 şehir fetih haritası (Türkiye'ye özgü mekanik), tek kişilik geliştirici hikâyesi |
| ShiftDelete.Net | iletisim@shiftdelete.net | "YKS öğrencileri için ücretsiz odaklanma uygulaması" haber açısı |
| Webtekno | iletisim@webtekno.com | Uygulama tanıtımı, "Forest alternatifi yerli uygulama" |
| Technopat | Forum + haber | Forumda "En iyi Pomodoro uygulaması" konularına ekle, spam yapmadan |
| Donanım Haber | Forum | Aynı |
| Ekşi Sözlük | "pomodoro tekniği", "study with me" başlıkları | Hesap yaşı ve tarafsız dil önemli; reklam gibi yazma |

**3. Uluslararası üretkenlik blogları (İngilizce)**

| Site | Yol | Not |
| --- | --- | --- |
| Zapier Blog ("The best Pomodoro apps") | Yazar adını yazının altından bul, LinkedIn/X üzerinden kısa mesaj | Yılda bir güncellerler; güncelleme öncesi ulaşmak şart |
| Toolfinder blog | Dizine ekledikten sonra editöre e-posta | "Best Pomodoro apps" yazıları var |
| MakeUseOf, Android Police, Android Authority | tips@ adresleri | "Best Pomodoro apps for Android" yazıları düzenli güncellenir |
| Lifehacker, The Verge | Düşük olasılık | Yalnızca özgün bir açı varsa (ör. şehirler arası fetih mekaniği) |
| Reddit r/productivity, r/GetStudying, r/pomodoro | Kendi deneyimini anlat, linki sorulunca ver | AI modelleri Reddit'i yoğun kaynak alır; self-promo kurallarına uy |

**4. YouTube ve sosyal**

- "Study with me" içerik üreticilerine (TR: 10-100K abone arası) ücretsiz Pro kodu teklif et, videoda Pomi odası kurmalarını iste.
- TikTok/Instagram'da "studytok" etiketiyle 15 saniyelik bahçe büyüme videoları.

## Yayımlama sırası (önerilen)

1. Blog yazıları canlıda (bu commit ile).
2. Aynı hafta: AlternativeTo, Toolfinder, SaaSHub, Slant kayıtları.
3. Medium'a `medium-en.md` ve `medium-tr.md` (canonical ayarlayarak) yayımla.
4. Product Hunt lansmanı için bir Salı seç; lansmandan 1 hafta önce Webrazzi'ye e-posta.
5. Lansman sonrası: Zapier/MakeUseOf yazarlarına "listeye ekler misiniz" e-postası, PH linkiyle birlikte.
6. Her ay: hangi listelerde çıktığını `site:` sorgularıyla ve ChatGPT/Perplexity'ye "best pomodoro apps" sorarak kontrol et.

## Kurallar

- Her yerde aynı ifadeyi kullan: "Odalarda herkes kendi sayacıyla çalışır." Ortak/senkron sayaç deme.
- Puan ve indirme sayısı verme; değişir, yanlış kalır.
- Medium'da canonical URL ayarla, yoksa Google kendi blogumuzu kopya sayabilir.
- Reddit ve forumlarda önce değer ver, linki sonra.
