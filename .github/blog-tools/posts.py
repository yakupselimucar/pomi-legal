# -*- coding: utf-8 -*-
"""Blog yazılarının içeriği. build_blog.py bunu HTML'e çevirir."""

IOS = "https://apps.apple.com/tr/app/id6784132034"
ANDROID = "https://play.google.com/store/apps/details?id=com.yakupselimucar.pomi"
SITE = "https://yakupselimucar.github.io/pomi-legal/"
D = "2026-09-13"
DH_TR = "13 Eylül 2026"
DH_EN = "September 13, 2026"
RFC = "Sun, 13 Sep 2026 09:00:00 +0300"

POSTS = []

# ─────────────────────────────────────────────────────────────────
# 1) TR — 2026'nın en iyi Pomodoro uygulamaları
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="en-iyi-pomodoro-uygulamalari-2026", lang="tr", pair="best-pomodoro-apps-2026",
  related=["forest-alternatifi-ucretsiz-uygulamalar", "pomodoro-teknigi-nedir", "odak-uygulamalarinda-oyunlastirma-ise-yarar-mi"],
  section="Karşılaştırma", date=D, date_human=DH_TR, rfc822=RFC, read=7, words=1400,
  title="2026'nın En İyi Pomodoro Uygulamaları (iOS ve Android)",
  short="En iyi Pomodoro uygulamaları 2026",
  h1="2026'nın en iyi <span class=\"accent\">Pomodoro</span> uygulamaları",
  lead="Sekiz uygulamayı aynı kriterlerle karşılaştırdık: ücret, reklam, çevrimdışı çalışma, oyunlaştırma ve birlikte çalışma. Hangisi kime uygun, kısa ve net.",
  desc="2026'da iPhone ve Android için en iyi Pomodoro uygulamaları: Pomi, Forest, Focus To-Do, Flora, Pomofocus, Tide, Study Bunny ve Be Focused. Ücret, reklam, çevrimdışı ve birlikte çalışma karşılaştırması.",
  keywords="en iyi pomodoro uygulamaları, pomodoro uygulaması, odak zamanlayıcı, pomodoro android, pomodoro iphone, ders çalışma uygulaması 2026",
  tldr="""<p><strong>Kısa cevap:</strong> Arkadaşlarınla birlikte çalışmak ve ilerlemeni görselleştirmek istiyorsan <strong>Pomi</strong>; sadece telefonu elinden bırakmak istiyorsan <strong>Forest</strong>; görev listesini sayaçla birleştirmek istiyorsan <strong>Focus To-Do</strong>; hiçbir şey yüklemek istemiyorsan <strong>Pomofocus</strong> iyi bir seçim. Hepsi ücretsiz başlangıç sunuyor.</p>""",
  itemlist=[("Pomi", SITE), ("Forest", "https://www.forestapp.cc/"), ("Focus To-Do", "https://www.focustodo.cn/"), ("Flora", "https://flora.appfinca.com/"), ("Pomofocus", "https://pomofocus.io/"), ("Tide", "https://tide.fm/"), ("Study Bunny", "https://apps.apple.com/app/id1219395424"), ("Be Focused", "https://apps.apple.com/app/id973134470")],
  body="""
<h2 id="nasil-sectik">Bu listeyi nasıl hazırladık?</h2>
<p>Pomodoro uygulamalarının çoğu aynı şeyi yapar: 25 dakika say, 5 dakika mola ver. Farkı yaratan, sayacın etrafına ne koyduklarıdır. Her uygulamayı şu altı soruya göre değerlendirdik:</p>
<ul>
  <li><strong>Ücret ve reklam:</strong> Ücretsiz sürüm gerçekten kullanılabilir mi, reklam var mı?</li>
  <li><strong>Çevrimdışı:</strong> İnternet yokken sayaç çalışıyor mu?</li>
  <li><strong>Arka plan:</strong> Uygulamayı kapatınca sayaç devam ediyor mu?</li>
  <li><strong>Oyunlaştırma:</strong> Seans bitince elle tutulur bir şey kazanıyor musun?</li>
  <li><strong>Birlikte çalışma:</strong> Arkadaşlarınla aynı anda odaklanabiliyor musun?</li>
  <li><strong>Platform:</strong> iOS, Android, web, masaüstü?</li>
</ul>

<h2 id="tablo">Karşılaştırma tablosu</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Uygulama</th><th>Platform</th><th>Ücretsiz sürüm</th><th>Reklam</th><th>Çevrimdışı</th><th>Oyunlaştırma</th><th>Birlikte çalışma</th></tr></thead>
  <tbody>
    <tr><td>Pomi</td><td>iOS, Android</td><td>Evet, tam sayaç</td><td>Yok</td><td>Evet</td><td>Piksel bahçe, fetih haritası, lig</td><td>Canlı odalar (herkes kendi sayacıyla)</td></tr>
    <tr><td>Forest</td><td>iOS, Android, tarayıcı eklentisi</td><td>Android'de ücretsiz, iOS'ta ücretli</td><td>Ücretsiz sürümde var</td><td>Evet</td><td>Sanal ağaç dikme</td><td>Ortak ağaç dikme</td></tr>
    <tr><td>Focus To-Do</td><td>iOS, Android, Windows, macOS, web</td><td>Evet</td><td>Yok</td><td>Evet</td><td>Yok, istatistik odaklı</td><td>Yok</td></tr>
    <tr><td>Flora</td><td>iOS, Android</td><td>Evet</td><td>Yok</td><td>Kısmen</td><td>Ağaç dikme</td><td>Arkadaşla ortak seans</td></tr>
    <tr><td>Pomofocus</td><td>Web</td><td>Evet</td><td>Var</td><td>Sınırlı</td><td>Yok</td><td>Yok</td></tr>
    <tr><td>Tide</td><td>iOS, Android</td><td>Evet, sınırlı</td><td>Yok</td><td>Evet</td><td>Yok, ses odaklı</td><td>Yok</td></tr>
    <tr><td>Study Bunny</td><td>iOS, Android</td><td>Evet</td><td>Var</td><td>Evet</td><td>Tavşan bakımı, para birimi</td><td>Yok</td></tr>
    <tr><td>Be Focused</td><td>iOS, macOS</td><td>Evet</td><td>Ücretsiz sürümde var</td><td>Evet</td><td>Yok</td><td>Yok</td></tr>
  </tbody>
</table>
</div>
<p class="note">Bilgiler Eylül 2026'daki mağaza sayfalarına dayanır. Uygulamalar fiyat ve özellik değiştirebilir; indirmeden önce mağaza sayfasını kontrol et.</p>

<h2 id="liste">Uygulamalar tek tek</h2>

<div class="app-card ours">
  <h3>1. Pomi <span class="tag rose">Birlikte çalışma</span> <span class="tag">Reklamsız</span></h3>
  <p>Pomi, her tamamlanan 25 dakikalık seansı piksel bir bahçede yeni bir bitkiye dönüştürür. Diğer oyunlaştırılmış sayaçlardan iki farkı var: <strong>canlı odalar</strong> ve <strong>fetih haritası</strong>. Odalarda arkadaşlarınla aynı ekranda çalışırsın ama herkes kendi sayacını kullanır; biri mola verince diğerlerinin seansı bozulmaz. Fetih haritasında odak dakikaların şehrine puan yazar ve Türkiye'nin 81 şehri 7 günlük sezonlarda bölge kazanmak için yarışır.</p>
  <dl>
    <dt>Kime uygun</dt><dd>Sınava hazırlanan öğrenciler, "study with me" tarzı birlikte çalışmayı sevenler, ilerlemesini görmek isteyenler</dd>
    <dt>Ücret</dt><dd>Ücretsiz; isteğe bağlı Pomi Pro aboneliği. Reklam yok.</dd>
    <dt>Eksik</dt><dd>Web ve masaüstü sürümü yok; şu an yalnızca iOS ve Android.</dd>
    <dt>İndir</dt><dd><a href="%s" rel="noopener">App Store</a> · <a href="%s" rel="noopener">Google Play</a></dd>
  </dl>
</div>

<div class="app-card">
  <h3>2. Forest <span class="tag sun">Telefon bağımlılığı</span></h3>
  <p>Kategorinin en bilinen uygulaması. Seansı başlatınca bir ağaç dikersin, uygulamadan çıkarsan ağaç kurur. Basit ve etkili bir "telefonu elinden bırak" mekaniği. Android'de reklamlı ücretsiz sürüm var, iOS'ta tek seferlik ücretli.</p>
  <dl>
    <dt>Kime uygun</dt><dd>Sorunu odaklanmaktan çok telefonu bırakamamak olanlar</dd>
    <dt>Eksik</dt><dd>Görev yönetimi zayıf; sosyal özellikler sınırlı.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>3. Focus To-Do <span class="tag sky">Görev + sayaç</span></h3>
  <p>Pomodoro sayacıyla tam bir görev yöneticisini birleştirir: projeler, alt görevler, tekrar eden işler, tahmini pomodoro sayısı. Telefon, bilgisayar ve web arasında senkronize olur. Oyunlaştırma yok, bu bazıları için artı.</p>
  <dl>
    <dt>Kime uygun</dt><dd>İş takibi yapan profesyoneller, çok cihaz kullananlar</dd>
    <dt>Eksik</dt><dd>Arayüz kalabalık; motivasyon katmanı yok.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>4. Flora <span class="tag">Ücretsiz</span></h3>
  <p>Forest'a benzer ağaç dikme mekaniği, ama ücretsiz ve arkadaşınla ortak seans başlatabiliyorsun. Seansı bozan kişi ağacı öldürür; sosyal baskı işe yarıyor.</p>
  <dl>
    <dt>Kime uygun</dt><dd>Forest'ı ücretsiz isteyenler, çiftler ve ikili çalışma grupları</dd>
    <dt>Eksik</dt><dd>İstatistikler ve görev yönetimi yüzeysel.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>5. Pomofocus <span class="tag sky">Web</span></h3>
  <p>Tarayıcıda açılan, kurulum gerektirmeyen bir Pomodoro sayacı. Süreleri ayarlar, görev eklersin, o kadar. Bilgisayar başında çalışanlar için en hızlı başlangıç.</p>
  <dl>
    <dt>Kime uygun</dt><dd>Masaüstünde çalışanlar, uygulama yüklemek istemeyenler</dd>
    <dt>Eksik</dt><dd>Mobil uygulama yok; sekmeyi kapatınca sayaç durur.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>6. Tide <span class="tag">Sesler</span></h3>
  <p>Odak sayacı ile doğa sesleri, meditasyon ve uyku modlarını tek uygulamada toplar. Tasarımı sakin ve şık. Sayaç ikinci planda, asıl ürün ses.</p>
  <dl>
    <dt>Kime uygun</dt><dd>Beyaz gürültüyle çalışanlar, nefes egzersizi isteyenler</dd>
    <dt>Eksik</dt><dd>Görev ve sosyal özellik yok; ücretsiz sürüm sınırlı.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>7. Study Bunny <span class="tag sun">Öğrenci</span></h3>
  <p>Çalıştıkça beslediğin bir tavşan karakteri, biriken para birimi ve dükkân. Lise ve üniversite öğrencileri arasında popüler; sevimli ama reklam yoğunluğu yüksek.</p>
  <dl>
    <dt>Kime uygun</dt><dd>Sevimli karakter isteyen öğrenciler</dd>
    <dt>Eksik</dt><dd>Reklamlar; tasarım eski.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>8. Be Focused <span class="tag sky">Apple</span></h3>
  <p>iPhone ve Mac'te sade bir Pomodoro sayacı. Görev bazlı istatistik tutar, iCloud ile senkronize olur. Fazlası yok, eksiği de yok.</p>
  <dl>
    <dt>Kime uygun</dt><dd>Sadelik isteyen Apple kullanıcıları</dd>
    <dt>Eksik</dt><dd>Android yok; ücretsiz sürümde reklam.</dd>
  </dl>
</div>

<h2 id="hangisi">Hangi Pomodoro uygulamasını seçmeliyim?</h2>
<ul>
  <li><strong>Arkadaşlarınla çalışıyorsan:</strong> Pomi (herkes kendi sayacıyla, ortak oda) veya Flora (ikili ortak seans).</li>
  <li><strong>Telefonu bırakamıyorsan:</strong> Forest.</li>
  <li><strong>Görev listen kalabalıksa:</strong> Focus To-Do.</li>
  <li><strong>Bilgisayardaysan ve hemen başlamak istiyorsan:</strong> Pomofocus.</li>
  <li><strong>Sesle çalışıyorsan:</strong> Tide veya Pomi'nin karıştırılabilir odak sesleri.</li>
</ul>
<p>Hangisini seçersen seç, tekniğin kendisi uygulamadan önemli. Nasıl uygulandığını <a href="pomodoro-teknigi-nedir.html">Pomodoro tekniği rehberimizde</a> anlattık.</p>
""" % (IOS, ANDROID),
  faq=[
    ("En iyi ücretsiz Pomodoro uygulaması hangisi?", "Reklamsız ve tam özellikli ücretsiz sürüm arıyorsan Pomi ve Focus To-Do öne çıkar. Pomi oyunlaştırma ve birlikte çalışma, Focus To-Do görev yönetimi tarafında güçlüdür. Web için Pomofocus ücretsizdir."),
    ("Arkadaşlarımla birlikte kullanabileceğim bir Pomodoro uygulaması var mı?", "Evet. Pomi'de 6 haneli davet koduyla canlı odalar kurulur; herkes aynı odada ama kendi sayacıyla çalışır. Flora ve Forest ise ortak ağaç dikme seansı sunar; orada biri seansı bozarsa herkes etkilenir."),
    ("Pomodoro uygulaması telefonu kapatınca çalışmaya devam eder mi?", "Pomi, Forest, Focus To-Do, Tide ve Be Focused arka planda ve uygulama kapalıyken saymaya devam eder. Web tabanlı Pomofocus'ta sekmeyi kapatırsan sayaç durur."),
    ("Pomodoro uygulaması çevrimdışı çalışır mı?", "Pomi, Forest, Focus To-Do, Tide, Study Bunny ve Be Focused internet olmadan çalışır. Pomi'de odalar ve fetih haritası gibi sosyal özellikler için bağlantı gerekir, sayaç ve bahçe çevrimdışı çalışır."),
    ("Forest yerine ücretsiz alternatif var mı?", "Flora aynı ağaç dikme mekaniğini ücretsiz sunar. Pomi de ücretsizdir; ağaç yerine seans başına bir bitki büyütürsün ve ek olarak odalar ve şehir yarışı vardır."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# 1) EN — Best Pomodoro apps 2026
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="best-pomodoro-apps-2026", lang="en", pair="en-iyi-pomodoro-uygulamalari-2026",
  related=["forest-app-alternatives", "what-is-the-pomodoro-technique", "does-gamification-help-you-focus"],
  section="Comparison", date=D, date_human=DH_EN, rfc822=RFC, read=7, words=1350,
  title="The Best Pomodoro Apps in 2026 (iOS and Android)",
  short="Best Pomodoro apps 2026",
  h1="The best <span class=\"accent\">Pomodoro</span> apps in 2026",
  lead="Eight apps compared on the same criteria: price, ads, offline use, gamification and studying together. Which one fits you, in plain terms.",
  desc="The best Pomodoro apps for iPhone and Android in 2026: Pomi, Forest, Focus To-Do, Flora, Pomofocus, Tide, Study Bunny and Be Focused, compared on price, ads, offline use and co-working.",
  keywords="best pomodoro apps, pomodoro app, focus timer app, pomodoro android, pomodoro iphone, study app 2026, study with me app",
  tldr="""<p><strong>Short answer:</strong> If you want to study together with friends and see your progress grow, pick <strong>Pomi</strong>. If your problem is putting the phone down, pick <strong>Forest</strong>. If you live in a task list, pick <strong>Focus To-Do</strong>. If you do not want to install anything, use <strong>Pomofocus</strong>. All of them have a free tier.</p>""",
  itemlist=[("Pomi", SITE), ("Forest", "https://www.forestapp.cc/"), ("Focus To-Do", "https://www.focustodo.cn/"), ("Flora", "https://flora.appfinca.com/"), ("Pomofocus", "https://pomofocus.io/"), ("Tide", "https://tide.fm/"), ("Study Bunny", "https://apps.apple.com/app/id1219395424"), ("Be Focused", "https://apps.apple.com/app/id973134470")],
  body="""
<h2 id="method">How we picked</h2>
<p>Most Pomodoro apps do the same core thing: count 25 minutes, then 5. What differs is what they build around the timer. We rated each app on six questions:</p>
<ul>
  <li><strong>Price and ads:</strong> Is the free tier actually usable, and does it show ads?</li>
  <li><strong>Offline:</strong> Does the timer work without internet?</li>
  <li><strong>Background:</strong> Does the timer keep running when you close the app?</li>
  <li><strong>Gamification:</strong> Do you earn something tangible when a session ends?</li>
  <li><strong>Studying together:</strong> Can you focus with friends at the same time?</li>
  <li><strong>Platforms:</strong> iOS, Android, web, desktop?</li>
</ul>

<h2 id="table">Comparison table</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>App</th><th>Platforms</th><th>Free tier</th><th>Ads</th><th>Offline</th><th>Gamification</th><th>Study together</th></tr></thead>
  <tbody>
    <tr><td>Pomi</td><td>iOS, Android</td><td>Yes, full timer</td><td>None</td><td>Yes</td><td>Pixel garden, conquest map, weekly league</td><td>Live rooms (everyone on their own timer)</td></tr>
    <tr><td>Forest</td><td>iOS, Android, browser extension</td><td>Free on Android, paid on iOS</td><td>In free tier</td><td>Yes</td><td>Virtual tree planting</td><td>Group planting</td></tr>
    <tr><td>Focus To-Do</td><td>iOS, Android, Windows, macOS, web</td><td>Yes</td><td>None</td><td>Yes</td><td>None, stats-focused</td><td>No</td></tr>
    <tr><td>Flora</td><td>iOS, Android</td><td>Yes</td><td>None</td><td>Partial</td><td>Tree planting</td><td>Shared session with a friend</td></tr>
    <tr><td>Pomofocus</td><td>Web</td><td>Yes</td><td>Yes</td><td>Limited</td><td>None</td><td>No</td></tr>
    <tr><td>Tide</td><td>iOS, Android</td><td>Yes, limited</td><td>None</td><td>Yes</td><td>None, sound-focused</td><td>No</td></tr>
    <tr><td>Study Bunny</td><td>iOS, Android</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Bunny care, in-app currency</td><td>No</td></tr>
    <tr><td>Be Focused</td><td>iOS, macOS</td><td>Yes</td><td>In free tier</td><td>Yes</td><td>None</td><td>No</td></tr>
  </tbody>
</table>
</div>
<p class="note">Based on public store listings as of September 2026. Apps change prices and features; check the store page before downloading.</p>

<h2 id="apps">The apps, one by one</h2>

<div class="app-card ours">
  <h3>1. Pomi <span class="tag rose">Study together</span> <span class="tag">No ads</span></h3>
  <p>Pomi turns every completed 25-minute session into a new plant in a pixel-art garden. Two things set it apart from other gamified timers: <strong>live rooms</strong> and a <strong>conquest map</strong>. In a room you focus on the same screen as your friends, but everyone runs their own timer, so one person taking a break does not break anyone else's session. On the conquest map your focus minutes score points for your city, and 81 cities of Turkey compete for regions in 7-day seasons.</p>
  <dl>
    <dt>Best for</dt><dd>Students preparing for exams, fans of "study with me" co-working, anyone who wants to see progress accumulate</dd>
    <dt>Price</dt><dd>Free, with an optional Pomi Pro subscription. No ads.</dd>
    <dt>Missing</dt><dd>No web or desktop version yet; iOS and Android only.</dd>
    <dt>Get it</dt><dd><a href="%s" rel="noopener">App Store</a> · <a href="%s" rel="noopener">Google Play</a></dd>
  </dl>
</div>

<div class="app-card">
  <h3>2. Forest <span class="tag sun">Phone addiction</span></h3>
  <p>The best-known app in the category. Start a session and you plant a tree; leave the app and the tree dies. A simple, effective "put the phone down" mechanic. Free with ads on Android, a one-time purchase on iOS.</p>
  <dl>
    <dt>Best for</dt><dd>People whose real problem is picking up the phone, not focusing</dd>
    <dt>Missing</dt><dd>Weak task management; limited social features.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>3. Focus To-Do <span class="tag sky">Tasks + timer</span></h3>
  <p>Combines a Pomodoro timer with a full task manager: projects, subtasks, recurring tasks, estimated pomodoros per task. Syncs across phone, desktop and web. No gamification, which some people prefer.</p>
  <dl>
    <dt>Best for</dt><dd>Professionals tracking work, multi-device users</dd>
    <dt>Missing</dt><dd>Busy interface; no motivation layer.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>4. Flora <span class="tag">Free</span></h3>
  <p>The same tree-planting idea as Forest, but free, and you can start a shared session with a friend. Whoever breaks the session kills the tree. Social pressure works.</p>
  <dl>
    <dt>Best for</dt><dd>People who want Forest for free, couples and study pairs</dd>
    <dt>Missing</dt><dd>Shallow statistics and task management.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>5. Pomofocus <span class="tag sky">Web</span></h3>
  <p>A browser-based Pomodoro timer with nothing to install. Set your durations, add tasks, go. The fastest start if you work at a computer.</p>
  <dl>
    <dt>Best for</dt><dd>Desktop workers, anyone who does not want another app</dd>
    <dt>Missing</dt><dd>No mobile app; the timer stops when you close the tab.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>6. Tide <span class="tag">Sounds</span></h3>
  <p>Bundles a focus timer with nature sounds, meditation and sleep modes. Calm, polished design. The timer is secondary; the real product is the audio.</p>
  <dl>
    <dt>Best for</dt><dd>People who work with white noise, anyone wanting breathing exercises</dd>
    <dt>Missing</dt><dd>No tasks or social features; limited free tier.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>7. Study Bunny <span class="tag sun">Students</span></h3>
  <p>A bunny you feed by studying, in-app coins and a shop. Popular with high-school and university students. Cute, but heavy on ads.</p>
  <dl>
    <dt>Best for</dt><dd>Students who want a cute character</dd>
    <dt>Missing</dt><dd>Ads; dated design.</dd>
  </dl>
</div>

<div class="app-card">
  <h3>8. Be Focused <span class="tag sky">Apple</span></h3>
  <p>A clean Pomodoro timer for iPhone and Mac. Tracks stats per task and syncs through iCloud. Nothing extra, nothing missing.</p>
  <dl>
    <dt>Best for</dt><dd>Apple users who want simplicity</dd>
    <dt>Missing</dt><dd>No Android; ads in the free tier.</dd>
  </dl>
</div>

<h2 id="which">Which Pomodoro app should I choose?</h2>
<ul>
  <li><strong>Studying with friends:</strong> Pomi (shared room, individual timers) or Flora (paired session).</li>
  <li><strong>Cannot put the phone down:</strong> Forest.</li>
  <li><strong>Long task list:</strong> Focus To-Do.</li>
  <li><strong>At a computer, want to start now:</strong> Pomofocus.</li>
  <li><strong>Work with sound:</strong> Tide, or Pomi's mixable focus sounds.</li>
</ul>
<p>Whichever you choose, the technique matters more than the app. Our Turkish-language <a href="pomodoro-teknigi-nedir.html" hreflang="tr">Pomodoro guide</a> covers how to apply it.</p>
""" % (IOS, ANDROID),
  faq=[
    ("What is the best free Pomodoro app?", "For an ad-free, fully usable free tier, Pomi and Focus To-Do stand out. Pomi is stronger on gamification and studying together; Focus To-Do is stronger on task management. On the web, Pomofocus is free."),
    ("Is there a Pomodoro app I can use with friends?", "Yes. Pomi has live rooms you join with a 6-character invite code; everyone is in the same room but runs their own timer. Flora and Forest offer shared tree-planting sessions, where one person leaving affects everyone."),
    ("Does the timer keep running when I close the app?", "Pomi, Forest, Focus To-Do, Tide and Be Focused keep counting in the background and when the app is closed. The web-based Pomofocus stops when you close the tab."),
    ("Do Pomodoro apps work offline?", "Pomi, Forest, Focus To-Do, Tide, Study Bunny and Be Focused work without internet. In Pomi, social features such as rooms and the conquest map need a connection, while the timer and garden work offline."),
    ("Is there a free alternative to Forest?", "Flora offers the same tree-planting mechanic for free. Pomi is also free; instead of a tree you grow one plant per session, plus rooms and a city competition."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# 2) TR — Öğrenciler için en iyi odaklanma araçları
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="ogrenciler-icin-en-iyi-odaklanma-araclari", lang="tr", pair="best-focus-apps-for-students",
  related=["verimli-ders-calisma-teknikleri", "ders-calisirken-telefonu-birakmak", "odaklanmak-icin-en-iyi-sesler"],
  section="Öğrenciler", date=D, date_human=DH_TR, rfc822=RFC, read=6, words=1150,
  title="Öğrenciler İçin En İyi Odaklanma Araçları (2026)",
  short="Öğrenciler için odaklanma araçları",
  h1="Öğrenciler için en iyi <span class=\"accent\">odaklanma</span> araçları",
  lead="YKS, LGS, KPSS ya da final haftası. Uygulama yığını değil, dört ihtiyaca dört araç: sayaç, engelleyici, tekrar sistemi ve planlayıcı.",
  desc="2026'da öğrenciler için en iyi odaklanma araçları: Pomodoro sayacı (Pomi), site engelleyici, aralıklı tekrar (Anki), planlayıcı ve odak sesleri. Az uygulama, net kullanım.",
  keywords="öğrenciler için odaklanma uygulamaları, ders çalışma uygulaması, yks çalışma uygulaması, odaklanma araçları, verimli ders çalışma, study with me",
  tldr="""<p><strong>Kısa cevap:</strong> Bir öğrencinin ihtiyacı dört araçtan fazlası değil: zamanı bölmek için bir <strong>Pomodoro sayacı</strong> (Pomi), dikkat dağıtıcıları kesmek için bir <strong>engelleyici</strong>, ezber için <strong>aralıklı tekrar</strong> (Anki) ve haftayı görmek için bir <strong>planlayıcı</strong>. Gerisi isteğe bağlı.</p>""",
  body="""
<h2 id="neden-dort">Neden dört araç, on değil?</h2>
<p>Her yeni uygulama bir kurulum, bir bildirim ve bir dikkat dağıtıcı daha demek. Uzun süre ders çalışan öğrencilerde ortak nokta, kullandıkları uygulama sayısının azlığı. Aşağıdaki liste, her ihtiyaç için tek bir öneriyle sınırlı tutuldu; alternatifler kısa not olarak var.</p>

<h2 id="sayac">1. Zamanı bölmek: Pomodoro sayacı</h2>
<div class="app-card ours">
  <h3>Pomi <span class="tag rose">Öneri</span></h3>
  <p>25 dakika çalış, 5 dakika dinlen; her seans piksel bahçende bir bitki büyütür. Öğrenciler için asıl fark <strong>odalar</strong>: sınıf arkadaşlarınla 6 haneli davet koduyla aynı odaya girersin, herkes kendi sayacını çalıştırır. Kütüphane hissi, kütüphaneye gitmeden. <strong>Fetih haritası</strong> odak dakikalarını şehrine puan olarak yazar; 81 şehir 7 günlük sezonlarda yarışır. Reklam yok, çevrimdışı çalışır.</p>
  <dl>
    <dt>Nasıl kullan</dt><dd>Her ders için bir görev oluştur, seansı göreve bağla. Haftalık istatistikte hangi derse kaç saat gittiğini gör.</dd>
    <dt>Alternatif</dt><dd>Forest (telefonu bırakamayanlar için), Focus To-Do (görev ağırlıklı)</dd>
    <dt>İndir</dt><dd><a href="%s" rel="noopener">App Store</a> · <a href="%s" rel="noopener">Google Play</a></dd>
  </dl>
</div>
<p>Tüm sayaçların karşılaştırması için <a href="en-iyi-pomodoro-uygulamalari-2026.html">2026'nın en iyi Pomodoro uygulamaları</a> yazısına bak.</p>

<h2 id="engelleyici">2. Dikkat dağıtıcıları kesmek: engelleyici</h2>
<p>Sayaç çalışırken TikTok'a bakmak seansı boşa çıkarır. Telefonun kendi araçları çoğu öğrenci için yeterli:</p>
<ul>
  <li><strong>iPhone:</strong> Ayarlar → Ekran Süresi → Uygulama Sınırları, ya da bir "Odaklanma" modu oluşturup ders saatlerine planla.</li>
  <li><strong>Android:</strong> Dijital Denge → Odak modu; seçtiğin uygulamalar gri çıkar ve açılmaz.</li>
  <li><strong>Bilgisayar:</strong> Cold Turkey veya Freedom gibi engelleyiciler; tarayıcıda uBlock Origin ile YouTube önerilerini kapat.</li>
</ul>
<p class="note mint">Pomi'de seans başlatınca uygulama kilitlemesi yok; bilerek. Bahçe ve oda seni ekranda tutar, yasak değil. Yasak istiyorsan yukarıdaki sistem araçlarını Pomi ile birlikte kullan.</p>

<h2 id="tekrar">3. Ezber ve kalıcılık: aralıklı tekrar</h2>
<p><strong>Anki</strong> (Android'de ücretsiz, iOS'ta ücretli, web ücretsiz) aralıklı tekrar algoritmasıyla kartları tam unutmak üzereyken önüne getirir. Tıp, hukuk, dil ve YKS öğrencilerinin yıllardır kullandığı bir sistem. Alternatif: Quizlet (daha kolay, daha az güçlü).</p>
<p>Pratik kural: Anki'yi Pomodoro molalarına değil, günün ilk seansına koy. Tekrar bittiğinde yeni konuya geç.</p>

<h2 id="planlayici">4. Haftayı görmek: planlayıcı</h2>
<p>Google Takvim ya da Apple Takvim yeter. Her derse haftada kaç seans ayıracağını takvime blok olarak yaz; Pomi'deki haftalık istatistikle karşılaştır. Planla gerçek arasındaki fark, bir sonraki haftanın planıdır.</p>
<p>Not tutmak için Notion veya Apple Notlar; ikisi de ücretsiz. Sistem kurmaya haftalar harcama, düz bir sayfa yeter.</p>

<h2 id="sesler">İsteğe bağlı: odak sesleri</h2>
<p>Bazı öğrenciler sessizlikte, bazıları kafe uğultusunda çalışır. Pomi'nin içinde yağmur, kafe ve orman gibi karıştırılabilir sesler var; ayrı bir uygulamaya gerek yok. Müzik dinleyeceksen sözsüz olsun; sözlü müzik okuduğunu anlamayı ölçülebilir biçimde düşürür.</p>

<h2 id="rutin">Bu araçlarla örnek bir çalışma günü</h2>
<ol>
  <li><strong>08:30</strong> Telefonda odak modu açık. Anki tekrarı, 1 seans.</li>
  <li><strong>09:00</strong> Pomi'de arkadaşlarla oda. Matematik, 4 seans (2 saat), her 4 seanstan sonra 20 dakika uzun mola.</li>
  <li><strong>11:30</strong> Türkçe/paragraf, 2 seans.</li>
  <li><strong>Öğleden sonra</strong> Deneme çözümü; sayaç kapalı, gerçek sınav süresi.</li>
  <li><strong>Akşam</strong> Pomi haftalık istatistiğe bak, yarının takvim bloklarını düzelt.</li>
</ol>
<p>Pomodoro'nun neden 25 dakika olduğunu ve nasıl uyarlanacağını <a href="pomodoro-teknigi-nedir.html">Pomodoro tekniği nedir</a> yazısında anlattık. Arkadaşlarla çalışmanın neden işe yaradığına dair <a href="study-with-me-birlikte-ders-calisma.html">study with me rehberi</a> de var.</p>
""" % (IOS, ANDROID),
  faq=[
    ("YKS için en iyi odaklanma uygulaması hangisi?", "Tek bir uygulama yerine ihtiyaca göre seç: zamanı bölmek için Pomi gibi bir Pomodoro sayacı, sosyal medyayı kesmek için telefonun odak modu, ezber için Anki. Pomi'de odalar sayesinde sınıf arkadaşlarınla aynı anda çalışabilirsin."),
    ("Ders çalışırken telefonu nasıl bırakırım?", "Telefonun yerleşik odak modunu ders saatlerine planla, bildirimleri kapat ve sayacı başlat. Pomi gibi her seans için görsel bir ödül veren uygulamalar ekrana geri dönme isteğini azaltır."),
    ("Ders çalışırken müzik dinlemek zararlı mı?", "Sözlü müzik okuduğunu anlamayı düşürür. Sözsüz müzik, yağmur veya kafe sesi gibi sabit arka plan sesleri çoğu öğrenci için nötr veya faydalıdır. Pomi bu sesleri uygulama içinde sunar."),
    ("Arkadaşlarımla uzaktan birlikte ders çalışabilir miyim?", "Evet. Pomi'de bir oda oluşturup 6 haneli davet kodunu paylaşırsın; herkes aynı odada ama kendi sayacıyla çalışır. Kamera ya da mikrofon gerekmez."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# 2) EN — Best focus apps for students
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="best-focus-apps-for-students", lang="en", pair="ogrenciler-icin-en-iyi-odaklanma-araclari",
  related=["evidence-based-study-techniques", "how-to-stop-checking-your-phone-while-studying", "best-background-sounds-for-studying"],
  section="Students", date=D, date_human=DH_EN, rfc822=RFC, read=6, words=1100,
  title="The Best Focus Apps for Students (2026)",
  short="Best focus apps for students",
  h1="The best <span class=\"accent\">focus</span> apps for students",
  lead="Exam season or finals week. Not a pile of apps, but four tools for four needs: a timer, a blocker, spaced repetition and a planner.",
  desc="The best focus apps for students in 2026: a Pomodoro timer (Pomi), a distraction blocker, spaced repetition (Anki), a planner and focus sounds. Few apps, clear usage.",
  keywords="best focus apps for students, study apps, pomodoro app for students, study with me app, exam study apps 2026, focus tools",
  tldr="""<p><strong>Short answer:</strong> A student needs no more than four tools: a <strong>Pomodoro timer</strong> to split time (Pomi), a <strong>blocker</strong> to cut distractions, <strong>spaced repetition</strong> for memorisation (Anki) and a <strong>planner</strong> to see the week. Everything else is optional.</p>""",
  body="""
<h2 id="why-four">Why four tools, not ten?</h2>
<p>Every new app is one more setup, one more notification, one more distraction. Students who study for long stretches tend to have one thing in common: a short app list. This guide gives one recommendation per need, with alternatives as short notes.</p>

<h2 id="timer">1. Splitting time: a Pomodoro timer</h2>
<div class="app-card ours">
  <h3>Pomi <span class="tag rose">Pick</span></h3>
  <p>Work 25 minutes, rest 5; every session grows a plant in your pixel garden. The real difference for students is <strong>rooms</strong>: join classmates with a 6-character invite code, and everyone runs their own timer. The feel of a library, without going to one. The <strong>conquest map</strong> turns your focus minutes into points for your city, with 81 cities competing in 7-day seasons. No ads, works offline.</p>
  <dl>
    <dt>How to use it</dt><dd>Create one task per subject and link each session to it. The weekly stats show how many hours went to each subject.</dd>
    <dt>Alternatives</dt><dd>Forest (if you cannot put the phone down), Focus To-Do (task-heavy)</dd>
    <dt>Get it</dt><dd><a href="%s" rel="noopener">App Store</a> · <a href="%s" rel="noopener">Google Play</a></dd>
  </dl>
</div>
<p>For a full comparison of timers, see <a href="best-pomodoro-apps-2026.html">the best Pomodoro apps in 2026</a>.</p>

<h2 id="blocker">2. Cutting distractions: a blocker</h2>
<p>Checking TikTok while the timer runs wastes the session. The tools built into your phone are enough for most students:</p>
<ul>
  <li><strong>iPhone:</strong> Settings → Screen Time → App Limits, or create a Focus mode and schedule it for study hours.</li>
  <li><strong>Android:</strong> Digital Wellbeing → Focus mode; chosen apps turn grey and will not open.</li>
  <li><strong>Computer:</strong> Blockers such as Cold Turkey or Freedom; in the browser, hide YouTube recommendations with uBlock Origin.</li>
</ul>
<p class="note mint">Pomi does not lock your apps when a session starts, on purpose. The garden and the room keep you on task through reward, not prohibition. If you want prohibition, combine Pomi with the system tools above.</p>

<h2 id="repetition">3. Memorisation: spaced repetition</h2>
<p><strong>Anki</strong> (free on Android and web, paid on iOS) uses a spaced-repetition algorithm to show you a card right before you would forget it. Medical, law and language students have relied on it for years. Alternative: Quizlet (easier, less powerful).</p>
<p>Practical rule: put Anki in the first session of the day, not in the Pomodoro breaks. When review is done, move on to new material.</p>

<h2 id="planner">4. Seeing the week: a planner</h2>
<p>Google Calendar or Apple Calendar is enough. Block out how many sessions each subject gets per week, then compare with Pomi's weekly stats. The gap between plan and reality is next week's plan.</p>
<p>For notes, Notion or Apple Notes, both free. Do not spend weeks building a system; a plain page is fine.</p>

<h2 id="sounds">Optional: focus sounds</h2>
<p>Some students work in silence, others in café noise. Pomi includes mixable sounds such as rain, café and forest, so no extra app is needed. If you listen to music, make it instrumental; lyrics measurably reduce reading comprehension.</p>

<h2 id="routine">A sample study day with these tools</h2>
<ol>
  <li><strong>08:30</strong> Focus mode on. Anki review, 1 session.</li>
  <li><strong>09:00</strong> Pomi room with friends. Maths, 4 sessions (2 hours), 20-minute long break after every 4 sessions.</li>
  <li><strong>11:30</strong> Reading and essays, 2 sessions.</li>
  <li><strong>Afternoon</strong> Practice exam; timer off, real exam timing.</li>
  <li><strong>Evening</strong> Check Pomi weekly stats, adjust tomorrow's calendar blocks.</li>
</ol>
""" % (IOS, ANDROID),
  faq=[
    ("What is the best focus app for exam preparation?", "Choose by need rather than a single app: a Pomodoro timer such as Pomi to split time, your phone's focus mode to cut social media, and Anki for memorisation. Pomi's rooms let you study at the same time as classmates."),
    ("How do I stop picking up my phone while studying?", "Schedule your phone's built-in focus mode for study hours, silence notifications and start a timer. Apps like Pomi that give a visible reward per session reduce the urge to return to the screen."),
    ("Is listening to music while studying bad?", "Music with lyrics reduces reading comprehension. Instrumental music or steady background sounds such as rain or café noise are neutral or helpful for most students. Pomi provides these sounds in-app."),
    ("Can I study together with friends remotely?", "Yes. In Pomi you create a room and share a 6-character invite code; everyone is in the same room but on their own timer. No camera or microphone needed."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# 3) TR — Pomodoro tekniği nedir?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="pomodoro-teknigi-nedir", lang="tr", pair="what-is-the-pomodoro-technique",
  related=["pomodoro-mu-flowtime-mi-52-17-odak-teknikleri", "gunde-kac-pomodoro-yapmali", "pomodoro-molasinda-ne-yapmali"],
  section="Temel bilgi", date=D, date_human=DH_TR, rfc822=RFC, read=6, words=1100,
  title="Pomodoro Tekniği Nedir? Nasıl Uygulanır? (Adım Adım Rehber)",
  short="Pomodoro tekniği nedir",
  h1="Pomodoro tekniği <span class=\"accent\">nedir</span>, nasıl uygulanır?",
  lead="25 dakika çalış, 5 dakika dinlen. Tekniğin kökeni, neden işe yaradığı, sık yapılan hatalar ve kendine göre nasıl uyarlayacağın.",
  desc="Pomodoro tekniği nedir, nasıl uygulanır? 25/5 döngüsü, uzun mola kuralı, Francesco Cirillo'nun yöntemi, sık hatalar ve öğrenciler için uyarlama önerileri.",
  keywords="pomodoro tekniği nedir, pomodoro nasıl uygulanır, pomodoro tekniği, 25 dakika çalışma tekniği, odaklanma teknikleri, verimli ders çalışma yöntemleri",
  tldr="""<p><strong>Kısa cevap:</strong> Pomodoro tekniği, işi <strong>25 dakikalık kesintisiz odak</strong> bloklarına bölüp her blok sonunda <strong>5 dakika mola</strong> vermeye dayanır. Dört bloktan sonra 15 ile 30 dakika arası uzun mola verilir. 1980'lerin sonunda Francesco Cirillo tarafından geliştirildi; adı, kullandığı domates şeklindeki mutfak zamanlayıcısından gelir.</p>""",
  body="""
<h2 id="tanim">Pomodoro tekniği nedir?</h2>
<p>Pomodoro, İtalyanca "domates" demek. Üniversite öğrencisi Francesco Cirillo 1980'lerin sonunda ders çalışamadığı bir gün mutfaktan domates şeklindeki mekanik zamanlayıcıyı alıp "10 dakika odaklanabilir miyim?" diye denedi. Yöntem zamanla 25 dakikalık bloklara oturdu ve bugün dünyada en yaygın zaman yönetimi tekniklerinden biri hâline geldi.</p>
<p>Tekniğin özü tek cümle: <strong>Zamanı değil, dikkati yönet.</strong> 25 dakika kısa olduğu için başlaması kolay, bittiği belli olduğu için tükenmeden bırakırsın.</p>

<h2 id="adimlar">Pomodoro tekniği nasıl uygulanır? 6 adım</h2>
<ol>
  <li><strong>Görevi seç.</strong> Tek ve somut olsun: "matematik çalış" değil, "türev soru bankası sayfa 40-48".</li>
  <li><strong>Sayacı 25 dakikaya kur.</strong> Telefonun sayacı ya da <a href="%s">Pomi</a> gibi bir Pomodoro uygulaması.</li>
  <li><strong>Sayaç bitene kadar sadece o işi yap.</strong> Aklına gelen başka işleri kâğıda not et, sonra dön.</li>
  <li><strong>Sayaç çalınca dur.</strong> Cümlenin ortasında bile olsan. Bu, tekniğin en zor ve en önemli kuralı.</li>
  <li><strong>5 dakika mola.</strong> Ekrandan uzak: su iç, yürü, pencereye bak.</li>
  <li><strong>Dört pomodoro sonra 15-30 dakika uzun mola.</strong> Sonra döngüye baştan başla.</li>
</ol>

<h2 id="neden">Neden işe yarıyor?</h2>
<ul>
  <li><strong>Başlama direncini kırar.</strong> "3 saat çalışacağım" ürkütücü, "25 dakika" değil. Sayaç başladığında en zor kısım geride kalmıştır.</li>
  <li><strong>Zamanı görünür kılar.</strong> Bir sayfa sorunun kaç pomodoro tuttuğunu öğrenince plan yapmak kolaylaşır.</li>
  <li><strong>Molayı zorunlu kılar.</strong> Dikkat, süreklilik değil dalga hâlindedir. Düzenli kısa mola, öğleden sonra çöküşünü azaltır.</li>
  <li><strong>Kesintiyi ölçer.</strong> Bir pomodoroyu kaç kez böldüğünü saydığında, dikkat dağıtıcıların gerçek boyutunu görürsün.</li>
</ul>

<h2 id="hatalar">Sık yapılan 5 hata</h2>
<ol>
  <li><strong>Molada telefona bakmak.</strong> 5 dakikalık mola 20 dakikaya uzar ve dikkat sıfırlanır. Mola ekransız olsun.</li>
  <li><strong>Sayaç çalınca devam etmek.</strong> "Akış hâlindeyim" dersin, iki saat sonra tükenirsin. Bir pomodoro daha başlat, ama molayı atlama.</li>
  <li><strong>Çok büyük görev seçmek.</strong> "Tezimi yaz" bir pomodoroya sığmaz. Bir oturuşta bitecek parçaya böl.</li>
  <li><strong>Süreyi sürekli değiştirmek.</strong> Önce iki hafta 25/5 ile dene, sonra uyarlama yap.</li>
  <li><strong>Sadece sayaca güvenmek.</strong> Sayaç çalışırken bildirimler açıksa sayaç değil, telefon kazanır. Odak modunu aç.</li>
</ol>

<h2 id="uyarlama">Süreyi kendine göre uyarlamak</h2>
<p>25/5 bir başlangıç noktası, kutsal bir kural değil. Yaygın uyarlamalar:</p>
<div class="table-wrap">
<table>
  <thead><tr><th>Döngü</th><th>Kime uygun</th></tr></thead>
  <tbody>
    <tr><td>15 / 3</td><td>Başlamakta zorlananlar, dikkat eksikliği olanlar, ilk hafta</td></tr>
    <tr><td>25 / 5</td><td>Klasik. Ders çalışma, soru çözme, e-posta</td></tr>
    <tr><td>50 / 10</td><td>Yazılım, yazı yazma, derin okuma gibi ısınma gerektiren işler</td></tr>
    <tr><td>90 / 20</td><td>Ultradiyen ritme yakın. Deneyimli kullanıcılar, tek işe uzun dalış</td></tr>
  </tbody>
</table>
</div>
<p>Pomi'de çalışma ve mola sürelerini ayarlardan değiştirebilirsin; bahçedeki bitki hangi süreyi seçersen seç seans tamamlanınca büyür.</p>

<h2 id="ogrenci">Öğrenciler için not</h2>
<p>Deneme sınavı çözerken Pomodoro kullanma; gerçek sınav süresiyle çalış. Konu çalışırken, tekrar yaparken ve soru bankası çözerken kullan. Arkadaşlarınla aynı saatte çalışıyorsan, Pomi'de bir oda açıp herkesin kendi sayacıyla girmesi motivasyonu belirgin biçimde artırır; bunun nedenini <a href="study-with-me-birlikte-ders-calisma.html">study with me yazısında</a> anlattık.</p>
""" % SITE,
  faq=[
    ("Pomodoro tekniği kaç dakika?", "Klasik döngü 25 dakika çalışma ve 5 dakika moladır. Dört döngüden sonra 15 ile 30 dakika arası uzun mola verilir. Süreler kişiye göre 15/3 veya 50/10 gibi uyarlanabilir."),
    ("Pomodoro tekniğini kim buldu?", "Francesco Cirillo, 1980'lerin sonunda üniversite öğrencisiyken geliştirdi. Adı, kullandığı domates şeklindeki mutfak zamanlayıcısından gelir; pomodoro İtalyanca domates demektir."),
    ("Pomodoro molasında ne yapmalıyım?", "Ekrandan uzak kal: su iç, ayağa kalk, birkaç adım yürü, pencereden bak. Sosyal medya molası, 5 dakikayı 20 dakikaya uzatır ve odağı sıfırlar."),
    ("Pomodoro tekniği herkes için uygun mu?", "Çoğu iş için uygundur ama yaratıcı akış gerektiren uzun görevlerde 50/10 veya 90/20 gibi uzun bloklar daha iyi çalışabilir. Sınav simülasyonunda kullanılmamalı, gerçek sınav süresi esas alınmalıdır."),
    ("Pomodoro için uygulama şart mı?", "Hayır, mutfak zamanlayıcısı yeter. Uygulama, seansları kaydetmek, istatistik görmek ve arkadaşlarla birlikte çalışmak istiyorsan fark yaratır. Pomi bunları ücretsiz ve reklamsız sunar."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# 4) TR — Study with me / birlikte ders çalışma
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="study-with-me-birlikte-ders-calisma", lang="tr", pair="study-with-me-how-to-study-together",
  related=["pomi-nasil-kullanilir", "erteleme-aliskanligini-yenmek", "sinava-hazirlanirken-pomodoro"],
  section="Rehber", date=D, date_human=DH_TR, rfc822=RFC, read=5, words=950,
  title="Study With Me: Arkadaşlarınla Birlikte Ders Çalışmak Neden İşe Yarar?",
  short="Study with me rehberi",
  h1="Study with me: birlikte ders çalışmak neden <span class=\"accent\">işe yarar</span>?",
  lead="YouTube'daki saatlik sessiz çalışma videolarından Discord odalarına, oradan uygulamalara. Sosyal odaklanmanın arkasındaki mekanizma ve evde nasıl kuracağın.",
  desc="Study with me nedir, neden işe yarar? Sosyal kolaylaştırma ve body doubling etkisi, YouTube ve Discord ile uygulama karşılaştırması, Pomi odalarıyla arkadaşlarla uzaktan birlikte ders çalışma rehberi.",
  keywords="study with me, birlikte ders çalışma, body doubling, sosyal odaklanma, online kütüphane, arkadaşlarla ders çalışma uygulaması, odak odası",
  tldr="""<p><strong>Kısa cevap:</strong> Başkalarının çalıştığını görmek, beynin "şu an çalışma zamanı" sinyalini güçlendirir; buna <strong>body doubling</strong> ve sosyal kolaylaştırma denir. Bunu evde kurmanın en kolay yolu, arkadaşlarınla aynı anda bir odak odasına girip herkesin kendi sayacını çalıştırmasıdır. Kamera ya da mikrofon gerekmez.</p>""",
  body="""
<h2 id="nedir">Study with me nedir?</h2>
<p>"Study with me", birinin ders çalışırken kendini kaydedip yayınladığı, izleyenin de onunla aynı anda çalıştığı bir içerik türü olarak YouTube'da doğdu. Saatlerce süren, konuşmasız, çoğu zaman bir Pomodoro sayacı ve yağmur sesi eşliğinde çekilmiş videolar milyonlarca kez izleniyor. Pandemiyle birlikte Discord'da 7/24 açık "sessiz kütüphane" odalarına, oradan da doğrudan bu iş için tasarlanmış uygulamalara taşındı.</p>

<h2 id="neden">Neden işe yarıyor?</h2>
<ul>
  <li><strong>Body doubling.</strong> Yanında çalışan biri varken bir işe başlamak ve devam etmek kolaylaşır. Özellikle dikkat eksikliği olan kişilerde iyi belgelenmiş bir etki; ama herkeste çalışır.</li>
  <li><strong>Sosyal kolaylaştırma.</strong> Basit ve iyi bilinen görevlerde, izlendiğini bilmek performansı artırır. Ders tekrarı ve soru çözümü tam bu kategoriye girer.</li>
  <li><strong>Randevu etkisi.</strong> "Saat 9'da odada buluşuyoruz" demek, "bir ara çalışırım" demekten çok daha bağlayıcıdır.</li>
  <li><strong>Normalleştirme.</strong> Herkes çalışıyorsa çalışmak sıradan bir şeye dönüşür; erteleme için bahane azalır.</li>
</ul>

<h2 id="secenekler">Üç yol: YouTube, Discord, uygulama</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Yöntem</th><th>Artı</th><th>Eksi</th></tr></thead>
  <tbody>
    <tr><td>YouTube videosu</td><td>Sıfır kurulum, istediğin süre ve atmosferi seç</td><td>Tek yönlü; seni gören yok. Öneriler dikkat dağıtır.</td></tr>
    <tr><td>Discord sunucusu</td><td>Gerçek insanlar, canlı sohbet, büyük topluluklar</td><td>Sohbet dikkat dağıtır; kamera baskısı; kurulum ve moderasyon yükü.</td></tr>
    <tr><td>Odak uygulaması (Pomi)</td><td>Arkadaşlarınla özel oda, herkes kendi sayacıyla, ilerleme kaydı, telefonda</td><td>Uygulama yüklemek gerekir; topluluk Discord kadar büyük değil.</td></tr>
  </tbody>
</table>
</div>

<h2 id="pomi">Pomi odaları nasıl çalışır?</h2>
<p>Pomi'de bir oda oluşturursun, uygulama <strong>6 haneli bir davet kodu</strong> verir. Kodu arkadaşlarına gönderirsin; onlar da odaya girer. Odada herkesin ismini ve sayacını görürsün ama <strong>her kişi kendi sayacını başlatır</strong>. Ortak bir sayaç yoktur: biri 25 dakikalık seansı bitirip mola verdiğinde diğerlerinin seansı devam eder. Bu, "biri odadan çıkınca herkesin ağacı kurusun" tarzı yaklaşımların yarattığı gerginliği ortadan kaldırır.</p>
<p>Her tamamlanan seans hem kendi bahçene bir bitki ekler hem de <a href="../#conquest">fetih haritasında</a> şehrine puan yazar. Aynı şehirden arkadaşlar aynı odada çalışınca, şehrin bölge kazanması için birlikte çalışmış olursunuz.</p>
<p class="note sky">Kamera, mikrofon ve sohbet yok. Oda, "birlikte sessizce çalışıyoruz" hissini vermek için var; konuşmak için değil.</p>

<h2 id="kurallar">İyi bir study with me oturumu için 5 kural</h2>
<ol>
  <li><strong>Saat belirle ve paylaş.</strong> "Bu akşam 20:00, oda kodu ABC123." Randevu etkisi burada başlıyor.</li>
  <li><strong>Herkes kendi görevini önceden yazsın.</strong> Odaya girip ne çalışacağına karar vermek, ilk pomodoroyu yakar.</li>
  <li><strong>Molada konuşun, seansta konuşmayın.</strong> Sohbeti 5 dakikalık molaya sığdır.</li>
  <li><strong>En az 4 pomodoro hedefle.</strong> Tek seans, oda kurma zahmetine değmez; 2 saat bir çalışma bloğu eder.</li>
  <li><strong>Sonunda sayıları paylaşın.</strong> "Bugün 6 seans yaptım" cümlesi, yarın odaya geri dönmenin en güçlü nedeni.</li>
</ol>
<p>Hangi sayacı kullanacağına karar vermediysen <a href="en-iyi-pomodoro-uygulamalari-2026.html">Pomodoro uygulamaları karşılaştırmasına</a>, tekniğin temellerine ise <a href="pomodoro-teknigi-nedir.html">Pomodoro tekniği rehberine</a> göz at.</p>
""",
  faq=[
    ("Study with me ne demek?", "Birinin ders çalışırken yayın yapması ve izleyenlerin de aynı anda çalışması anlamına gelir. Zamanla Discord odalarına ve Pomi gibi arkadaşlarla aynı odada çalışmayı sağlayan uygulamalara taşındı."),
    ("Body doubling nedir?", "Bir işi yaparken yanında başka birinin bulunmasının başlama ve sürdürme kolaylığı sağlamasıdır. Dikkat eksikliği olan kişilerde özellikle etkilidir; sanal odalarda da aynı etki görülür."),
    ("Pomi odalarında ortak sayaç var mı?", "Hayır. Odada herkes kendi sayacını başlatır ve durdurur. Biri mola verdiğinde diğerlerinin seansı etkilenmez. Oda, birlikte çalışma hissini vermek için vardır."),
    ("Pomi odasına nasıl katılırım?", "Oda oluşturan kişi 6 haneli davet kodunu paylaşır. Uygulamada Odalar sekmesinden kodu girersin ve odaya katılırsın. Kamera veya mikrofon gerekmez."),
  ],
))
