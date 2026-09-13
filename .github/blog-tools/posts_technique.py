# -*- coding: utf-8 -*-
"""Türkçe yazılar: teknik, odak yöntemleri, erteleme, sesler, evden çalışma."""

IOS = "https://apps.apple.com/tr/app/id6784132034"
ANDROID = "https://play.google.com/store/apps/details?id=com.yakupselimucar.pomi"
SITE = "https://yakupselimucar.github.io/pomi-legal/"
D = "2026-09-13"
DH = "13 Eylül 2026"
RFC = "Sun, 13 Sep 2026 10:00:00 +0300"

POSTS = []

# ─────────────────────────────────────────────────────────────────
# Pomodoro mu, 52/17 mi, Flowtime mı?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="pomodoro-mu-flowtime-mi-52-17-odak-teknikleri", lang="tr", pair="pomodoro-vs-flowtime-vs-52-17",
  section="Karşılaştırma", date=D, date_human=DH, rfc822=RFC, read=7, words=1300,
  related=["pomodoro-teknigi-nedir", "gunde-kac-pomodoro-yapmali", "evden-calisirken-odaklanma"],
  title="Pomodoro mu, 52/17 mi, Flowtime mı? Odak Tekniklerinin Dürüst Karşılaştırması",
  short="Pomodoro, 52/17 ve Flowtime karşılaştırması",
  h1="Pomodoro mu, 52/17 mi, <span class=\"accent\">Flowtime</span> mı?",
  lead="Beş popüler odak tekniğini aynı sorularla karşılaştırdık: kim için, hangi iş için, nerede tökezliyor. Sonunda hangisini seçeceğine karar verebileceksin.",
  desc="Pomodoro, 52/17, Flowtime, 90 dakikalık ultradiyen blok ve zaman bloklama karşılaştırması. Her tekniğin kökeni, artıları, eksileri ve hangi iş türüne uyduğu.",
  keywords="pomodoro alternatifleri, 52 17 kuralı, flowtime tekniği, odak teknikleri, zaman yönetimi teknikleri, ultradiyen ritim, time blocking, derin çalışma",
  tldr="""<p><strong>Kısa cevap:</strong> Başlamakta zorlanıyorsan ve işin parçalara bölünebiliyorsa <strong>Pomodoro (25/5)</strong>. Bilgisayar başında uzun gün geçiriyorsan <strong>52/17</strong>. Akışa girince bölünmek istemiyorsan <strong>Flowtime</strong>. Yazılım, yazı ve araştırma gibi ısınma gerektiren işlerde <strong>90/20</strong>. Takvimin yoğunsa hepsinin üstüne <strong>zaman bloklama</strong>. Teknikler birbirini dışlamaz; çoğu insan ikisini birlikte kullanır.</p>""",
  body="""
<h2 id="neden-fark-eder">Teknik neden fark eder?</h2>
<p>Bütün odak teknikleri aynı iki soruna cevap arar: <strong>başlayamamak</strong> ve <strong>sürdürememek</strong>. Fark, sorunu nasıl çözdüklerinde. Pomodoro kısa ve kesin sınırlarla başlamayı kolaylaştırır; Flowtime sınırları kaldırıp akışı korur; 52/17 ve 90/20 sınırı vücudun doğal ritmine yaklaştırır. Doğru teknik, senin hangi sorundan daha çok çektiğine bağlı.</p>

<h2 id="tablo">Beş teknik tek tabloda</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Teknik</th><th>Döngü</th><th>Köken</th><th>En iyi olduğu iş</th><th>Zayıf noktası</th></tr></thead>
  <tbody>
    <tr><td>Pomodoro</td><td>25 dk çalış / 5 dk mola, 4 turda uzun mola</td><td>Francesco Cirillo, 1980'ler</td><td>Ders çalışma, soru çözme, e-posta, sevilmeyen işler</td><td>Akıştayken sayaç böler</td></tr>
    <tr><td>52/17</td><td>52 dk çalış / 17 dk mola</td><td>DeskTime kullanım verisi, 2014</td><td>Ofis işi, bilgisayar başı görevler</td><td>52 dakika, yeni başlayan için uzun</td></tr>
    <tr><td>Flowtime</td><td>Sıkılana kadar çalış, süreyi kaydet, orantılı mola</td><td>Zoë Read-Bivens, 2016</td><td>Yaratıcı iş, programlama, yazı</td><td>Disiplin ister; kayıt tutmazsan dağılır</td></tr>
    <tr><td>90/20 (ultradiyen)</td><td>90 dk çalış / 20 dk mola</td><td>Kleitman'ın uyku ritmi araştırması</td><td>Derin okuma, tez, tasarım</td><td>Günde 3-4 blok sınırı; kesintiye dayanıksız</td></tr>
    <tr><td>Zaman bloklama</td><td>Takvimde her işe saat aralığı</td><td>Cal Newport'un popülerleştirdiği yöntem</td><td>Toplantılı, çok görevli günler</td><td>Blok içinde ne yapacağını söylemez</td></tr>
  </tbody>
</table>
</div>

<h2 id="pomodoro">Pomodoro: 25 / 5</h2>
<p>Kuralları basit ve katı: 25 dakika tek iş, 5 dakika mola, dört turda 15-30 dakika uzun mola. Sayaç çalarken durursun, cümlenin ortasında bile olsan. Detaylı uygulamayı <a href="pomodoro-teknigi-nedir.html">Pomodoro tekniği rehberinde</a> anlattık.</p>
<ul>
  <li><strong>Artısı:</strong> Başlama eşiği çok düşük. 25 dakika, en isteksiz günde bile kabul edilebilir. Kesintileri sayabildiğin için dikkat dağıtıcıların gerçek boyutunu görürsün.</li>
  <li><strong>Eksisi:</strong> Akışa girdiğin 20. dakikada sayaç çalar. Cirillo bunu bilerek yapar ("mola kutsaldır"), ama yazılımcılar ve yazarlar için bu kural pahalıya patlayabilir.</li>
  <li><strong>Kime:</strong> Öğrenciler, ertelemeye eğilimli olanlar, dikkat eksikliği olanlar, işi küçük parçalara bölünebilenler.</li>
</ul>

<h2 id="52-17">52/17: verinin söylediği</h2>
<p>2014'te zaman takip uygulaması DeskTime, en verimli yüzde 10'luk kullanıcı diliminin ortalama <strong>52 dakika çalışıp 17 dakika ara verdiğini</strong> yayımladı. Bilimsel bir deney değil, kullanım verisinden çıkarılmış bir gözlem; ama sayılar çoğu ofis çalışanı için mantıklı bir orta yol sunuyor. Mola uzun olduğu için gerçekten ekrandan kalkarsın.</p>
<ul>
  <li><strong>Artısı:</strong> Isınma için yeterli süre, gerçek dinlenme için yeterli mola.</li>
  <li><strong>Eksisi:</strong> 52 dakika kesintisiz odak, alışkın olmayan için zor. Molanın 17 dakikası sosyal medyaya giderse tekniğin anlamı kalmaz.</li>
  <li><strong>Kime:</strong> Bilgisayar başında tam gün çalışanlar, Pomodoro'yu fazla bölücü bulanlar.</li>
</ul>

<h2 id="flowtime">Flowtime: sayaç yok, kayıt var</h2>
<p>Zoë Read-Bivens'ın 2016'da önerdiği yöntem Pomodoro'nun en çok eleştirilen kuralını, zorunlu kesintiyi kaldırır. Bir görev seçersin, başlangıç saatini not edersin, dikkatin dağılana ya da yorulana kadar çalışırsın, bitişi not edersin. Mola süresi çalıştığın süreyle orantılı: 25 dakikaya 5, 50'ye 8, 90'a 15 gibi.</p>
<ul>
  <li><strong>Artısı:</strong> Akışı korur. Kayıtlar zamanla senin gerçek odak süreni gösterir; çoğu insan 35-45 dakikada zirve yaptığını keşfeder.</li>
  <li><strong>Eksisi:</strong> Dış sınır olmadığı için "biraz daha" tuzağına düşmek kolay. Kayıt tutmayı bırakırsan teknik buharlaşır.</li>
  <li><strong>Kime:</strong> Deneyimli odaklananlar, programcılar, yazarlar, tasarımcılar.</li>
</ul>

<h2 id="90-20">90/20: ultradiyen ritim</h2>
<p>Uyku araştırmacısı Nathaniel Kleitman, uykuda 90 dakikalık döngüler olduğunu ve benzer bir dinlenme-uyanıklık dalgasının gün boyunca da sürdüğünü öne sürdü. Buradan türetilen 90/20, işi vücudun doğal dalgasına oturtmayı hedefler. Anders Ericsson'un uzman kemancılar üzerindeki çalışması da benzer bir tabloya işaret eder: en iyi öğrenciler günde toplam 4 saati geçmeyen, yaklaşık 90 dakikalık bloklar hâlinde çalışır.</p>
<ul>
  <li><strong>Artısı:</strong> Derin işe gerçekten dalmaya izin verir.</li>
  <li><strong>Eksisi:</strong> Günde en fazla 3-4 blok yapabilirsin. Açık ofiste ya da kalabalık evde 90 dakika kesintisizlik bulmak zor.</li>
  <li><strong>Kime:</strong> Tez yazanlar, araştırmacılar, sabah saatlerini kendine ayırabilenler.</li>
</ul>

<h2 id="time-blocking">Zaman bloklama: takvim tekniği</h2>
<p>Bu bir ritim değil, planlama yöntemi. Günün başında ya da önceki akşam her işe takvimde bir saat aralığı ayırırsın: 09:00-10:30 rapor, 10:30-11:00 e-posta, 11:00-12:30 kod. Blok içinde ne yapacağını söylemez; o yüzden Pomodoro veya 52/17 ile birlikte kullanılır. Takvimin dolu olduğu bir günde en gerçekçi tekniktir çünkü toplantıların etrafındaki boşlukları görünür kılar.</p>

<h2 id="birlestirme">Teknikleri birleştirmek</h2>
<p>Pratikte insanlar tek tekniğe bağlı kalmaz. İşe yaradığını gördüğümüz üç kombinasyon:</p>
<ol>
  <li><strong>Blok + Pomodoro:</strong> Takvimde 2 saatlik "ders" bloğu, içinde 4 pomodoro. Öğrenciler için en güvenli düzen.</li>
  <li><strong>Pomodoro ile ısın, Flowtime ile sür:</strong> Güne bir 25'likle başla; akışa girdiysen sayacı kapat, süreyi not et. İsteksiz sabahlar için.</li>
  <li><strong>Sabah 90/20, öğleden sonra 25/5:</strong> Zihin en tazeyken derin iş, enerjinin düştüğü saatlerde kısa turlar.</li>
</ol>
<p>Pomi'de çalışma ve mola sürelerini serbestçe ayarlayabildiğin için aynı uygulamayla 25/5, 52/17 veya 90/20 çalışabilirsin; bahçedeki bitki, hangi süreyi seçersen seç seans tamamlanınca büyür. Günde kaç tur yapmanın gerçekçi olduğunu <a href="gunde-kac-pomodoro-yapmali.html">ayrı bir yazıda</a> ele aldık.</p>

<h2 id="secim">Nasıl seçmeli? Üç soru</h2>
<ul>
  <li><strong>Asıl sorunum başlamak mı?</strong> Evetse Pomodoro. Kısa sınır, başlama direncini kırar.</li>
  <li><strong>Akışa girince bölünmek beni kızdırıyor mu?</strong> Evetse Flowtime veya 90/20.</li>
  <li><strong>Günüm toplantı ve kesintiyle dolu mu?</strong> Evetse önce zaman bloklama, boşluklara Pomodoro.</li>
</ul>
<p>Hangisini seçersen seç iki hafta değiştirmeden dene. Teknik değiştirmek, çalışmamanın en sofistike biçimi olabilir.</p>
""",
  faq=[
    ("52/17 kuralı nedir?", "52 dakika kesintisiz çalışıp 17 dakika mola vermeye dayanan bir düzendir. 2014'te zaman takip uygulaması DeskTime'ın en verimli kullanıcılarının ortalamasından türetildi; bilimsel bir deney değil, kullanım verisine dayalı bir gözlemdir."),
    ("Flowtime tekniği nedir?", "Zorunlu sayaç olmadan, dikkatin dağılana kadar çalışıp başlangıç ve bitiş saatini kaydettiğin, sonra çalıştığın süreyle orantılı mola verdiğin bir yöntemdir. Pomodoro'nun akışı bölme sorununu çözmek için 2016'da Zoë Read-Bivens tarafından önerildi."),
    ("Pomodoro mu Flowtime mı daha iyi?", "Başlamakta zorlanıyorsan ve işin parçalara bölünebiliyorsa Pomodoro; akışa girince bölünmek istemediğin yaratıcı işlerde Flowtime daha iyi çalışır. Çoğu kişi Pomodoro ile başlayıp deneyim kazandıkça Flowtime'a geçer veya ikisini birlikte kullanır."),
    ("90 dakika kuralı ne demek?", "Kleitman'ın ultradiyen ritim araştırmasından türetilen, 90 dakika çalışıp 20 dakika dinlenmeye dayanan düzendir. Derin ve uzun iş için uygundur ama günde en fazla 3-4 blok yapılabilir."),
    ("Pomi ile 52/17 veya 90/20 çalışabilir miyim?", "Evet. Pomi'de çalışma ve mola sürelerini ayarlardan değiştirebilirsin. Seans hangi uzunlukta olursa olsun tamamlandığında bahçene bitki eklenir ve şehrine puan yazılır."),
  ],
  sources=[
    "Cirillo, F. (2018). <em>The Pomodoro Technique</em>. Currency.",
    "DeskTime (2014). \"The secret of the 10% most productive people? Breaking!\" DeskTime blog.",
    "Read-Bivens, Z. (2016). \"The Flowtime Technique.\" Medium.",
    "Kleitman, N. (1963). <em>Sleep and Wakefulness</em>. University of Chicago Press.",
    "Ericsson, K. A., Krampe, R. T. &amp; Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. <em>Psychological Review</em>, 100(3).",
    "Newport, C. (2016). <em>Deep Work</em>. Grand Central Publishing.",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Günde kaç pomodoro?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="gunde-kac-pomodoro-yapmali", lang="tr", pair="how-many-pomodoros-a-day",
  section="Rehber", date=D, date_human=DH, rfc822=RFC, read=6, words=1100,
  related=["pomodoro-teknigi-nedir", "pomodoro-molasinda-ne-yapmali", "sinava-hazirlanirken-pomodoro"],
  title="Günde Kaç Pomodoro Yapmalı? Gerçekçi Hedefler ve Sık Yapılan Hata",
  short="Günde kaç pomodoro",
  h1="Günde kaç <span class=\"accent\">pomodoro</span> yapmalı?",
  lead="\"16 pomodoro yaptım\" cümlesi etkileyici ama çoğu zaman yanlış hedef. Öğrenci, çalışan ve tez yazan için gerçekçi sayılar, sayıyı nasıl artıracağın ve ne zaman durman gerektiği.",
  desc="Günde kaç pomodoro yapılmalı? Öğrenciler, çalışanlar ve uzaktan çalışanlar için gerçekçi hedefler, 8 pomodoro kuralı, sayıyı kademeli artırma planı ve tükenmişlik işaretleri.",
  keywords="günde kaç pomodoro, kaç pomodoro yapmalı, pomodoro hedef, günde kaç saat ders çalışmalı, verimli çalışma süresi, odak süresi",
  tldr="""<p><strong>Kısa cevap:</strong> Yeni başlıyorsan günde <strong>4 pomodoro</strong> (100 dakika net odak) iyi bir hedef. Alışınca çoğu öğrenci ve çalışan için sürdürülebilir üst sınır <strong>8 ile 12</strong> arası; bu 3,5 ile 5 saat gerçek odak demektir ve tam gün ofis çalışmasının çoğundan fazladır. 16 ve üstü, sınav haftası gibi kısa dönemler dışında tükenmişlik tarifi olur.</p>""",
  body="""
<h2 id="yanlis-hedef">Neden "ne kadar çok o kadar iyi" yanlış?</h2>
<p>Pomodoro sayısı bir <strong>çıktı</strong> değil, <strong>girdi</strong> ölçüsüdür. Sekiz seans oturup hiçbir soru çözmeden geçirmek mümkün; üç seansta bir konuyu bitirmek de. Yine de sayı işe yarar, çünkü ölçülebilen tek şey odur ve zaman içinde kendinle karşılaştırmanı sağlar.</p>
<p>İkinci sorun, bir pomodoronun 25 değil <strong>30 dakika</strong> sürmesidir (mola dâhil). Uzun molalarla birlikte 8 pomodoro yaklaşık 4,5 saat eder. 16 pomodoro ise 9 saat demektir ve o günün içinde yemek, yol, ders ya da toplantı yoktur.</p>

<h2 id="sayilar">Kim için kaç pomodoro?</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Durum</th><th>Günlük hedef</th><th>Net odak</th><th>Not</th></tr></thead>
  <tbody>
    <tr><td>Yeni başlayan</td><td>3-4</td><td>75-100 dk</td><td>İlk iki hafta sayıyı değil düzenliliği hedefle</td></tr>
    <tr><td>Okula giden öğrenci</td><td>4-6</td><td>100-150 dk</td><td>Ders dışı saatlerde; hafta sonu 8'e çıkabilir</td></tr>
    <tr><td>Sınava hazırlanan (tam gün)</td><td>10-14</td><td>4-6 saat</td><td>İki-üç aylık dönemler için; ara vermeden 6 hafta sürdürme</td></tr>
    <tr><td>Tam zamanlı çalışan</td><td>6-8</td><td>2,5-3,5 saat</td><td>Kalan mesai toplantı, e-posta ve sığ işe gider</td></tr>
    <tr><td>Uzaktan çalışan / serbest</td><td>8-10</td><td>3,5-4 saat</td><td>Kesinti az olduğundan üst sınır biraz yüksek</td></tr>
    <tr><td>Tez, kitap, araştırma</td><td>6-8 (uzun bloklu)</td><td>3-4 saat</td><td>50/10 kullanıyorsan sayı yarıya iner, süre aynı kalır</td></tr>
  </tbody>
</table>
</div>

<h2 id="4-saat">4 saat tavanı</h2>
<p>Bu tablodaki üst sınırlar rastgele değil. Anders Ericsson'un 1993'te yayımladığı ve "10.000 saat" tartışmasını başlatan çalışmada en iyi keman öğrencilerinin günde ortalama 4 saatten fazla bilinçli pratik yapmadığı görüldü; daha uzun süreler kaliteyi düşürüyordu. Yazarlar ve matematikçiler üzerine yapılan gözlemler de benzer: derin, dikkat isteyen işte günde 4-5 saat çoğu insan için tavan. Bunun üstü ya sığ işe kayar ya da ertesi güne borç olur.</p>
<p class="note">Bu tavan "toplam çalışma" değil, "yoğun odak" tavanı. Okuma, tekrar ve düzenleme gibi daha hafif işler bunun üstüne eklenebilir.</p>

<h2 id="artirma">Sayıyı nasıl artırırsın?</h2>
<ol>
  <li><strong>Önce düzenlilik.</strong> İki hafta boyunca her gün 3 pomodoro. Günü kaçırmamak, 8 yapmaktan önemli.</li>
  <li><strong>Haftada bir seans ekle.</strong> 3'ten 4'e, 4'ten 5'e. Sıçrama yapma; sıçrama ertesi gün sıfıra düşürür.</li>
  <li><strong>Sabah bloğunu koru.</strong> İlk 4 pomodoroyu günün en erken boş saatine koy. Öğleden sonra eklenenler bonus.</li>
  <li><strong>Kesintileri say.</strong> Cirillo'nun orijinal yönteminde her kesinti işaretlenir. Kesinti sayısı düşmeden seans sayısı artmaz.</li>
  <li><strong>Sayıyı görünür tut.</strong> Kâğıtta çetele, takvimde X ya da Pomi'de bahçe. Görünür ilerleme, sayıyı artırmanın en ucuz yolu.</li>
</ol>

<h2 id="dur">Ne zaman durmalı?</h2>
<p>Şu üç işaret ertesi güne zarar verdiğinin sinyali: aynı paragrafı üç kez okumak, molada telefona uzanma sıklığının artması ve seans sonunda ne yaptığını hatırlayamamak. Böyle bir günde 6. pomodoroyu zorlamak yerine yürüyüşe çıkmak, ertesi günkü 8 pomodoroyu kurtarır.</p>

<h2 id="haftalik">Günlük yerine haftalık düşün</h2>
<p>Günlük hedef, kötü bir günün seni "başarısız" hissettirmesine yol açar. Haftalık hedef daha bağışlayıcı: haftada 30 pomodoro, günde 4 ile 8 arasında dalgalanabilir. Pomi'nin haftalık istatistik ekranı ve haftalık lig tam bu mantıkla çalışır; seni bugünle değil, haftanla değerlendirir.</p>
""",
  faq=[
    ("Günde kaç pomodoro yapılmalı?", "Yeni başlayanlar için 3-4, alışkın kullanıcılar için 8-12 pomodoro gerçekçi bir aralıktır. 12 pomodoro yaklaşık 5 saat net odak demektir ve derin iş için günlük tavana yakındır."),
    ("8 pomodoro kaç saat eder?", "Molalar dâhil yaklaşık 4,5 saat. Net odak süresi 8 × 25 = 200 dakika, yani 3 saat 20 dakikadır."),
    ("Günde 16 pomodoro yapmak mümkün mü?", "Kısa dönemler için mümkün ama sürdürülebilir değil. 16 pomodoro molalarla 9 saat demektir. Sınav haftası gibi istisnalar dışında 12'nin üstü çoğu kişide ertesi gün verim düşüşüne yol açar."),
    ("Kaç saat ders çalışmalıyım?", "Okula giden bir öğrenci için ders dışında 2-2,5 saat (4-6 pomodoro) net odak yeterlidir. Tam gün sınava hazırlananlar için 4-6 saat net odak üst sınırdır; kalan zaman tekrar ve hafif işe ayrılabilir."),
    ("Pomodoro sayısını nasıl takip ederim?", "Kâğıt çetele en basit yol. Uygulama kullanıyorsan Pomi her tamamlanan seansı bahçene bitki olarak ekler ve haftalık istatistikte toplamı gösterir; böylece sayıya bakmadan da ilerlemeni görürsün."),
  ],
  sources=[
    "Ericsson, K. A., Krampe, R. T. &amp; Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. <em>Psychological Review</em>, 100(3).",
    "Cirillo, F. (2018). <em>The Pomodoro Technique</em>. Currency.",
    "Newport, C. (2016). <em>Deep Work</em>. Grand Central Publishing.",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Pomodoro molasında ne yapmalı?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="pomodoro-molasinda-ne-yapmali", lang="tr",
  section="Rehber", date=D, date_human=DH, rfc822=RFC, read=5, words=950,
  related=["pomodoro-teknigi-nedir", "gunde-kac-pomodoro-yapmali", "ders-calisirken-telefonu-birakmak"],
  title="Pomodoro Molasında Ne Yapmalı? 5 Dakikayı İyi Kullanmanın 12 Yolu",
  short="Pomodoro molasında ne yapmalı",
  h1="Pomodoro molasında <span class=\"accent\">ne yapmalı</span>?",
  lead="Mola, tekniğin en çok ihmal edilen yarısı. Kötü bir mola sonraki seansı bozar; iyi bir mola onu kurtarır. Kısa ve uzun molalar için somut liste.",
  desc="Pomodoro molasında ne yapılır? 5 dakikalık kısa mola ve 15-30 dakikalık uzun mola için 12 öneri, molada yapılmaması gerekenler ve telefonun neden en kötü mola olduğu.",
  keywords="pomodoro molası, pomodoro mola ne yapmalı, 5 dakika mola, ders çalışma molası, uzun mola, mola aktiviteleri, çalışma arası",
  tldr="""<p><strong>Kısa cevap:</strong> Molada yapılacak en iyi şey, seansta yapmadığın şeydir: <strong>ayağa kalk, ekrandan uzaklaş, gözünü uzağa çevir, su iç</strong>. En kötü mola, sosyal medyaya bakmaktır; 5 dakika 20 olur ve dikkat sıfırlanır. Uzun molada dışarı çık, bir şey ye ya da kısa bir şekerleme yap.</p>""",
  body="""
<h2 id="neden">Mola neden bu kadar önemli?</h2>
<p>Dikkat sabit bir kaynak değil, dalgalanan bir şey. Illinois Üniversitesi'nden Ariga ve Lleras'ın 2011 deneyinde, 50 dakikalık tekdüze bir görev sırasında kısa ve seyrek aralar veren katılımcıların performansı korundu; aralıksız çalışanlarınki belirgin biçimde düştü. Mola, dinlenmek için değil, sonraki 25 dakikayı ilk 25 dakika kadar verimli kılmak için var.</p>
<p>İyi bir molanın üç özelliği var: <strong>fiziksel olarak farklı</strong> (oturduysan kalk), <strong>bilişsel olarak hafif</strong> (yeni bilgi yükleme) ve <strong>zamanla sınırlı</strong> (sayaç molada da çalışsın).</p>

<h2 id="kisa">5 dakikalık kısa mola: 8 öneri</h2>
<ol>
  <li><strong>Ayağa kalk ve gerin.</strong> Boyun, omuz, bel. Oturma pozisyonunu kırmak tek başına yeter.</li>
  <li><strong>20-20-20 kuralı.</strong> 20 saniye boyunca 6 metre uzaktaki bir noktaya bak. Göz yorgunluğunu azaltır; ekran başında çalışanlar için en önemlisi bu.</li>
  <li><strong>Su iç.</strong> Bardağı masadan uzak tut ki gitmek zorunda kal.</li>
  <li><strong>Pencereyi aç, iki derin nefes.</strong> Odanın havası 4 seansta belirgin ağırlaşır.</li>
  <li><strong>Küçük bir fiziksel iş.</strong> Bulaşığı makineye koy, masayı topla. Zihni boşaltır, üstelik gün sonunda ev toplanmış olur.</li>
  <li><strong>Bir sonraki seansı yaz.</strong> Tek cümle: "Sonraki 25 dakikada X." Molayı bitirince karar vermek için zaman kaybetmezsin.</li>
  <li><strong>Gözlerini kapat.</strong> 2 dakika, hiçbir şey yapmadan. Sıkıcı gelir; tam da bu yüzden işe yarar.</li>
  <li><strong>Bir kişiyle iki cümle konuş.</strong> Aynı evde biri varsa "nasıl gidiyor?" yeter. Odada arkadaşlarınla çalışıyorsan mola, sohbetin tek yeri.</li>
</ol>

<h2 id="uzun">15-30 dakikalık uzun mola: 4 öneri</h2>
<ol>
  <li><strong>Dışarı çık.</strong> 10 dakikalık yürüyüş, sonraki bloğun kalitesini en çok artıran şey. Hava kötüyse merdiven.</li>
  <li><strong>Bir şey ye.</strong> Meyve, kuruyemiş, yoğurt. Ağır yemek uzun molayı uyku molasına çevirir.</li>
  <li><strong>Kısa şekerleme.</strong> 10-20 dakika, alarm kurarak. 30'u geçerse uyku ataleti başlar ve sonraki seans gider.</li>
  <li><strong>Duş veya yüz yıkama.</strong> Öğleden sonraki çöküşü toparlamanın en hızlı yolu.</li>
</ol>

<h2 id="yapma">Molada yapılmaması gerekenler</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Yapma</th><th>Neden</th><th>Yerine</th></tr></thead>
  <tbody>
    <tr><td>Sosyal medya</td><td>5 dakika 20 olur; akış, dikkat kaynaklarını yeniden yükler, boşaltmaz</td><td>Telefonu başka odada bırak</td></tr>
    <tr><td>E-posta ve mesaj kontrolü</td><td>Cevap gerektiren bir şey görürsen sonraki seans o mesajı düşünerek geçer</td><td>Uzun molada, sınırlı süreyle bak</td></tr>
    <tr><td>Yeni bir konu okumak</td><td>Bilişsel yük eklersin, mola dinlendirmez</td><td>Göz kapatma veya yürüyüş</td></tr>
    <tr><td>"Şunu da bitireyim" demek</td><td>Molayı atlamak birkaç turdan sonra çöküşe götürür</td><td>Kaldığın yeri not et, kalk</td></tr>
    <tr><td>Video başlatmak</td><td>Videonun süresi molanın süresini belirler, tersi değil</td><td>Müzik olabilir; tek parça</td></tr>
  </tbody>
</table>
</div>

<h2 id="telefon">Telefon neden en kötü mola?</h2>
<p>Sorun sadece sürenin uzaması değil. Texas Üniversitesi'nden Ward ve arkadaşlarının 2017 çalışmasında telefonun sessizde bile masada durması çalışma belleği performansını düşürdü; katılımcılar başka odaya bıraktığında fark kapandı. Molada telefona bakmak, sonraki seansa "yarım kalmış bildirim" hissiyle girmek demektir. Telefonu bırakmanın yollarını <a href="ders-calisirken-telefonu-birakmak.html">ayrı bir yazıda</a> topladık.</p>

<h2 id="pomi">Pomi'de mola</h2>
<p>Pomi'de mola sayacı otomatik başlar, süresini ayarlardan değiştirebilirsin. Seans tamamlandığında bahçene eklenen bitkiyi görmek, molaya girerken küçük bir "bitirdim" hissi verir; sonraki seansa dönmeyi kolaylaştıran da bu his. Odada arkadaşlarınla çalışıyorsan herkesin kendi sayacı olduğu için molaların çakışmak zorunda değil; biri molada, diğeri seansta olabilir.</p>
""",
  faq=[
    ("Pomodoro molası kaç dakika?", "Kısa mola 5 dakika, dört pomodoro sonundaki uzun mola 15 ile 30 dakika arasıdır. 50/10 gibi uzun döngülerde kısa mola 10 dakikaya çıkar."),
    ("Pomodoro molasında telefona bakabilir miyim?", "Önerilmez. Sosyal medya 5 dakikayı kolayca 20 dakikaya çıkarır ve dikkat kaynaklarını dinlendirmek yerine yeniden yükler. Telefona bakman gerekiyorsa uzun molada, süreyi sınırlayarak bak."),
    ("Molada uyumak iyi fikir mi?", "Uzun molada 10-20 dakikalık şekerleme faydalıdır, ama alarm kur. 30 dakikayı geçen uyku, uyku ataletine yol açar ve sonraki seansı bozar. Kısa 5 dakikalık molada uyumaya çalışma."),
    ("Molada yemek yiyebilir miyim?", "Kısa molada hafif atıştırma (meyve, kuruyemiş) uygun. Ana öğünü uzun molaya ya da blok sonuna bırak; ağır yemek sonraki seansta uyku getirir."),
    ("Molayı atlamak zararlı mı?", "Bir kez atlamak sorun değil ama alışkanlık hâline gelirse birkaç tur sonra dikkat belirgin biçimde düşer. Akıştaysan bir pomodoro daha yap, ama ardından molayı mutlaka ver."),
  ],
  sources=[
    "Ariga, A. &amp; Lleras, A. (2011). Brief and rare mental \"breaks\" keep you focused: Deactivation and reactivation of task goals preempt vigilance decrements. <em>Cognition</em>, 118(3).",
    "Ward, A. F., Duke, K., Gneezy, A. &amp; Bos, M. W. (2017). Brain Drain: The mere presence of one's own smartphone reduces available cognitive capacity. <em>Journal of the Association for Consumer Research</em>, 2(2).",
    "Cirillo, F. (2018). <em>The Pomodoro Technique</em>. Currency.",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Erteleme
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="erteleme-aliskanligini-yenmek", lang="tr", pair="how-to-stop-procrastinating",
  section="Temel bilgi", date=D, date_human=DH, rfc822=RFC, read=7, words=1300,
  related=["pomodoro-teknigi-nedir", "study-with-me-birlikte-ders-calisma", "ders-calisirken-telefonu-birakmak"],
  title="Erteleme Alışkanlığını Yenmek: Neden Erteliyoruz ve Bugün Ne Yapabiliriz?",
  short="Erteleme alışkanlığını yenmek",
  h1="Erteleme alışkanlığını <span class=\"accent\">yenmek</span>",
  lead="Erteleme bir zaman yönetimi sorunu değil, duygu yönetimi sorunu. Araştırmaların söylediği bu. Buradan çıkan çözümler de \"daha disiplinli ol\"dan farklı.",
  desc="Erteleme neden olur, nasıl yenilir? Araştırmalara göre ertelemenin duygusal kökeni, 2 dakika kuralı, uygulama niyetleri, Pomodoro ve birlikte çalışma ile bugün uygulanabilecek 7 yöntem.",
  keywords="erteleme alışkanlığı, prokrastinasyon, ertelemeyi yenmek, neden erteliyoruz, ders çalışmaya nasıl başlanır, motivasyon, 2 dakika kuralı, akademik erteleme",
  tldr="""<p><strong>Kısa cevap:</strong> Ertelemek tembellik değil, hoş olmayan bir duygudan (sıkıntı, kaygı, yetersizlik hissi) kısa vadede kaçmaktır. Bu yüzden çözüm, duyguyu küçültmekten geçer: görevi <strong>2 dakikada başlanacak kadar küçült</strong>, ne zaman nerede yapacağını <strong>önceden yaz</strong>, <strong>25 dakikalık bir sayaç</strong> kur ve mümkünse <strong>başkalarının yanında</strong> çalış. İlk 5 dakika geçince duygunun yarısı gider.</p>""",
  body="""
<h2 id="nedir">Erteleme nedir, ne değildir?</h2>
<p>Erteleme, daha kötü sonuçlanacağını bile bile bir işi gönüllü olarak geciktirmektir. Kritik kelime "bile bile": bilgi eksikliği yok, plan eksikliği çoğu zaman yok. Piers Steel'in 2007'de 691 çalışmayı tarayan meta-analizine göre üniversite öğrencilerinin yüzde 80 ile 95'i düzenli erteliyor ve yaklaşık yarısı bunu sorun olarak görüyor. Yani ertelemek istisna değil, varsayılan durum.</p>
<p>Steel'in bulgularına göre ertelemeyi en güçlü yordayan şeyler görevin <strong>sevimsizliği</strong>, ödülün <strong>uzaklığı</strong>, kişinin <strong>dürtüselliği</strong> ve <strong>başarabileceğine inancının azlığı</strong>. Zaman yönetimi becerisi bu listede en altta.</p>

<h2 id="duygu">Asıl mekanizma: kısa vadeli duygu onarımı</h2>
<p>Fuschia Sirois ve Timothy Pychyl'in 2013'te öne sürdüğü çerçeve bugün alanın ana modeli: erteleme, <strong>şu anki kötü hissi düzeltmek için gelecekteki kendini feda etmektir</strong>. Ders kitabını açmak sıkıntı, kaygı ya da "yapamayacağım" hissi yaratır; telefona uzanmak bu hissi anında dindirir. Beyin bu döngüyü öğrenir. Sonuç suçluluk, suçluluk daha fazla kaçınma.</p>
<p>Bu modelin pratik sonucu şu: "Kendine kız, disiplinli ol" yaklaşımı kötü hissi büyüttüğü için ertelemeyi <strong>artırır</strong>. Aynı ekibin öğrencilerle yaptığı çalışmada ilk sınavdan önce ertelediği için kendini affedenler, ikinci sınavda daha az erteledi.</p>

<h2 id="yontemler">Bugün uygulanabilecek 7 yöntem</h2>

<h3>1. Görevi 2 dakikaya küçült</h3>
<p>David Allen'ın kuralı biraz farklı bir amaç için: "Konuya çalış" yerine "kitabı aç, ilk başlığı oku." İki dakikalık işin yarattığı duygu küçük olduğu için kaçınma da küçük olur. Başladıktan sonra devam etmek, başlamaktan çok daha kolay.</p>

<h3>2. Ne zaman, nerede, ne: uygulama niyeti yaz</h3>
<p>Peter Gollwitzer'in araştırmalarında "hedefim X" diyenlere kıyasla "Y durumunda Z yapacağım" biçiminde plan yazanlar hedefe iki-üç kat daha sık ulaştı. Cümle şöyle: <em>"Yarın 09:00'da mutfak masasında matematik soru bankası sayfa 40'ı açacağım."</em> Karar anını sabah 9'a değil, bu akşama taşımış olursun.</p>

<h3>3. 25 dakikalık sayaç kur</h3>
<p>Pomodoro'nun erteleme üzerinde iyi çalışmasının nedeni, bitişin baştan belli olması. "Üç saat çalışacağım" belirsiz ve ürkütücü; "25 dakika, sonra kalkacağım" katlanılabilir. Sayaç başladığında en zor kısım, yani başlamak, geride kalmıştır. Uygulama için <a href="pomodoro-teknigi-nedir.html">Pomodoro rehberine</a> bak.</p>

<h3>4. Ortamı önceden kur</h3>
<p>Ertelenen işin başlangıç maliyetini sıfıra indir: kitap açık, defter yanında, telefon başka odada, su masada. Bir akşam önce hazırlanan masa, sabah verilecek beş küçük kararı ortadan kaldırır.</p>

<h3>5. Başkalarının yanında çalış</h3>
<p>Kütüphane, kafe ya da çevrimiçi bir odak odası. Bir başkasının çalıştığını görmek başlama eşiğini düşürür; buna body doubling deniyor. Pomi'de arkadaşlarınla bir oda açıp herkesin kendi sayacıyla girmesi bu etkiyi evden sağlar. Mekanizmayı <a href="study-with-me-birlikte-ders-calisma.html">study with me yazısında</a> anlattık.</p>

<h3>6. İlerlemeyi görünür kıl</h3>
<p>Ertelemenin bir nedeni ödülün uzaklığı. Aradaki mesafeyi küçük, görünür ödüllerle doldur: takvimde çarpı, çetele, tamamlanan seans başına bahçeye eklenen bir bitki. Sistemin kendisi önemli değil; önemli olan bugün yaptığın işin bugün bir iz bırakması.</p>

<h3>7. Kendini affet, sonra 2 dakikaya dön</h3>
<p>Bu bir yumuşaklık önerisi değil, araştırma bulgusu. Ertelediğin için kendine kızdığın her dakika, ertelemenin beslendiği duyguyu büyütür. "Dün olmadı, şimdi kitabı açıyorum" cümlesi döngüyü kırar.</p>

<h2 id="kronik">Ne zaman daha fazlası gerekir?</h2>
<p>Erteleme her alanı kapsıyorsa, aylardır sürüyor ve uyku, ilişkiler ya da sağlıkla ilgili işleri de içine alıyorsa, altında dikkat eksikliği, depresyon ya da kaygı bozukluğu olabilir. Bu durumda yukarıdaki yöntemler yardımcı olur ama yeterli olmaz; bir uzmanla konuşmak en kısa yol.</p>

<h2 id="ozet">Tek cümlelik özet</h2>
<p>Erteleme duyguyla ilgili olduğu için çözüm de duyguyla ilgili: görevi küçült, kararı önceden ver, süreyi sınırla, yalnız kalma, kendini affet. Bunların hepsi 25 dakikalık tek bir seansa sığar.</p>
""",
  faq=[
    ("Neden sürekli erteliyorum?", "Araştırmalara göre erteleme, görevin yarattığı hoş olmayan duygudan (sıkıntı, kaygı, yetersizlik hissi) kısa vadede kaçmaktır. Tembellik ya da zaman yönetimi sorunu değil, duygu düzenleme sorunudur. Bu yüzden kendini eleştirmek ertelemeyi artırır."),
    ("Ertelemeyi yenmenin en hızlı yolu nedir?", "Görevi 2 dakikada başlanacak kadar küçültmek ve 25 dakikalık bir sayaç kurmak. Başlamak en zor kısımdır; sayaç başladıktan sonra devam etmek görece kolaydır."),
    ("2 dakika kuralı nedir?", "Bir işe başlamayı 2 dakikada yapılabilecek en küçük adıma indirmektir: \"kitabı aç, ilk paragrafı oku\" gibi. Küçük adım küçük duygu yaratır, kaçınma azalır."),
    ("Pomodoro erteleme için işe yarar mı?", "Evet, özellikle başlayamama sorununda. Sürenin sınırlı olması başlama direncini düşürür, mola zorunluluğu da tükenmeyi önler. Uzun vadede birlikte çalışma ve görünür ilerlemeyle desteklenmesi gerekir."),
    ("Erteleme bir hastalık mı?", "Tek başına değil; öğrencilerin büyük çoğunluğu düzenli erteler. Ancak her alanı kapsıyor, aylardır sürüyor ve günlük hayatı bozuyorsa dikkat eksikliği, depresyon veya kaygı bozukluğuyla ilişkili olabilir; bu durumda bir uzmana danışmak gerekir."),
  ],
  sources=[
    "Steel, P. (2007). The nature of procrastination: A meta-analytic and theoretical review of quintessential self-regulatory failure. <em>Psychological Bulletin</em>, 133(1).",
    "Sirois, F. &amp; Pychyl, T. (2013). Procrastination and the priority of short-term mood regulation: Consequences for future self. <em>Social and Personality Psychology Compass</em>, 7(2).",
    "Wohl, M. J. A., Pychyl, T. A. &amp; Bennett, S. H. (2010). I forgive myself, now I can study: How self-forgiveness for procrastinating can reduce future procrastination. <em>Personality and Individual Differences</em>, 48(7).",
    "Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans. <em>American Psychologist</em>, 54(7).",
    "Allen, D. (2001). <em>Getting Things Done</em>. Viking.",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Odaklanmak için en iyi sesler
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="odaklanmak-icin-en-iyi-sesler", lang="tr", pair="best-background-sounds-for-studying",
  section="Rehber", date=D, date_human=DH, rfc822=RFC, read=6, words=1150,
  related=["ogrenciler-icin-en-iyi-odaklanma-araclari", "pomodoro-teknigi-nedir", "evden-calisirken-odaklanma"],
  title="Odaklanmak İçin En İyi Sesler: Yağmur, Kafe, Beyaz Gürültü ve Müzik Karşılaştırması",
  short="Odaklanmak için en iyi sesler",
  h1="Odaklanmak için <span class=\"accent\">en iyi sesler</span>",
  lead="Sessizlik mi, yağmur mu, lo-fi mi? Araştırmaların bulduğu şaşırtıcı biçimde net: iş türüne ve sesin türüne bağlı. Hangi ses hangi işte çalışıyor, hangisi zarar veriyor.",
  desc="Ders çalışırken ve çalışırken odaklanmak için en iyi sesler: yağmur, kafe ambiyansı, beyaz/pembe/kahverengi gürültü, sözsüz müzik ve lo-fi karşılaştırması. Araştırmalara göre hangi ses hangi iş için uygun.",
  keywords="odaklanma sesleri, ders çalışırken müzik, beyaz gürültü, kahverengi gürültü, yağmur sesi çalışma, kafe sesi, lo-fi, odak müziği, sözsüz müzik",
  tldr="""<p><strong>Kısa cevap:</strong> Okuma ve yazma gibi dil işlerinde <strong>sözlü müzik zarar verir</strong>; sözsüz ve tekdüze sesler (yağmur, kahverengi gürültü, düşük sesli kafe uğultusu) nötr ya da faydalı. Tekrar ve soru çözme gibi mekanik işlerde sevdiğin müzik motivasyonu artırabilir. Genel kural: <strong>ses değişmiyorsa arka planda kalır, değişiyorsa dikkati çeker.</strong></p>""",
  body="""
<h2 id="neden">Ses neden işe yarıyor (ya da yaramıyor)?</h2>
<p>Dikkat, çevredeki değişimlere tepki verir. Sessiz bir odada kapının gıcırtısı, komşunun sesi ya da uzaktaki bir korna her seferinde dikkati koparır. Sabit bir arka plan sesi bu değişimleri örter; buna <strong>maskeleme</strong> denir. Yağmurun işe yaramasının nedeni büyülü bir frekans değil, öngörülebilir olması.</p>
<p>Öte yandan ses bir bilgi taşıyorsa, örneğin şarkı sözü ya da anlaşılır konuşma, beynin dil işleyen bölgeleri onu ister istemez işler. Bu yüzden aynı ses bir işte yardımcı, başka bir işte engel olabilir.</p>

<h2 id="tablo">Ses türleri ve hangi işe uyduğu</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Ses</th><th>Okuma / yazma</th><th>Soru çözme / tekrar</th><th>Yaratıcı iş</th><th>Not</th></tr></thead>
  <tbody>
    <tr><td>Tam sessizlik</td><td>İyi (ortam sessizse)</td><td>İyi</td><td>Orta</td><td>Gürültülü evde en kötü seçenek olabilir</td></tr>
    <tr><td>Yağmur / doğa</td><td>Çok iyi</td><td>İyi</td><td>İyi</td><td>Tekdüze, bilgi taşımaz; en güvenli seçim</td></tr>
    <tr><td>Kafe uğultusu</td><td>İyi (konuşma anlaşılmıyorsa)</td><td>İyi</td><td>Çok iyi</td><td>Orta düzey gürültü yaratıcılığı artırabilir</td></tr>
    <tr><td>Beyaz gürültü</td><td>İyi</td><td>İyi</td><td>Orta</td><td>Tiz; bazı kişilere rahatsız gelir</td></tr>
    <tr><td>Pembe / kahverengi gürültü</td><td>Çok iyi</td><td>İyi</td><td>Orta</td><td>Daha bas, uzun süre dinlemeye uygun</td></tr>
    <tr><td>Sözsüz müzik / lo-fi</td><td>Orta</td><td>İyi</td><td>İyi</td><td>Tempo ve dinamik değişimi az olan parçalar</td></tr>
    <tr><td>Sözlü müzik</td><td>Kötü</td><td>Orta</td><td>Orta</td><td>Okuduğunu anlamayı ölçülebilir biçimde düşürür</td></tr>
    <tr><td>Podcast / video</td><td>Çok kötü</td><td>Kötü</td><td>Kötü</td><td>İkisi de dil işler; birinden biri kaybeder</td></tr>
  </tbody>
</table>
</div>

<h2 id="arastirma">Araştırmalar ne diyor?</h2>
<ul>
  <li><strong>Sözlü müzik ve okuma:</strong> Perham ve Currie'nin 2014 çalışmasında sevilen sözlü müzik dinleyen katılımcılar okuduğunu anlama testinde sessizlik ve sözsüz müziğe göre belirgin düşük puan aldı. Şarkıyı sevmek durumu iyileştirmedi.</li>
  <li><strong>Orta düzey gürültü ve yaratıcılık:</strong> Mehta, Zhu ve Cheema'nın 2012 çalışması yaklaşık 70 desibellik ambiyans gürültüsünün (kalabalık kafe düzeyi) yaratıcı problem çözmeyi sessizliğe göre artırdığını, 85 desibelin ise düşürdüğünü buldu. Kafe sesi efsanesinin dayanağı bu.</li>
  <li><strong>Beyaz gürültü ve dikkat:</strong> Söderlund ve arkadaşlarının 2007 çalışmasında beyaz gürültü, dikkat sorunu olan çocukların bellek performansını artırırken dikkat sorunu olmayanlarda hafif düşürdü. Sesin faydası kişiye göre değişiyor.</li>
  <li><strong>Maskeleme:</strong> Açık ofis araştırmaları, anlaşılır konuşmanın en bozucu ses olduğunu tutarlı biçimde gösteriyor. Sabit arka plan sesi bu konuşmaları örttüğünde performans toparlıyor.</li>
</ul>

<h2 id="renkler">Beyaz, pembe, kahverengi: fark ne?</h2>
<p>Üçü de rastgele gürültü; fark, enerjinin frekanslara nasıl dağıldığında. <strong>Beyaz</strong> gürültü tüm frekanslarda eşit güçte, kulağa tiz ve "radyo cızırtısı" gibi gelir. <strong>Pembe</strong> gürültü tizleri kısar, sağanak yağmura benzer. <strong>Kahverengi</strong> gürültü daha da bas, uzaktan gelen şelale ya da uçak kabini sesi gibidir. Uzun seanslar için çoğu insan pembe ya da kahverengiyi daha az yorucu bulur; deneyip karar vermek en doğrusu.</p>

<h2 id="nasil">Sesi doğru kullanmanın 5 kuralı</h2>
<ol>
  <li><strong>Sesi seansla başlat, molayla bitir.</strong> Ses zamanla "çalışma zamanı" sinyaline dönüşür; Pavlov burada senin lehine çalışır.</li>
  <li><strong>Ses düzeyini düşük tut.</strong> Amaç ortamı örtmek, ortamı bastırmak değil. Konuşma sesinin altında kalsın.</li>
  <li><strong>Çalma listesi kurcalama.</strong> Her parça seçimi bir karar, her karar dikkat harcar. Tek uzun ses ya da karıştırılmış bir ambiyans seç.</li>
  <li><strong>İşe göre değiştir.</strong> Okurken yağmur, soru çözerken lo-fi, beyin fırtınasında kafe.</li>
  <li><strong>Kulaklık her zaman gerekmez.</strong> Hoparlörden düşük sesli yağmur, kulak yorgunluğu yapmadan aynı maskelemeyi sağlar.</li>
</ol>

<h2 id="pomi">Pomi'de odak sesleri</h2>
<p>Pomi'de yağmur, kafe, orman gibi sesler var ve her birinin seviyesini ayrı ayrı ayarlayıp karıştırabilirsin: hafif yağmur üstüne uzak kafe uğultusu gibi. Sesler sayaçla birlikte çalışır, seans bitince durur; ayrı bir uygulama açıp çalma listesi aramana gerek kalmaz. Ses için başka araçlara bakıyorsan <a href="ogrenciler-icin-en-iyi-odaklanma-araclari.html">odaklanma araçları rehberinde</a> alternatifler var.</p>
""",
  faq=[
    ("Ders çalışırken müzik dinlemek zararlı mı?", "Sözlü müzik, okuma ve yazma gibi dil gerektiren işlerde anlamayı ölçülebilir biçimde düşürür. Sözsüz ve tekdüze müzik ya da doğa sesleri çoğu kişi için nötr veya faydalıdır. Soru çözme gibi mekanik işlerde sevdiğin müzik motivasyonu artırabilir."),
    ("Odaklanmak için en iyi ses hangisi?", "Tek bir cevap yok, ama en güvenli seçenekler tekdüze ve bilgi taşımayan seslerdir: yağmur, kahverengi gürültü, anlaşılmayan kafe uğultusu. Bu sesler ortamdaki ani değişimleri maskeler ve dikkatin kopmasını azaltır."),
    ("Beyaz gürültü ile kahverengi gürültü arasındaki fark nedir?", "İkisi de rastgele gürültüdür; beyaz gürültü tüm frekanslarda eşit güçtedir ve tiz duyulur, kahverengi gürültü bas frekanslarda yoğunlaşır ve şelale ya da uçak kabini gibi duyulur. Uzun süre dinlemek için çoğu kişi kahverengi veya pembe gürültüyü daha rahat bulur."),
    ("Kafe sesi neden odaklanmaya yardımcı oluyor?", "Orta düzeyde (yaklaşık 70 desibel) sabit bir uğultu hem ortamdaki ani sesleri maskeler hem de araştırmalara göre yaratıcı düşünmeyi hafifçe artırır. Konuşmalar anlaşılır hâle gelirse etki tersine döner."),
    ("Lo-fi müzik çalışırken iyi mi?", "Genellikle evet: sözsüz, tekrarlı ve dinamik değişimi az olduğu için arka planda kalır. Okuma ağırlıklı işlerde yine de yağmur veya gürültü gibi tamamen bilgisiz sesler daha güvenlidir."),
  ],
  sources=[
    "Perham, N. &amp; Currie, H. (2014). Does listening to preferred music improve reading comprehension performance? <em>Applied Cognitive Psychology</em>, 28(2).",
    "Mehta, R., Zhu, R. &amp; Cheema, A. (2012). Is noise always bad? Exploring the effects of ambient noise on creative cognition. <em>Journal of Consumer Research</em>, 39(4).",
    "Söderlund, G., Sikström, S. &amp; Smart, A. (2007). Listen to the noise: Noise is beneficial for cognitive performance in ADHD. <em>Journal of Child Psychology and Psychiatry</em>, 48(8).",
    "Haapakangas, A., Hongisto, V. et al. (2014). Effects of five speech masking sounds on performance and acoustic satisfaction. <em>Acta Acustica united with Acustica</em>, 100(2).",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Evden çalışırken odaklanma
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="evden-calisirken-odaklanma", lang="tr",
  section="Rehber", date=D, date_human=DH, rfc822=RFC, read=6, words=1150,
  related=["pomodoro-mu-flowtime-mi-52-17-odak-teknikleri", "gunde-kac-pomodoro-yapmali", "odaklanmak-icin-en-iyi-sesler"],
  title="Evden Çalışırken Odaklanmak: Uzaktan Çalışanlar İçin Pomodoro Düzeni",
  short="Evden çalışırken odaklanma",
  h1="Evden çalışırken <span class=\"accent\">odaklanmak</span>",
  lead="Ofiste sınırları bina çizer; evde senin çizmen gerekir. Uzaktan çalışanlar için gün düzeni, kesintiyle başa çıkma ve iş-ev sınırını korumanın somut yolları.",
  desc="Evden çalışırken nasıl odaklanılır? Uzaktan çalışanlar için Pomodoro tabanlı gün planı, kesinti yönetimi, bildirim ayarları, iş-ev sınırı ve yalnızlıkla başa çıkma önerileri.",
  keywords="evden çalışırken odaklanma, uzaktan çalışma verimlilik, home office odaklanma, remote çalışma pomodoro, evden çalışma düzeni, dikkat dağınıklığı evde çalışma",
  tldr="""<p><strong>Kısa cevap:</strong> Evde odaklanmanın üç ayağı var: <strong>zaman sınırı</strong> (Pomodoro ya da 52/17 ile bloklar), <strong>mekân sınırı</strong> (yalnızca iş için kullanılan bir köşe) ve <strong>kesinti sınırı</strong> (bildirimler kapalı, ev halkıyla anlaşılmış saatler). Güne sabit bir başlangıç ritüeli ve sabit bir bitiş saatiyle çerçeve çiz; çerçeve olmayınca iş güne yayılır ve hiçbir saat tam iş olmaz.</p>""",
  body="""
<h2 id="sorun">Evde asıl sorun ne?</h2>
<p>Uzaktan çalışanların şikâyeti genellikle "odaklanamıyorum" diye başlar ama biraz kazınca üç farklı sorun çıkar: <strong>başlayamamak</strong> (sabah bir türlü masaya oturamamak), <strong>bölünmek</strong> (mesaj, kapı, çamaşır makinesi) ve <strong>bitirememek</strong> (akşam 9'da hâlâ e-posta). Çözümler farklı olduğu için hangisinden çektiğini bilmek gerekir.</p>
<p>Gloria Mark'ın bilgi işçileri üzerine yaptığı çalışmalar, bir kesintiden sonra asıl işe dönmenin ortalama <strong>23 dakika</strong> sürdüğünü gösteriyor. Evde kesinti kaynakları ofisten farklı ama daha az değil; üstelik hiçbiri "toplantıdayım" tabelasını görmüyor.</p>

<h2 id="gun">Örnek gün düzeni</h2>
<p>Aşağıdaki plan 8 saatlik bir gün için; saatler senin ritmine göre kayabilir. Önemli olan blokların varlığı ve sırası.</p>
<div class="table-wrap">
<table>
  <thead><tr><th>Saat</th><th>Blok</th><th>Ne</th></tr></thead>
  <tbody>
    <tr><td>08:30</td><td>Başlangıç ritüeli (15 dk)</td><td>Kahve, günün 3 işi kâğıda, telefon başka odaya</td></tr>
    <tr><td>08:45-10:45</td><td>Derin iş 1 (4 pomodoro)</td><td>Günün en zor işi. Mesajlaşma kapalı</td></tr>
    <tr><td>10:45-11:15</td><td>Uzun mola + iletişim</td><td>Dışarı çık, dönünce mesaj ve e-posta</td></tr>
    <tr><td>11:15-12:45</td><td>Derin iş 2 (3 pomodoro)</td><td>İkinci öncelikli iş</td></tr>
    <tr><td>12:45-13:45</td><td>Öğle</td><td>Masadan uzakta, ekransız</td></tr>
    <tr><td>13:45-15:30</td><td>Toplantı ve sığ iş</td><td>Enerjinin düştüğü saat; işbirliği gerektiren işler buraya</td></tr>
    <tr><td>15:30-17:00</td><td>Derin iş 3 (3 pomodoro)</td><td>Bitirme, düzenleme, yarına hazırlık</td></tr>
    <tr><td>17:00</td><td>Kapanış ritüeli (10 dk)</td><td>Yarının 3 işi, bilgisayar kapalı, masa toplu</td></tr>
  </tbody>
</table>
</div>
<p>Toplam 10 pomodoro, yani 4 saatten biraz fazla derin iş. Bu, ofis günlerinin çoğundan fazla; <a href="gunde-kac-pomodoro-yapmali.html">günde kaç pomodoro yazısında</a> nedenini anlattık. 25 dakika kısa geliyorsa aynı iskeleti <a href="pomodoro-mu-flowtime-mi-52-17-odak-teknikleri.html">52/17 veya 90/20</a> ile de kurabilirsin.</p>

<h2 id="baslamak">Başlamak için: ritüel ve mekân</h2>
<ul>
  <li><strong>Sabit başlangıç.</strong> Her gün aynı saatte aynı üç hareket: kahve, kâğıda üç iş, sayaç. Ritüel, karar vermeyi ortadan kaldırır; karar vermemek başlamanın en kolay hâli.</li>
  <li><strong>Yalnızca iş için bir köşe.</strong> Ayrı oda şart değil; masanın belirli bir tarafı, belirli bir sandalye. Orada başka şey yapma. Birkaç haftada beden "buraya oturunca çalışılır" bağlantısını kurar.</li>
  <li><strong>Giyin.</strong> Pijama değil, dışarı çıkabileceğin bir şey. Küçük ama etkili bir sınır.</li>
</ul>

<h2 id="kesinti">Kesintiyle başa çıkmak</h2>
<ul>
  <li><strong>Bildirimleri seansta kapat.</strong> Telefon başka odada, bilgisayarda odak modu. Mesajlaşma uygulamasını 25 dakika kapatmak kimseyi öldürmez; acil olan arar.</li>
  <li><strong>İletişim pencereleri.</strong> Mesaj ve e-postaya günde 3 sabit saatte bak (örnekte 10:45, 13:45, 17:00). Ekibe bunu söyle; beklenti netleşince kaygı azalır.</li>
  <li><strong>Ev halkıyla anlaşma.</strong> "Kapı kapalıysa toplantıdayım" gibi tek ve basit bir işaret. Çocuklu evlerde sayaç görünür bir yerde dursun; "sayaç bitince geliyorum" çocuklar için anlaşılır bir söz.</li>
  <li><strong>Kesinti defteri.</strong> Seansta aklına gelen "çamaşırı asmalıyım" gibi işleri kâğıda yaz, molada yap. Cirillo'nun orijinal yöntemindeki bu kural, evde ofistekinden daha değerli.</li>
</ul>

<h2 id="bitirmek">Bitirmek için: kapanış saati</h2>
<p>Evde en çok ihmal edilen sınır bu. Bitiş saati yoksa iş akşama sızar, akşam dinlendirmez, ertesi sabah başlamak zorlaşır ve döngü kapanır. Sabit bir kapanış ritüeli kur: yarının üç işini yaz, açık sekmeleri kapat, bilgisayarı kapat, masayı topla. Cal Newport bunu "kapanış cümlesi" ile bitirmeyi önerir; sesli söylemek tuhaf ama işe yarıyor.</p>

<h2 id="yalnizlik">Yalnızlık ve motivasyon</h2>
<p>Ofisin görünmeyen faydası, çevrende çalışan insanların varlığı. Evde bunu iki yolla telafi edebilirsin: haftada bir-iki gün kütüphane ya da ortak çalışma alanı, ya da çevrimiçi bir odak odası. Pomi'de ekip arkadaşlarınla ya da benzer saatlerde çalışan tanıdıklarınla oda açıp herkesin kendi sayacıyla girmesi, sessiz bir ofis hissi verir; kamera ya da mikrofon gerekmez. Arka plan sesi için de ayrı uygulamaya gerek kalmaz; <a href="odaklanmak-icin-en-iyi-sesler.html">hangi sesin hangi işe uyduğunu</a> ayrıca yazdık.</p>

<h2 id="kontrol">Haftalık kontrol listesi</h2>
<ul>
  <li>Bu hafta kaç derin iş bloğu yaptım? (Hedef: günde 2-3)</li>
  <li>Bitiş saatine kaç gün uydum?</li>
  <li>En sık kesinti kaynağı neydi, önümüzdeki hafta onun için tek bir önlem ne?</li>
</ul>
""",
  faq=[
    ("Evden çalışırken neden odaklanamıyorum?", "Genellikle üç farklı sorundan biri: başlayamamak (ritüel ve sabit mekân eksikliği), bölünmek (bildirimler ve ev halkı) ya da bitirememek (kapanış saati yokluğu). Hangisinden çektiğini belirleyip ona özel önlem almak, genel \"daha disiplinli olma\" çabasından daha etkilidir."),
    ("Evden çalışırken Pomodoro işe yarar mı?", "Evet, özellikle başlamak ve kesintileri yönetmek için. 25 dakikalık bloklar başlama direncini düşürür; seans sırasında aklına gelen ev işlerini not edip molada yapmak bölünmeyi azaltır. 25 dakika kısa geliyorsa 52/17 de aynı iskelette çalışır."),
    ("Evde ayrı çalışma odam yoksa ne yapmalıyım?", "Ayrı oda şart değil. Yalnızca iş için kullanılan bir masa köşesi ya da sandalye yeterlidir; orada başka bir şey yapmamak birkaç haftada mekân-iş bağlantısını kurar. Gün sonunda iş malzemelerini kaldırmak da sınırı güçlendirir."),
    ("Uzaktan çalışırken günde kaç saat derin iş yapabilirim?", "Çoğu kişi için 4-5 saat net odak üst sınırdır; bu 8-10 pomodoroya denk gelir. Kalan mesai toplantı, iletişim ve hafif işlere gider. Ofiste bu sayı genellikle daha düşüktür."),
    ("Evde çalışırken yalnızlık hissiyle nasıl başa çıkarım?", "Haftada bir-iki gün kütüphane ya da ortak çalışma alanı, kalan günlerde çevrimiçi odak odaları yardımcı olur. Pomi'de tanıdıklarınla oda açıp herkesin kendi sayacıyla çalışması, kamera ve mikrofon olmadan sessiz bir ofis hissi verir."),
  ],
  sources=[
    "Mark, G., Gudith, D. &amp; Klocke, U. (2008). The cost of interrupted work: More speed and stress. <em>CHI 2008</em>.",
    "Newport, C. (2016). <em>Deep Work</em>. Grand Central Publishing.",
    "Cirillo, F. (2018). <em>The Pomodoro Technique</em>. Currency.",
  ],
))
