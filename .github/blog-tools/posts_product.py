# -*- coding: utf-8 -*-
"""Türkçe yazılar: Pomi'nin kendisi ve oyunlaştırma."""

IOS = "https://apps.apple.com/tr/app/id6784132034"
ANDROID = "https://play.google.com/store/apps/details?id=com.yakupselimucar.pomi"
SITE = "https://yakupselimucar.github.io/pomi-legal/"
D = "2026-09-13"
DH = "13 Eylül 2026"
RFC = "Sun, 13 Sep 2026 11:00:00 +0300"

POSTS = []

# ─────────────────────────────────────────────────────────────────
# Pomi nasıl kullanılır?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="pomi-nasil-kullanilir", lang="tr", pair="how-to-use-pomi",
  section="Pomi", date=D, date_human=DH, rfc822=RFC, read=7, words=1300,
  related=["pomi-fetih-haritasi-nasil-calisir", "study-with-me-birlikte-ders-calisma", "pomodoro-teknigi-nedir"],
  title="Pomi Nasıl Kullanılır? Bahçe, Odalar, Fetih Haritası ve Lig İçin Başlangıç Rehberi",
  short="Pomi nasıl kullanılır",
  h1="Pomi <span class=\"accent\">nasıl kullanılır</span>? Başlangıç rehberi",
  lead="İlk seansından ilk bitkine, ilk odandan şehrin için kazandığın ilk bölgeye. Pomi'nin her parçası ne işe yarar, nasıl kurulur, hangi ayarlar değişir.",
  desc="Pomi kullanım rehberi: ilk Pomodoro seansını başlatma, görev ekleme, piksel bahçe ve bitki koleksiyonu, davet koduyla oda kurma, fetih haritası, haftalık lig, odak sesleri, süre ayarları ve Pomi Pro.",
  keywords="pomi nasıl kullanılır, pomi uygulaması, pomi oda kurma, pomi davet kodu, pomi fetih haritası, pomi bahçe, pomi pro, pomodoro uygulaması rehber",
  tldr="""<p><strong>Kısa cevap:</strong> Pomi'de akış üç adım: <strong>görev seç, sayacı başlat, 25 dakika odaklan.</strong> Seans bitince bahçene bir bitki eklenir ve odak dakikaların şehrinin fetih haritası puanına yazılır. Arkadaşlarınla çalışmak için bir oda aç, 6 haneli kodu paylaş; odada herkes kendi sayacıyla çalışır. Sayaç ücretsiz, reklamsız ve çevrimdışı çalışır.</p>""",
  howto=dict(name="Pomi ile ilk odak seansını tamamlama", steps=[
    ("Görev ekle", "Görevler sekmesinden bugün yapacağın işi yaz. Her seans bir göreve bağlanır."),
    ("Süreyi ayarla", "Varsayılan 25 dakika çalışma, 5 dakika mola. Ayarlardan 15/3, 50/10 gibi döngülere değiştirebilirsin."),
    ("Sayacı başlat ve telefonu uzaklaştır", "Sayaç ekran kapalıyken ve uygulama arka plandayken saymaya devam eder."),
    ("İstersen ses aç ya da odaya katıl", "Yağmur, kafe, orman seslerini karıştır; arkadaşlarının odasına davet koduyla gir."),
    ("Seansı tamamla", "Bahçene yeni bir bitki eklenir, odak dakikaların şehrine puan olarak yazılır ve haftalık ligde ilerlersin."),
  ]),
  body="""
<h2 id="ilk-seans">İlk seans: üç adım</h2>
<ol>
  <li><strong>Görev ekle.</strong> Görevler sekmesine bugün ne yapacağını yaz: "Türev soru bankası 40-48" gibi somut bir şey. Her seans bir göreve bağlanır; gün sonunda hangi işe kaç seans gittiğini buradan görürsün.</li>
  <li><strong>Sayacı başlat.</strong> Varsayılan döngü 25 dakika çalışma, 5 dakika mola. Retro piksel sayaç çalışırken tek işe odaklan. Telefonu ters çevirip uzaklaştırabilirsin; sayaç ekran kapalıyken ve uygulama arka plandayken saymaya devam eder.</li>
  <li><strong>Seansı tamamla.</strong> Süre dolunca bahçene yeni bir bitki eklenir, odak dakikaların şehrinin puanına yazılır. Mola sayacı otomatik başlar.</li>
</ol>
<p class="note mint">Seansı yarıda bırakırsan bitki eklenmez. Ceza yok, kurumuş ağaç yok; sadece o seans sayılmaz. Tekniğin kendisi hakkında bilgi için <a href="pomodoro-teknigi-nedir.html">Pomodoro rehberine</a> bak.</p>

<h2 id="bahce">Piksel bahçe ve koleksiyon</h2>
<p>Bahçe, odak geçmişinin görsel kaydı. Her tamamlanan seans bir bitki; bitkilerin türleri, büyüme aşamaları ve nadirlik dereceleri var. Odaklandıkça yeni türler açılır ve koleksiyon ekranında hangilerini bulduğunu, hangilerinin eksik olduğunu görürsün. Bahçeye baktığında geçen ayın çalışmasını tek bakışta okuyabilmen, sayının kendisinden daha motive edici oluyor.</p>

<h2 id="odalar">Odalar: arkadaşlarınla, herkes kendi sayacıyla</h2>
<p>Odalar sekmesinden yeni bir oda oluşturduğunda uygulama <strong>6 haneli bir davet kodu</strong> üretir. Kodu arkadaşlarına gönder; onlar da Odalar sekmesinden kodu girip katılır. Odada herkesin ismini ve sayaç durumunu görürsün.</p>
<p>Önemli tasarım kararı: <strong>ortak sayaç yok.</strong> Herkes kendi seansını kendi istediği anda başlatır ve bitirir. Sen 25 dakikalık seansın ortasındayken arkadaşın mola verebilir; senin seansın etkilenmez. Kamera, mikrofon ve sohbet de yok; oda "birlikte sessizce çalışıyoruz" hissini vermek için var. Bunun neden işe yaradığını <a href="study-with-me-birlikte-ders-calisma.html">study with me yazısında</a> anlattık.</p>
<p>İyi bir oda düzeni için: sabit saat belirleyin ("her akşam 20:00"), herkes görevini önceden yazsın, konuşma molaya kalsın.</p>

<h2 id="fetih">Fetih haritası</h2>
<p>Pomi'yi diğer sayaçlardan ayıran özellik. Profilinde şehrini seçersin; tamamladığın her seansın dakikaları şehrinin puanına eklenir. Puan biriktikçe haritadaki bölgeler şehrinin rengine döner. Bölgeler gün içinde el değiştirir, bir bölgeyi bugün alırsın, yarın rakip şehir geri alır. Sezonlar <strong>7 gün</strong> sürer; sezon sonunda en çok bölgeyi tutan şehir kazanır. Türkiye'nin 81 şehri yarışır. Tek başına çalışırken bile bir takımın parçası olduğunu hissettiren mekanizma bu; ayrıntılar <a href="pomi-fetih-haritasi-nasil-calisir.html">fetih haritası yazısında</a>.</p>

<h2 id="lig">Haftalık lig</h2>
<p>Lig, bireysel sıralama: haftalık odak sürene göre diğer kullanıcılarla aynı ligde yarışırsın, hafta sonunda sıralamaya göre yükselir ya da düşersin. Şehrinin genel sıralamadaki yerini de görürsün. Ligin amacı seni bugünle değil haftanla değerlendirmek; kötü bir gün haftayı bozmaz.</p>

<h2 id="sesler">Odak sesleri</h2>
<p>Yağmur, kafe, orman gibi sesleri seans sırasında açabilir ve her birinin seviyesini ayrı ayrı ayarlayıp karıştırabilirsin: hafif yağmur üstüne uzak kafe uğultusu gibi. Sesler sayaçla birlikte durur. Hangi sesin hangi işe uyduğunu <a href="odaklanmak-icin-en-iyi-sesler.html">sesler yazısında</a> açıkladık.</p>

<h2 id="ayarlar">Ayarlar: süreler ve tema</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Ayar</th><th>Ne yapar</th><th>Öneri</th></tr></thead>
  <tbody>
    <tr><td>Çalışma süresi</td><td>Seans uzunluğu</td><td>Başlangıç 25; soru çözümünde 40-50</td></tr>
    <tr><td>Kısa mola</td><td>Seanslar arası mola</td><td>5; uzun seanslarda 8-10</td></tr>
    <tr><td>Uzun mola</td><td>Dört seans sonrası mola</td><td>15-30</td></tr>
    <tr><td>Karanlık mod</td><td>Gece kullanımı için koyu tema</td><td>Akşam seanslarında</td></tr>
    <tr><td>Şehir</td><td>Fetih haritasında puanların gideceği şehir</td><td>Bir kez seç, arkadaşlarınla aynı şehirde ol</td></tr>
  </tbody>
</table>
</div>

<h2 id="istatistik">İstatistikler</h2>
<p>Haftalık odak saati grafiği, tamamlanan seans sayısı ve göreve göre dağılım. "Bu hafta zayıf derse gerçekten zaman ayırdım mı?" sorusunun cevabı tahmin değil, sayı olur. Gerçekçi haftalık hedefler için <a href="gunde-kac-pomodoro-yapmali.html">günde kaç pomodoro yazısına</a> bak.</p>

<h2 id="pro">Ücretsiz ve Pomi Pro</h2>
<p>Sayaç, bahçe, görevler, odalar ve fetih haritası ücretsiz sürümde var ve <strong>reklam yok</strong>. Pomi Pro isteğe bağlı bir abonelik; ek özellikler ve kişiselleştirme sunar. Aboneliği mağaza hesabından yönetir, istediğin zaman iptal edersin. Satın alma geri yükleme ve hesap silme gibi konular <a href="../support.html">destek sayfasında</a>.</p>

<h2 id="cevrimdisi">Çevrimdışı ve arka plan</h2>
<p>Sayaç ve bahçe internet olmadan çalışır; odalar, fetih haritası ve lig için bağlantı gerekir. Çevrimdışı tamamlanan seanslar bağlantı gelince şehrine yazılır. Sayaç uygulama kapalıyken de saymaya devam eder; bildirim izni verirsen seans ve mola bitişini haber alırsın.</p>

<h2 id="ipuclari">İlk hafta için 5 ipucu</h2>
<ol>
  <li>İlk üç gün sadece sayaç ve görev; odaya ve haritaya sonra bak.</li>
  <li>Günde 3-4 seans hedefle, sayıyı haftada bir artır.</li>
  <li>Şehrini seç ve aynı şehirden bir arkadaşını davet et; harita o zaman anlam kazanıyor.</li>
  <li>Akşam sabit saatte bir oda aç; kodu bir kez paylaş, oda kalıcı.</li>
  <li>Pazar akşamı istatistiğe bak, gelecek haftanın tek hedefini yaz.</li>
</ol>
""",
  faq=[
    ("Pomi ücretsiz mi?", "Evet. Sayaç, bahçe, görevler, odalar ve fetih haritası ücretsizdir ve reklam yoktur. Pomi Pro isteğe bağlı bir aboneliktir; ek özellikler sunar ve istediğin zaman iptal edilebilir."),
    ("Pomi'de oda nasıl kurulur?", "Odalar sekmesinden yeni oda oluştur; uygulama 6 haneli bir davet kodu verir. Kodu arkadaşlarına gönder, onlar da Odalar sekmesinden kodu girerek katılır. Odada herkes kendi sayacıyla çalışır."),
    ("Pomi çevrimdışı çalışır mı?", "Sayaç ve bahçe internet olmadan çalışır. Odalar, fetih haritası ve lig için bağlantı gerekir; çevrimdışı tamamlanan seanslar bağlantı gelince şehrine yazılır."),
    ("Seansı yarıda bırakırsam ne olur?", "Bitki eklenmez ve o seans sayılmaz. Ceza ya da kuruyan ağaç yoktur; bir sonraki seansa temiz başlarsın."),
    ("Pomi'de çalışma süresi değiştirilebilir mi?", "Evet. Ayarlardan çalışma, kısa mola ve uzun mola sürelerini değiştirebilirsin; 15/3, 25/5, 50/10 gibi döngüler kurulabilir. Seans hangi uzunlukta olursa olsun tamamlandığında bahçeye bitki eklenir."),
    ("Pomi hangi cihazlarda var?", "iPhone, iPad (iOS 15 ve üzeri) ve Android. Web ve masaüstü sürümü şu an yok."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# Fetih haritası nasıl çalışır?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="pomi-fetih-haritasi-nasil-calisir", lang="tr",
  section="Pomi", date=D, date_human=DH, rfc822=RFC, read=5, words=900,
  related=["pomi-nasil-kullanilir", "odak-uygulamalarinda-oyunlastirma-ise-yarar-mi", "study-with-me-birlikte-ders-calisma"],
  title="Pomi Fetih Haritası Nasıl Çalışır? 81 Şehir, 7 Günlük Sezonlar ve Bölge Savaşları",
  short="Fetih haritası nasıl çalışır",
  h1="Fetih haritası <span class=\"accent\">nasıl çalışır</span>?",
  lead="Odak dakikaların şehrine puan yazıyor, puanlar bölgeleri boyuyor, bölgeler el değiştiriyor. Pomi'nin en çok soru gelen özelliğinin kuralları ve arkasındaki düşünce.",
  desc="Pomi fetih haritası rehberi: odak dakikalarının şehir puanına dönüşmesi, bölgelerin el değiştirmesi, 7 günlük sezonlar, 81 şehrin yarışı, şehir seçimi ve arkadaşlarla birlikte bölge kazanma taktikleri.",
  keywords="pomi fetih haritası, fetih haritası nasıl çalışır, şehir yarışı pomodoro, bölge savaşı odak uygulaması, pomi sezon, pomi şehir seçimi",
  tldr="""<p><strong>Kısa cevap:</strong> Tamamladığın her seansın dakikaları <strong>şehrinin puanına</strong> eklenir. Puan biriktikçe haritadaki <strong>bölgeler şehrinin rengine</strong> döner; rakip şehirler daha çok odaklanırsa bölgeyi geri alır. Sezon <strong>7 gün</strong> sürer, sonunda en çok bölgeyi tutan şehir kazanır ve harita sıfırlanır. Türkiye'nin 81 şehri yarışır. Tek seans bile fark yaratır.</p>""",
  body="""
<h2 id="neden">Neden bir harita?</h2>
<p>Bireysel oyunlaştırma (bahçe, seri, rozet) bir noktadan sonra doygunluğa ulaşır: yüzüncü bitki, birincisi kadar heyecan vermez. Takım hedefleri farklı çalışır. "Bugün çalışmazsam şehrim bölge kaybeder" düşüncesi, "bugün çalışmazsam bahçeme bitki eklenmez"den daha güçlü bir itki; çünkü sonuç yalnızca seni değil, aynı rengi taşıyan herkesi etkiliyor. Fetih haritası, tek başına çalışan birine takım hissi vermek için tasarlandı.</p>

<h2 id="kurallar">Kurallar</h2>
<ul>
  <li><strong>Şehir seçimi.</strong> Profilinde bir şehir seçersin; Türkiye'nin 81 ili arasından. Puanların o şehre yazılır.</li>
  <li><strong>Puan.</strong> Tamamlanan her seansın odak dakikaları şehrinin puanına eklenir. Yarıda bırakılan seans puan getirmez.</li>
  <li><strong>Bölgeler.</strong> Harita bölgelere ayrılmıştır. Puan biriktikçe bölgeler şehrinin rengine döner; rakip şehirler daha çok puan toplarsa bölge el değiştirir.</li>
  <li><strong>Canlı.</strong> Bölgeler gün içinde el değiştirir ve haritayı anlık izlersin. Şehrinin sırasını, elindeki bölge sayısını ve o an odaklanan "savunucu" sayısını görürsün.</li>
  <li><strong>Sezon.</strong> Her sezon 7 gün sürer. Sezon sonunda en çok bölgeyi tutan şehir kazanır, sonra yeni sezon temiz haritayla başlar.</li>
</ul>

<h2 id="denge">Büyük şehir her zaman kazanmaz mı?</h2>
<p>En sık gelen soru. Nüfusu yüksek şehirlerin doğal avantajı var, ama yarışta belirleyici olan toplam kullanıcı sayısı değil, <strong>o hafta gerçekten odaklanan kişi sayısı ve dakikası</strong>. Küçük ama düzenli çalışan bir grup, kalabalık ama dağınık bir şehri bölge bazında geçebiliyor. Sezonların 7 gün olmasının nedeni de bu: her Pazartesi herkes sıfırdan başlar, geçmiş birikim kimseyi taşımaz.</p>

<h2 id="taktik">Şehrin için daha çok bölge kazanmanın yolları</h2>
<ol>
  <li><strong>Aynı şehirden arkadaşlarınla oda kur.</strong> Odada herkes kendi sayacıyla çalışır ama puanlar aynı şehre gider. Üç kişilik düzenli bir oda, bir haftada belirgin fark yaratır.</li>
  <li><strong>Düzenlilik, yoğunluktan değerli.</strong> Pazartesi 10 seans, sonra sessizlik yerine her gün 3 seans; bölgeler gün içinde el değiştirdiği için sürekli varlık önemli.</li>
  <li><strong>Sezon sonunu takip et.</strong> Son gün en çok bölgeyi kimin tuttuğu sayılır; haftanın son akşamındaki seanslar sembolik olarak en değerli seanslar.</li>
  <li><strong>Seansı tamamla.</strong> Yarım seans puan getirmez. Emin olmadığın bir zaman diliminde 25 yerine 15 dakikalık seans ayarla, tamamla.</li>
</ol>

<h2 id="motivasyon">Rekabet herkes için mi?</h2>
<p>Hayır ve bu sorun değil. Harita, seni zorlamadan arka planda çalışır: bakmazsan yok gibidir, bakarsan bir takımın parçası olduğunu hatırlatır. Oyunlaştırmanın kimde nasıl işlediğini <a href="odak-uygulamalarinda-oyunlastirma-ise-yarar-mi.html">ayrı bir yazıda</a> tartıştık. Bireysel ilerlemeyi görmek için bahçe ve istatistikler, takım hissi için oda ve harita; hangisi seni çalıştırıyorsa ona bak.</p>

<h2 id="pratik">Sık sorulan pratik konular</h2>
<ul>
  <li><strong>Şehir değiştirebilir miyim?</strong> Evet, ayarlardan. Puanların yeni şehre bir sonraki seanstan itibaren yazılır.</li>
  <li><strong>Yurt dışındayım.</strong> Bağlı hissettiğin şehri seç; konum kontrolü yok.</li>
  <li><strong>Çevrimdışı seanslar sayılıyor mu?</strong> Evet, bağlantı gelince şehrine yazılır.</li>
  <li><strong>Kişisel veri paylaşılıyor mu?</strong> Haritada bireysel bilgi görünmez; yalnızca şehir toplamları ve o an odaklanan kişi sayısı gösterilir. Ayrıntı için <a href="../privacy.html">gizlilik politikası</a>.</li>
</ul>
<p>Uygulamanın geri kalanı için <a href="pomi-nasil-kullanilir.html">başlangıç rehberine</a> bak.</p>
""",
  faq=[
    ("Pomi fetih haritası nedir?", "Odak dakikalarının şehrinin puanına yazıldığı, puan biriktikçe haritadaki bölgelerin şehrinin rengine döndüğü bir takım yarışıdır. Türkiye'nin 81 şehri 7 günlük sezonlarda en çok bölgeyi tutmak için yarışır."),
    ("Fetih haritasında sezon ne kadar sürer?", "7 gün. Sezon sonunda en çok bölgeyi tutan şehir kazanır ve yeni sezon temiz haritayla başlar; geçmiş birikim yeni sezona taşınmaz."),
    ("Yarım bırakılan seans şehrime puan yazar mı?", "Hayır. Yalnızca tamamlanan seansların dakikaları şehir puanına eklenir. Emin olmadığın zamanlarda daha kısa bir seans ayarlayıp tamamlamak daha iyidir."),
    ("Büyük şehirler her zaman kazanır mı?", "Hayır. Belirleyici olan toplam kullanıcı değil, o hafta gerçekten odaklanan kişi ve dakika sayısıdır. Düzenli çalışan küçük bir grup, bölge bazında kalabalık şehirleri geçebilir; sezonların kısa olması da bunu destekler."),
    ("Fetih haritasında şehrimi değiştirebilir miyim?", "Evet, ayarlardan şehir değiştirebilirsin. Puanların bir sonraki seanstan itibaren yeni şehre yazılır. Konum kontrolü yoktur; bağlı hissettiğin şehri seçebilirsin."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# Oyunlaştırma işe yarar mı?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="odak-uygulamalarinda-oyunlastirma-ise-yarar-mi", lang="tr", pair="does-gamification-help-you-focus",
  section="Temel bilgi", date=D, date_human=DH, rfc822=RFC, read=7, words=1250,
  related=["erteleme-aliskanligini-yenmek", "forest-alternatifi-ucretsiz-uygulamalar", "pomi-fetih-haritasi-nasil-calisir"],
  title="Odak Uygulamalarında Oyunlaştırma İşe Yarıyor mu? Ağaçlar, Bahçeler ve Ligler Üzerine Dürüst Bir Bakış",
  short="Oyunlaştırma işe yarıyor mu",
  h1="Odak uygulamalarında oyunlaştırma <span class=\"accent\">işe yarıyor mu</span>?",
  lead="Kuruyan ağaçlar, büyüyen bahçeler, kırılmaması gereken seriler. Araştırma ne diyor, hangi mekanikler kalıcı, hangileri birkaç haftada söner ve bir odak uygulaması geliştiricisi olarak neyi bilerek yapmadık.",
  desc="Odak ve verimlilik uygulamalarında oyunlaştırma işe yarar mı? Araştırma bulguları, ceza ve ödül mekanikleri, seri (streak) tuzağı, öz belirleme kuramı, takım hedefleri ve Pomi'nin tasarım kararları.",
  keywords="oyunlaştırma işe yarar mı, gamification verimlilik, odak uygulaması oyunlaştırma, streak motivasyon, ödül ceza motivasyon, öz belirleme kuramı, forest ağaç kurur, motivasyon uygulama",
  tldr="""<p><strong>Kısa cevap:</strong> Evet ama koşullu. Araştırmalar oyunlaştırmanın <strong>kısa vadede</strong> katılımı artırdığını, <strong>uzun vadede</strong> etkinin mekaniğe ve kişiye bağlı olduğunu gösteriyor. İyi çalışanlar: görünür ilerleme, anlamlı geri bildirim, takım hedefleri. Kötü çalışanlar: ceza korkusu, kırılınca her şeyi sıfırlayan seriler ve işin kendisiyle ilgisiz ödüller. Oyunlaştırma, yapılan işi sevdiremiyorsa yalnızca başlangıcı kolaylaştırır; bu da az şey değil.</p>""",
  body="""
<h2 id="arastirma">Araştırma ne diyor?</h2>
<p>Hamari, Koivisto ve Sarsa'nın 2014'te yaptığı ve alanın en çok atıf alan derlemesi olan çalışma, 24 deneysel araştırmayı taradı. Sonuç: oyunlaştırma çoğunlukla olumlu etki yaratıyor, ama etki <strong>bağlama ve kullanıcıya</strong> güçlü biçimde bağlı ve çoğu çalışma kısa süreli. "Yenilik etkisi" diye bir sorun var: yeni bir mekanik ilk haftalarda çalışır, alışınca etkisi azalır.</p>
<p>Daha derin açıklama, Deci ve Ryan'ın öz belirleme kuramından geliyor. İnsanlar üç şeye ihtiyaç duyar: <strong>yetkinlik</strong> (ilerlediğimi görmek), <strong>özerklik</strong> (kendi seçimim olması) ve <strong>ilişkililik</strong> (başkalarıyla bağ). Bu üçünü besleyen oyunlaştırma içsel motivasyonu destekler; dışarıdan bastıran (ceza, baskı, yapay yarış) uzun vadede onu zayıflatabilir.</p>

<h2 id="mekanikler">Mekanik mekanik: ne çalışıyor, ne çalışmıyor?</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Mekanik</th><th>Örnek</th><th>Kısa vade</th><th>Uzun vade</th><th>Risk</th></tr></thead>
  <tbody>
    <tr><td>Ceza / kayıp</td><td>Uygulamadan çıkınca ağaç kurur</td><td>Güçlü</td><td>Zayıflar</td><td>Kaygı; uygulamayı bırakma</td></tr>
    <tr><td>Biriken koleksiyon</td><td>Her seans bir bitki, bahçe büyür</td><td>Orta</td><td>İyi</td><td>Doygunluk (100. bitki)</td></tr>
    <tr><td>Seri (streak)</td><td>"37 gündür çalışıyorsun"</td><td>Güçlü</td><td>İkiye ayrılır</td><td>Bir gün kaçınca her şeyi bırakma</td></tr>
    <tr><td>Puan ve seviye</td><td>XP, rütbe</td><td>Orta</td><td>Zayıf</td><td>İşle ilgisiz; anlamını yitirir</td></tr>
    <tr><td>Takım hedefi</td><td>Şehrin için bölge kazanma</td><td>Orta</td><td>İyi</td><td>Katkım görünmezse kopma</td></tr>
    <tr><td>Sosyal varlık</td><td>Arkadaşlarla aynı odada çalışma</td><td>İyi</td><td>İyi</td><td>Karşılaştırma baskısı</td></tr>
    <tr><td>Bilgilendirici geri bildirim</td><td>Haftalık odak grafiği</td><td>Zayıf</td><td>İyi</td><td>Yok denecek kadar az</td></tr>
  </tbody>
</table>
</div>

<h3>Ceza neden ilk aylarda çalışıp sonra sönüyor?</h3>
<p>Kayıptan kaçınma güçlü bir dürtü; kuruyan ağaç fikri tam bunu kullanır. Ama ceza, işi yapmanın nedenini "ağaç kurumasın"a indirger. Öz belirleme kuramı bunun içsel motivasyonu <strong>bastırdığını</strong> öngörüyor ve pratikte de görülen şu: kullanıcı ya cezayı önemsemez hâle gelir ya da uygulamayı siler. Ceza, başlamayı kolaylaştıran bir ilk itki olabilir; sürdüren şey olamaz.</p>

<h3>Seri tuzağı</h3>
<p>Seriler, kaçırılan tek günü felakete çevirir. Alışkanlık araştırmalarında bir günü kaçırmanın alışkanlık oluşumuna ölçülebilir zarar vermediği görülüyor (Lally ve arkadaşları, 2010); ama seri mekaniği bunu tam tersi gibi hissettirir ve "nasılsa bozuldu" diyerek bırakmayı kolaylaştırır. Seri kullanılacaksa haftalık olmalı ve bir kaçak gün affedilmeli.</p>

<h3>Takım hedefleri neden dayanıklı?</h3>
<p>İlişkililik ihtiyacını besler ve çabanın anlamını kişiden büyük bir şeye bağlar. "Bugün çalışmazsam şehrim bölge kaybeder" düşüncesi, bireysel puandan daha uzun ömürlü. Koşul: katkının görünür olması. Katkısını göremeyen kullanıcı takımdan kopar.</p>

<h2 id="pomi">Pomi'de neyi neden yaptık, neyi yapmadık</h2>
<p>Bir odak uygulaması geliştirirken bu araştırmaya bakıp şu kararları verdik; katılmayabilirsin ama gerekçe şeffaf olsun:</p>
<ul>
  <li><strong>Ceza yok.</strong> Yarım seansta bitki eklenmez ama hiçbir şey kurumaz, ölmez, sıfırlanmaz. Kaygı üzerine kurulu bir motivasyon istemedik.</li>
  <li><strong>Biriken koleksiyon var.</strong> Bahçe, doygunluğu geciktirmek için tür, aşama ve nadirlik katmanlarıyla tasarlandı; 100. bitki farklı bir tür olabilir.</li>
  <li><strong>Günlük seri yok, haftalık lig var.</strong> Lig haftayla değerlendirir; kötü bir gün haftayı bozmaz.</li>
  <li><strong>Takım hedefi: fetih haritası.</strong> Odak dakikaların şehrine puan yazar, 81 şehir 7 günlük sezonlarda yarışır. Katkı görünür: haritaya baktığında şehrinin rengini ve o an odaklanan kişi sayısını görürsün. Kuralları <a href="pomi-fetih-haritasi-nasil-calisir.html">ayrı yazıda</a>.</li>
  <li><strong>Sosyal varlık, sosyal baskı değil.</strong> Odalarda herkes kendi sayacıyla çalışır; kimse kimsenin seansını bozamaz, kimse kimseyi "ağacı kuruttu" diye suçlayamaz.</li>
  <li><strong>Sıkıcı ama etkili olan da var.</strong> Haftalık istatistik grafiği hiç oyun değil, ama uzun vadede en çok işe yarayan geri bildirim o.</li>
</ul>

<h2 id="kime">Kim için işe yarar, kim için yaramaz?</h2>
<p>Oyunlaştırma en çok <strong>başlamakta zorlananlar</strong> ve <strong>ilerlemesini göremediği için bırakanlar</strong> için işe yarar. İşi zaten seven ve düzenli yapan biri için gereksiz, hatta dikkat dağıtıcı olabilir; o kişi sade bir sayaçla mutlu olur. Sen hangisisin bilmiyorsan iki hafta oyunlaştırmalı bir uygulama, iki hafta sade sayaç dene ve haftalık toplamlara bak. Sayı karar versin.</p>

<h2 id="ozet">Özet</h2>
<p>Oyunlaştırma sihirli değil; iyi tasarlandığında başlamayı kolaylaştırır, ilerlemeyi görünür kılar ve yalnız çalışan birine takım hissi verir. Kötü tasarlandığında kaygı üretir ve birkaç haftada silinir. Fark, mekaniğin işin kendisine ve insanın temel ihtiyaçlarına ne kadar bağlandığında.</p>
""",
  faq=[
    ("Oyunlaştırma gerçekten verimliliği artırıyor mu?", "Araştırmalar kısa vadede katılımı artırdığını, uzun vadede etkinin mekaniğe ve kişiye bağlı olduğunu gösteriyor. Görünür ilerleme, anlamlı geri bildirim ve takım hedefleri kalıcı çalışıyor; ceza ve yapay puanlar birkaç haftada sönüyor."),
    ("Forest'taki ağaç kurma mekaniği neden işe yarıyor?", "Kayıptan kaçınma dürtüsünü kullanır ve ilk aylarda güçlüdür. Ancak ceza temelli motivasyon zamanla zayıflar; kullanıcı ya cezayı önemsemez hâle gelir ya da uygulamayı bırakır. Başlatıcı olarak iyi, sürdürücü olarak zayıftır."),
    ("Streak yani seri mekaniği zararlı mı?", "Kişiye göre değişir. Bazıları için güçlü bir itki, ama kaçırılan tek günü felakete çevirdiği için bırakmayı da kolaylaştırır. Araştırmalar bir günü kaçırmanın alışkanlığa zarar vermediğini gösteriyor; seri kullanılacaksa haftalık ve affedici olmalı."),
    ("Pomi neden ceza kullanmıyor?", "Kaygı üzerine kurulu motivasyonun uzun vadede içsel motivasyonu zayıflattığını gösteren araştırmalara dayanarak. Yarım seansta bitki eklenmez ama hiçbir şey kurumaz ya da sıfırlanmaz; ilerleme bahçe, haftalık lig ve fetih haritasıyla görünür kılınır."),
    ("Oyunlaştırma kimin için uygun değil?", "İşi zaten seven ve düzenli yapan kişiler için gereksiz, hatta dikkat dağıtıcı olabilir. Böyle biri sade bir sayaçla daha iyi çalışır. Emin değilsen iki hafta oyunlaştırmalı, iki hafta sade sayaç deneyip haftalık toplamları karşılaştır."),
  ],
  sources=[
    "Hamari, J., Koivisto, J. &amp; Sarsa, H. (2014). Does gamification work? A literature review of empirical studies on gamification. <em>Proceedings of the 47th Hawaii International Conference on System Sciences</em>.",
    "Deci, E. L. &amp; Ryan, R. M. (2000). The \"what\" and \"why\" of goal pursuits: Human needs and the self-determination of behavior. <em>Psychological Inquiry</em>, 11(4).",
    "Deci, E. L., Koestner, R. &amp; Ryan, R. M. (1999). A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation. <em>Psychological Bulletin</em>, 125(6).",
    "Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W. &amp; Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <em>European Journal of Social Psychology</em>, 40(6).",
  ],
))
