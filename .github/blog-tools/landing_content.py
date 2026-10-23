# -*- coding: utf-8 -*-
"""Anahtar kelime açılış sayfaları: web Pomodoro sayacı ve online kütüphane (TR + EN).

Neden ayrı sayfalar: "pomodoro sayacı", "pomodoro timer", "online kütüphane",
"birlikte ders çalış", "study together online" gibi aramalarda Google bir araç ya
da o konuya ayrılmış bir sayfa gösteriyor; ana sayfa ve blog yazıları bu niyeti
karşılamıyordu. Her sayfada tarayıcıda çalışan sayaç (/assets/timer.js) var.

Kural: odalarda herkes kendi sayacıyla çalışır, ortak sayaç yoktur; odalar davet
koduyla açılır, yabancılarla eşleştirme yoktur. Metinlerde bunun dışına çıkma.

Üretim: python3 .github/blog-tools/build_blog.py (sayfalar <slug>/index.html'e yazılır).
Blog bağlantıları "../blog/<slug>.html", diğer açılış sayfaları "../<slug>/" biçiminde.
"""

TIMER_UI = {
    "tr": dict(
        heading="Pomodoro sayacı", modes="Sayaç modu",
        focus="Pomodoro", short="Kısa mola", long="Uzun mola",
        start="Başlat", pause="Duraklat", resume="Devam et", reset="Sıfırla", skip="Atla",
        ready="Hazır olduğunda başlat.", focusRun="Odak sürüyor", shortRun="Kısa mola", longRun="Uzun mola",
        paused="Duraklatıldı", doneFocus="Seans tamamlandı. Mola zamanı.", doneBreak="Mola bitti. Yeni seansa hazır mısın?",
        notifyTitle="Pomi", notifyFocus="25 dakika tamam. Biraz mola ver.", notifyBreak="Mola bitti, odak zamanı.",
        notifyDenied="Tarayıcı bildirimlere izin vermedi.",
        today="seans bugün", settings="Ayarlar",
        focusMin="Odak (dk)", shortMin="Kısa mola (dk)", longMin="Uzun mola (dk)", longEvery="Uzun mola her",
        noise="Arka plan sesi", noiseOff="Kapalı", noiseBrown="Kahverengi gürültü", noisePink="Pembe gürültü",
        auto="Sonraki aşamayı otomatik başlat", chime="Bitince sesli uyarı", notify="Bitince bildirim göster",
        hint="Kısayollar: <kbd>Boşluk</kbd> başlat/duraklat · <kbd>R</kbd> sıfırla. Ayarların yalnızca bu tarayıcıda saklanır.",
    ),
    "en": dict(
        heading="Pomodoro timer", modes="Timer mode",
        focus="Pomodoro", short="Short break", long="Long break",
        start="Start", pause="Pause", resume="Resume", reset="Reset", skip="Skip",
        ready="Start when you are ready.", focusRun="Focusing", shortRun="Short break", longRun="Long break",
        paused="Paused", doneFocus="Session complete. Time for a break.", doneBreak="Break is over. Ready for the next session?",
        notifyTitle="Pomi", notifyFocus="25 minutes done. Take a short break.", notifyBreak="Break is over, time to focus.",
        notifyDenied="Your browser blocked notifications.",
        today="sessions today", settings="Settings",
        focusMin="Focus (min)", shortMin="Short break (min)", longMin="Long break (min)", longEvery="Long break every",
        noise="Background sound", noiseOff="Off", noiseBrown="Brown noise", noisePink="Pink noise",
        auto="Auto-start the next phase", chime="Play a chime at the end", notify="Show a notification at the end",
        hint="Shortcuts: <kbd>Space</kbd> start/pause · <kbd>R</kbd> reset. Your settings stay in this browser only.",
    ),
}

PAGES = []

# ═══════════════════════════════════════════════════════════════════════
# 1) Online Pomodoro sayacı (TR)
# ═══════════════════════════════════════════════════════════════════════
PAGES.append(dict(
  slug="pomodoro-sayaci", lang="tr", pair="pomodoro-timer", nav="timer",
  modified="2026-10-23", modified_human="23 Ekim 2026",
  title="Online Pomodoro Sayacı: Ücretsiz, Reklamsız, Kayıtsız | Pomi",
  desc="Ücretsiz online Pomodoro sayacı: 25 dakika odak, 5 dakika mola, 4 seansta bir uzun mola. Kayıt ve reklam yok; sesli uyarı, bildirim ve kahverengi gürültüyle hemen başlat.",
  short="Pomodoro sayacı",
  kicker="Ücretsiz · Kayıt yok · Reklam yok",
  h1="Online <span class=\"accent\">Pomodoro</span> sayacı",
  lead="25 dakika odaklan, 5 dakika mola ver. Hesap açmadan, reklam görmeden tarayıcıda başlat. Telefonda devam etmek istersen her seans Pomi uygulamasında bahçene bir bitki olarak eklenir.",
  keywords="pomodoro sayacı, online pomodoro, pomodoro timer, pomodoro zamanlayıcı, ders çalışma sayacı, 25 dakika sayaç, odak sayacı, pomi, pomifocus",
  webapp=dict(
    name="Pomi Online Pomodoro Sayacı",
    description="Tarayıcıda çalışan ücretsiz Pomodoro sayacı: 25/5 odak-mola döngüsü, uzun mola, ayarlanabilir süreler, sesli uyarı, bildirim ve arka plan gürültüsü.",
    features=["25/5/15 dakikalık klasik Pomodoro döngüsü", "Ayarlanabilir odak ve mola süreleri", "Her 4 seansta bir otomatik uzun mola",
              "Sekme başlığında kalan süre", "Sesli uyarı ve masaüstü bildirimi", "Kahverengi ve pembe gürültü",
              "Klavye kısayolları", "Hesap ve reklam yok"],
  ),
  howto=dict(name="Pomodoro sayacı nasıl kullanılır?", steps=[
    ("Tek bir görev seç", "Bu seansta yapacağın tek işi yaz: 'biyoloji 3. ünite özeti' gibi somut olsun."),
    ("25 dakikalık sayacı başlat", "Başlat'a bas ve sayaç bitene kadar yalnızca o işle uğraş. Aklına gelen başka işleri bir kenara not et."),
    ("5 dakika mola ver", "Sayaç bitince kalk, su iç, gözlerini dinlendir. Telefona dalmamaya çalış."),
    ("Dört seansta bir uzun mola", "Dördüncü Pomodoro'dan sonra 15-30 dakikalık uzun mola ver, sonra döngüyü yeniden başlat."),
  ]),
  tldr="""<p>Bu sayfadaki <strong>online Pomodoro sayacı</strong> ücretsizdir; kayıt, reklam ya da indirme gerektirmez. Varsayılan döngü <strong>25 dakika odak, 5 dakika kısa mola ve her 4 seansta bir 15 dakika uzun mola</strong>dır; süreleri Ayarlar'dan değiştirebilirsin. Kalan süre sekme başlığında görünür, süre dolunca sesli uyarı ve istersen bildirim gelir. Telefonda kullanmak, seanslarını kaydetmek ve arkadaşlarınla birlikte çalışmak için <a href="../">Pomi uygulaması</a> var.</p>""",
  body="""<h2 id="nasil">Pomodoro sayacı nasıl kullanılır?</h2>
<p>Pomodoro tekniği, 1980'lerin sonunda Francesco Cirillo'nun domates biçimli bir mutfak sayacıyla geliştirdiği bir zaman yönetimi yöntemidir. Fikir basit: işi kısa ve sabit aralıklara bölersin, her aralığın sonunda mola verirsin. Sayacı şöyle kullan:</p>
<ol>
  <li><strong>Tek bir görev seç.</strong> "Ders çalışmak" değil, "fizik 4. bölümden 20 soru" gibi somut bir iş.</li>
  <li><strong>25 dakikalık sayacı başlat.</strong> Sayaç bitene kadar yalnızca o işle uğraş; aklına gelen başka işleri bir kâğıda not et.</li>
  <li><strong>5 dakika mola ver.</strong> Kalk, su iç, pencereden bak. Mola sayacı otomatik başlayabilir (Ayarlar → otomatik başlat).</li>
  <li><strong>Dört Pomodoro'da bir uzun mola.</strong> Dördüncü seanstan sonra 15-30 dakika ara ver; sayaç bunu kendisi önerir.</li>
</ol>
<p>Tekniğin ayrıntılarını, sık yapılan hataları ve öğrenciler için uyarlamaları <a href="../blog/pomodoro-teknigi-nedir.html">Pomodoro tekniği nedir</a> rehberinde anlattık.</p>

<h2 id="ozellikler">Bu sayaçta neler var?</h2>
<ul>
  <li><strong>Klasik ve özel süreler:</strong> 25/5/15 varsayılan; odak 1-180, mola 1-90 dakika arasında ayarlanır.</li>
  <li><strong>Sekmede kalan süre:</strong> Başka sekmede çalışırken başlıkta "18:42 · Odak" gibi kalan süreyi görürsün.</li>
  <li><strong>Sesli uyarı ve bildirim:</strong> Süre dolunca kısa bir zil çalar; izin verirsen masaüstü bildirimi de gelir.</li>
  <li><strong>Arka plan sesi:</strong> Kahverengi ya da pembe gürültüyü tarayıcı kendisi üretir; ayrı bir video ya da uygulama açmana gerek kalmaz. Hangi sesin hangi işe uyduğunu <a href="../blog/odaklanmak-icin-en-iyi-sesler.html">odak sesleri karşılaştırmasında</a> yazdık.</li>
  <li><strong>Gizlilik:</strong> Hesap yok, çerez yok. Ayarların ve bugünkü seans sayın yalnızca senin tarayıcında saklanır.</li>
  <li><strong>Doğru zaman:</strong> Sayaç saniye saymak yerine bitiş saatini hesaplar; sekme arka planda kalsa da süre kaymaz.</li>
</ul>

<h2 id="sureler">Hangi süreleri seçmeliyim?</h2>
<p>25/5 bir başlangıç noktası, kural değil. İşin türüne göre şu düzenler sık kullanılır:</p>
<div class="table-wrap"><table>
  <thead><tr><th>Düzen</th><th>Odak / mola</th><th>Kimin için</th></tr></thead>
  <tbody>
    <tr><td>Klasik Pomodoro</td><td>25 dk / 5 dk, 4 seansta bir 15-30 dk</td><td>Başlarken, soru çözerken, tekrar yaparken</td></tr>
    <tr><td>Kısa döngü</td><td>15 dk / 3 dk</td><td>Başlamakta zorlananlar, dikkati çabuk dağılanlar</td></tr>
    <tr><td>Uzun blok</td><td>50 dk / 10 dk</td><td>Kod, yazı, konu anlatımı gibi derin işler</td></tr>
    <tr><td>52/17</td><td>52 dk / 17 dk</td><td>Uzun mola isteyen, gün boyu çalışanlar</td></tr>
  </tbody>
</table></div>
<p>Farkları ve hangisinin hangi işe uyduğunu <a href="../blog/pomodoro-mu-flowtime-mi-52-17-odak-teknikleri.html">Pomodoro, 52/17 ve Flowtime karşılaştırmasında</a>, günlük hedefi ise <a href="../blog/gunde-kac-pomodoro-yapmali.html">günde kaç Pomodoro yapmalı</a> yazısında bulabilirsin.</p>

<h2 id="uygulama">Web sayacı mı, Pomodoro uygulaması mı?</h2>
<p>Bilgisayar başındaysan bu sayfa yeter. Telefonla çalışıyorsan ya da düzenli bir alışkanlık kurmak istiyorsan bir uygulama daha çok işe yarar:</p>
<div class="table-wrap"><table>
  <thead><tr><th></th><th>Bu web sayacı</th><th>Pomi uygulaması</th></tr></thead>
  <tbody>
    <tr><td>Fiyat</td><td>Ücretsiz</td><td>Ücretsiz (isteğe bağlı Pomi Pro)</td></tr>
    <tr><td>Reklam</td><td>Yok</td><td>Yok</td></tr>
    <tr><td>Sekme/uygulama kapanınca</td><td>Sayaç durur</td><td>Sayaç devam eder</td></tr>
    <tr><td>Seans kaydı</td><td>Yalnızca bugünkü sayı</td><td>Haftalık istatistik, görevler</td></tr>
    <tr><td>Ödül</td><td>—</td><td>Her seans piksel bahçende bir bitki</td></tr>
    <tr><td>Birlikte çalışma</td><td>—</td><td>Arkadaşlarla canlı odalar, herkes kendi sayacıyla</td></tr>
    <tr><td>Rekabet</td><td>—</td><td>Şehirlerin yarıştığı fetih haritası, haftalık lig</td></tr>
  </tbody>
</table></div>
<p class="note mint">Arkadaşlarınla aynı anda ders çalışmak istiyorsan <a href="../online-kutuphane/">online kütüphane</a> sayfasına bak: Pomi odalarında herkes kendi sayacıyla, aynı odada çalışır.</p>""",
  faq=[
    ("Online Pomodoro sayacı ücretsiz mi?", "Evet. Sayaç tamamen ücretsizdir; kayıt, reklam ya da indirme gerektirmez. Ayarların yalnızca kendi tarayıcında saklanır."),
    ("Sekmeyi kapatırsam sayaç durur mu?", "Evet, sekme kapanınca sayaç durur. Sekme açık kaldığı sürece başka sekmede çalışsan da süre doğru ilerler. Uygulama kapalıyken de çalışan bir sayaç istersen Pomi'yi telefona indirebilirsin."),
    ("Pomodoro neden 25 dakika?", "Francesco Cirillo, 25 dakikayı yorulmadan tam dikkat verilebilecek ve molayı hak ettirecek kadar uzun bir aralık olarak seçti. Kesin bir bilimsel sınır değildir; 15 ya da 50 dakika sana daha uygunsa Ayarlar'dan değiştir."),
    ("Kaç Pomodoro'dan sonra uzun mola verilir?", "Klasik yöntemde dört Pomodoro'dan sonra 15-30 dakikalık uzun mola verilir. Bu sayaçta bu sayı varsayılan olarak 4'tür ve Ayarlar'dan değiştirilebilir."),
    ("Telefonda kullanabileceğim bir Pomodoro uygulaması var mı?", "Pomi, iPhone ve Android için ücretsiz bir Pomodoro uygulamasıdır. Her tamamlanan seans piksel bahçene bir bitki ekler; arkadaşlarınla canlı odalarda birlikte çalışabilir, şehrin için fetih haritasında yarışabilirsin. Reklam yoktur."),
  ],
  cta_h="Seanslarını telefonda biriktir",
  cta_p="Pomi'de her 25 dakika bahçene bir bitki ekler, sayaç uygulama kapalıyken de çalışır. Ücretsiz, reklamsız; iPhone, iPad ve Android'de.",
  related=["pomodoro-teknigi-nedir", "gunde-kac-pomodoro-yapmali", "en-iyi-pomodoro-uygulamalari-2026"],
))

# ═══════════════════════════════════════════════════════════════════════
# 2) Online Pomodoro timer (EN)
# ═══════════════════════════════════════════════════════════════════════
PAGES.append(dict(
  slug="pomodoro-timer", lang="en", pair="pomodoro-sayaci", nav="timer",
  modified="2026-10-23", modified_human="October 23, 2026",
  title="Free Online Pomodoro Timer: No Ads, No Sign-up | Pomi",
  desc="A free online Pomodoro timer: 25 minutes of focus, 5-minute breaks and a long break every 4 sessions. No sign-up, no ads; chime, notifications and brown noise built in.",
  short="Pomodoro timer",
  kicker="Free · No sign-up · No ads",
  h1="Online <span class=\"accent\">Pomodoro</span> timer",
  lead="Focus for 25 minutes, rest for 5. Start right in your browser with no account and no ads. If you want to keep going on your phone, every session in the Pomi app grows a plant in your garden.",
  keywords="pomodoro timer, online pomodoro timer, pomodoro app, focus timer, study timer, 25 minute timer, tomato timer, pomi, pomifocus",
  webapp=dict(
    name="Pomi Online Pomodoro Timer",
    description="A free browser-based Pomodoro timer: 25/5 focus and break cycle, long breaks, custom lengths, chime, desktop notifications and background noise.",
    features=["Classic 25/5/15 minute Pomodoro cycle", "Custom focus and break lengths", "Automatic long break every 4 sessions",
              "Time left shown in the tab title", "Chime and desktop notifications", "Brown and pink noise",
              "Keyboard shortcuts", "No account and no ads"],
  ),
  howto=dict(name="How to use a Pomodoro timer", steps=[
    ("Pick one task", "Write down the single thing you will do in this session, and make it concrete, such as 'summarise chapter 3'."),
    ("Start the 25-minute timer", "Press Start and work only on that task until the timer ends. Jot down anything else that pops into your head."),
    ("Take a 5-minute break", "When the timer ends, stand up, drink water and rest your eyes. Try to stay off your phone."),
    ("Take a long break every four sessions", "After the fourth Pomodoro, take a 15 to 30-minute break, then start the cycle again."),
  ]),
  tldr="""<p>This <strong>online Pomodoro timer</strong> is free and needs no sign-up, ads or download. The default cycle is <strong>25 minutes of focus, a 5-minute short break and a 15-minute long break every 4 sessions</strong>; you can change every length in Settings. The time left shows in the tab title, and a chime (and, if you allow it, a notification) tells you when time is up. To use it on your phone, keep a record of your sessions and study together with friends, there is the <a href="../en/">Pomi app</a>.</p>""",
  body="""<h2 id="how">How to use the Pomodoro timer</h2>
<p>The Pomodoro Technique is a time-management method Francesco Cirillo developed in the late 1980s with a tomato-shaped kitchen timer. The idea is simple: you split work into short, fixed intervals and take a break after each one. Use the timer like this:</p>
<ol>
  <li><strong>Pick one task.</strong> Not "study", but something concrete such as "20 physics problems from chapter 4".</li>
  <li><strong>Start the 25-minute timer.</strong> Work only on that task until it ends; write any other thoughts on a piece of paper.</li>
  <li><strong>Take a 5-minute break.</strong> Stand up, drink water, look out of the window. The break can start automatically (Settings → auto-start).</li>
  <li><strong>Take a long break every four Pomodoros.</strong> After the fourth session, rest for 15 to 30 minutes; the timer suggests it for you.</li>
</ol>
<p>Common mistakes and ways to adapt the method are in our guide <a href="../blog/what-is-the-pomodoro-technique.html">What is the Pomodoro Technique?</a></p>

<h2 id="features">What this timer does</h2>
<ul>
  <li><strong>Classic and custom lengths:</strong> 25/5/15 by default; focus from 1 to 180 minutes, breaks from 1 to 90.</li>
  <li><strong>Time left in the tab:</strong> While you work in another tab, the title shows something like "18:42 · Focus".</li>
  <li><strong>Chime and notifications:</strong> A short chime plays when time is up; allow notifications to get a desktop alert as well.</li>
  <li><strong>Background sound:</strong> Brown or pink noise generated by the browser itself, so you do not need a separate video or app. Our <a href="../blog/best-background-sounds-for-studying.html">background sounds comparison</a> explains which sound suits which task.</li>
  <li><strong>Privacy:</strong> No account and no cookies. Your settings and today's session count stay in your browser.</li>
  <li><strong>Accurate time:</strong> The timer tracks the end time instead of counting seconds, so it does not drift when the tab is in the background.</li>
</ul>

<h2 id="lengths">Which lengths should I use?</h2>
<p>25/5 is a starting point, not a rule. These patterns are common depending on the kind of work:</p>
<div class="table-wrap"><table>
  <thead><tr><th>Pattern</th><th>Focus / break</th><th>Good for</th></tr></thead>
  <tbody>
    <tr><td>Classic Pomodoro</td><td>25 min / 5 min, 15-30 min every 4 sessions</td><td>Getting started, practice questions, revision</td></tr>
    <tr><td>Short cycle</td><td>15 min / 3 min</td><td>People who struggle to start or get distracted quickly</td></tr>
    <tr><td>Long block</td><td>50 min / 10 min</td><td>Deep work such as coding, writing or learning new material</td></tr>
    <tr><td>52/17</td><td>52 min / 17 min</td><td>Long days where you want longer breaks</td></tr>
  </tbody>
</table></div>
<p>The trade-offs are covered in <a href="../blog/pomodoro-vs-flowtime-vs-52-17.html">Pomodoro vs 52/17 vs Flowtime</a>, and daily targets in <a href="../blog/how-many-pomodoros-a-day.html">How many Pomodoros a day?</a></p>

<h2 id="app">Web timer or Pomodoro app?</h2>
<p>If you are at your computer, this page is enough. If you study on your phone or want to build a habit, an app does more:</p>
<div class="table-wrap"><table>
  <thead><tr><th></th><th>This web timer</th><th>Pomi app</th></tr></thead>
  <tbody>
    <tr><td>Price</td><td>Free</td><td>Free (optional Pomi Pro)</td></tr>
    <tr><td>Ads</td><td>None</td><td>None</td></tr>
    <tr><td>When the tab/app closes</td><td>Timer stops</td><td>Timer keeps running</td></tr>
    <tr><td>Session history</td><td>Today's count only</td><td>Weekly stats, tasks</td></tr>
    <tr><td>Reward</td><td>—</td><td>Every session grows a plant in your pixel garden</td></tr>
    <tr><td>Studying together</td><td>—</td><td>Live rooms with friends, each on their own timer</td></tr>
    <tr><td>Competition</td><td>—</td><td>Conquest map where cities compete, weekly league</td></tr>
  </tbody>
</table></div>
<p class="note mint">Want to study at the same time as your friends? See <a href="../study-together/">Study together online</a>: in Pomi rooms everyone works in the same room, each on their own timer.</p>""",
  faq=[
    ("Is this online Pomodoro timer free?", "Yes. The timer is completely free and needs no sign-up, ads or download. Your settings are stored only in your own browser."),
    ("Does the timer stop if I close the tab?", "Yes, closing the tab stops the timer. As long as the tab stays open, time stays accurate even while you work in another tab. If you want a timer that keeps running when the app is closed, you can install Pomi on your phone."),
    ("Why is a Pomodoro 25 minutes?", "Francesco Cirillo chose 25 minutes as long enough to make real progress and earn a break, yet short enough to keep full attention. It is not a scientific limit; if 15 or 50 minutes suits you better, change it in Settings."),
    ("After how many Pomodoros do you take a long break?", "In the classic method you take a 15 to 30-minute long break after four Pomodoros. This timer uses 4 by default, and you can change it in Settings."),
    ("Is there a Pomodoro app for my phone?", "Pomi is a free Pomodoro app for iPhone and Android. Every completed session grows a plant in your pixel garden, you can study with friends in live rooms and compete for your city on a conquest map. It has no ads."),
  ],
  cta_h="Keep your sessions on your phone",
  cta_p="In Pomi every 25 minutes grows a plant in your garden, and the timer keeps running when the app is closed. Free and ad-free on iPhone, iPad and Android.",
  related=["what-is-the-pomodoro-technique", "how-many-pomodoros-a-day", "best-pomodoro-apps-2026"],
))

# ═══════════════════════════════════════════════════════════════════════
# 3) Online kütüphane: birlikte ders çalış (TR)
# ═══════════════════════════════════════════════════════════════════════
PAGES.append(dict(
  slug="online-kutuphane", lang="tr", pair="study-together", nav="",
  modified="2026-10-23", modified_human="23 Ekim 2026",
  title="Online Kütüphane: Arkadaşlarınla Birlikte Ders Çalış | Pomi",
  desc="Online kütüphane ve online ders çalışma: Pomi'de arkadaşlarınla aynı odada, herkes kendi Pomodoro sayacıyla birlikte çalışır. Kamera ve mikrofon gerekmez. Ücretsiz.",
  short="Online kütüphane",
  kicker="Birlikte çalış · Online ders çalışma",
  h1="Online kütüphane: <span class=\"accent\">birlikte</span> ders çalış",
  lead="Kütüphanede seni masada tutan şey sessizlik değil, etrafında çalışan insanlardır. Pomi bu hissi telefona taşır: arkadaşlarınla aynı odaya gir, herkes kendi sayacıyla çalışsın.",
  keywords="online kütüphane, sanal kütüphane, birlikte ders çalış, birlikte çalış, online ders çalış, online ders çalışma, arkadaşlarla ders çalışma uygulaması, study with me, pomi, pomifocus",
  howto=dict(name="Pomi'de arkadaşlarınla online kütüphane nasıl kurulur?", steps=[
    ("Oda oluştur", "Pomi'de odalar bölümünden yeni bir oda oluştur; uygulama 6 haneli bir davet kodu verir."),
    ("Kodu paylaş", "Davet kodunu arkadaşlarına, sınıf ya da çalışma grubuna gönder; kodu giren aynı odaya katılır."),
    ("Herkes kendi seansını başlatsın", "Ortak sayaç yoktur: herkes kendi Pomodoro sayacını başlatır, molasını kendi verir."),
    ("Birbirini gör, sessizce çalış", "Odada kimin çalıştığını görürsün; kamera ve mikrofon gerekmez, molada oda sohbetinden yazışılabilir. Tamamlanan seanslar herkesin kendi bahçesine eklenir."),
  ]),
  tldr="""<p><strong>Online kütüphane</strong>, insanların aynı anda, birbirinin çalıştığını bilerek ama konuşmadan ders çalıştığı sanal ortamdır. <a href="../">Pomi</a>'de 6 haneli davet koduyla bir oda açıp arkadaşlarınla <strong>birlikte ders çalışabilirsin</strong>: herkes aynı odada ama <strong>kendi Pomodoro sayacıyla</strong> çalışır, kamera ve mikrofon gerekmez, uygulama ücretsizdir. Hemen başlamak istersen yukarıdaki online sayaç tarayıcında çalışır.</p>""",
  body="""<h2 id="nedir">Online kütüphane nedir, neden işe yarar?</h2>
<p>Online kütüphane (sanal kütüphane), evde tek başına ders çalışırken kütüphane ortamını yeniden kurma çabasıdır: aynı saatte çalışan başka insanlar, sessizlik ve belirli çalışma blokları. YouTube'daki "study with me" yayınları, Discord çalışma sunucuları ve kameralı Zoom odaları bu fikrin farklı biçimleri.</p>
<p>İşe yaramasının iki bilinen nedeni var. Birincisi <strong>sosyal kolaylaştırma</strong>: psikolojide, başkalarının yanında basit ve alışılmış işlerde daha istekli çalıştığımız uzun süredir gözlemleniyor. İkincisi <strong>body doubling</strong>: yanında sessizce çalışan birinin varlığı işe başlama eşiğini düşürür; özellikle erteleme ve dikkat sorunu yaşayanlar bunu sık anlatır. Ayrıntıları ve araştırmaları <a href="../blog/study-with-me-birlikte-ders-calisma.html">study with me rehberinde</a> topladık.</p>

<h2 id="pomi">Pomi'de birlikte ders çalışmak nasıl olur?</h2>
<ol>
  <li><strong>Oda oluştur.</strong> Pomi'de yeni bir oda aç; uygulama 6 haneli bir davet kodu verir.</li>
  <li><strong>Kodu paylaş.</strong> Kodu arkadaşlarına, sınıf grubuna ya da çalışma ekibine gönder; kodu giren odaya katılır.</li>
  <li><strong>Herkes kendi seansını başlatsın.</strong> Odada ortak sayaç yoktur. Biri mola verince diğerlerinin seansı bozulmaz; herkes kendi temposunda çalışır.</li>
  <li><strong>Birbirini gör, sessizce çalış.</strong> Odada kimlerin çalıştığını görürsün; kamera ya da mikrofon açmana gerek yok. Molada oda sohbetinden yazışabilirsin.</li>
  <li><strong>Emeğin görünür olsun.</strong> Tamamlanan her seans kendi piksel bahçene bir bitki ekler ve şehrinin fetih haritasındaki puanına yazılır.</li>
</ol>
<p class="note">Pomi'deki odalar davet koduyla açılır; tanımadığın kişilerle otomatik eşleştirme yoktur. Çalışma grubun yoksa sınıf ya da kurs arkadaşlarına kodu göndererek başlayabilirsin. Tek başına çalışırken de şehrin için fetih haritasında puan toplarsın; yalnız ama bir takımın parçası olarak.</p>

<h2 id="karsilastirma">Online ders çalışma yöntemleri karşılaştırması</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Yöntem</th><th>Kiminle</th><th>Kamera</th><th>Sayaç</th><th>Dikkat riski</th></tr></thead>
  <tbody>
    <tr><td>YouTube "study with me"</td><td>Yayıncıyla tek yönlü</td><td>Gerekmez</td><td>Yayının sayacı</td><td>Öneriler ve yorumlar dikkat dağıtabilir</td></tr>
    <tr><td>Discord çalışma sunucusu</td><td>Büyük topluluk, çoğu yabancı</td><td>İsteğe bağlı</td><td>Bot ya da ayrı uygulama</td><td>Sohbet kanalları açık</td></tr>
    <tr><td>Zoom / Meet kütüphanesi</td><td>Davet edilen grup</td><td>Genelde açık</td><td>Ayrı uygulama</td><td>Kamera yorgunluğu</td></tr>
    <tr><td>Pomi odaları</td><td>Davet kodu verdiğin arkadaşlar</td><td>Gerekmez</td><td>Herkes kendi sayacıyla, uygulamada</td><td>Düşük: yalnızca davet ettiğin kişiler, oda sohbeti yalnızca üyelere açık</td></tr>
  </tbody>
</table></div>
<p>Hiçbiri tek doğru değil: büyük bir toplulukta yabancılarla çalışmak istiyorsan Discord, arka planda birinin varlığı yetiyorsa YouTube, tanıdığın insanlarla düzenli ve sessiz bir çalışma saati istiyorsan Pomi odaları uygun.</p>

<h2 id="kurallar">Online ders çalışırken verimli olmak için 6 kural</h2>
<ul>
  <li><strong>Saati önceden belirle.</strong> "Akşam bakarız" yerine "20:00'de odadayız" de. Sabit saat, kütüphaneye gitmek kadar bağlayıcı olur.</li>
  <li><strong>Her seansa tek görev.</strong> Seansa başlamadan ne yapacağını yaz; odadakiler değil, görevin seni yönetsin.</li>
  <li><strong>Telefonu sadece sayaç için kullan.</strong> Bildirimleri kapat; telefonu bırakmanın yollarını <a href="../blog/ders-calisirken-telefonu-birakmak.html">bu yazıda</a> anlattık.</li>
  <li><strong>Molaları ayrı ver.</strong> Ortak sayaç olmadığı için kimseyi beklemeden molanı ver, döndüğünde odadakiler hâlâ orada.</li>
  <li><strong>Sohbeti molaya sakla.</strong> Online kütüphanenin değeri sessizliğinde; oda sohbetini molada kullan, seans sırasında bildirimleri sustur.</li>
  <li><strong>Sınav dönemlerinde düzenli kal.</strong> Uzun hazırlık dönemleri için <a href="../blog/sinava-hazirlanirken-pomodoro.html">sınava hazırlanırken Pomodoro</a> planına bak.</li>
</ul>

<h2 id="bilgisayar">Bilgisayardan da birlikte çalışabilir miyim?</h2>
<p>Pomi odaları iPhone ve Android uygulamasında çalışır. Bilgisayar başındaysan bu sayfadaki <a href="../pomodoro-sayaci/">online Pomodoro sayacını</a> kullanabilirsin; ancak web sayacı odaya bağlanmaz, seanslarını kaydetmez. Arkadaşlarınla aynı odada görünmek için telefonda Pomi'yi aç, çalışmayı bilgisayarda sürdür.</p>""",
  faq=[
    ("Online kütüphane nedir?", "Online kütüphane, insanların aynı saatte, birbirinin çalıştığını bilerek ama konuşmadan ders çalıştığı sanal ortamdır. YouTube study with me yayınları, Discord sunucuları, kameralı görüntülü görüşmeler ve Pomi gibi uygulamalardaki odalar bu amaçla kullanılır."),
    ("Pomi'de online kütüphane ücretsiz mi?", "Evet. Pomi ücretsiz indirilir ve oda kurup arkadaşlarınla birlikte çalışmak için ödeme gerekmez. Reklam yoktur; isteğe bağlı bir Pomi Pro aboneliği vardır."),
    ("Birlikte ders çalışırken kamera ya da mikrofon açmam gerekiyor mu?", "Hayır. Pomi odalarında kamera ya da mikrofon gerekmez; odada kimlerin çalıştığını görürsün, herkes kendi sayacıyla sessizce çalışır. İstersen molada oda sohbetinden yazışabilirsin."),
    ("Pomi odalarında ortak bir sayaç var mı?", "Hayır. Herkes aynı odada ama kendi Pomodoro sayacıyla çalışır. Biri mola verdiğinde ya da seansı bitirdiğinde diğerlerinin seansı devam eder."),
    ("Tanımadığım kişilerle birlikte çalışabilir miyim?", "Pomi'deki odalar 6 haneli davet koduyla açılır; tanımadığın kişilerle otomatik eşleştirme yoktur. Kodu paylaştığın herkes odaya katılabilir."),
    ("Bilgisayardan Pomi odasına katılabilir miyim?", "Pomi odaları iPhone ve Android uygulamasında çalışır. Bilgisayarda pomifocus.com'daki online Pomodoro sayacını kullanabilirsin, ancak bu sayaç odaya bağlanmaz."),
  ],
  cta_h="Arkadaşlarınla ilk odanı aç",
  cta_p="Pomi'yi indir, bir oda oluştur ve 6 haneli kodu arkadaşlarına gönder. Ücretsiz, reklamsız; iPhone, iPad ve Android'de.",
  related=["study-with-me-birlikte-ders-calisma", "sinava-hazirlanirken-pomodoro", "verimli-ders-calisma-teknikleri"],
))

# ═══════════════════════════════════════════════════════════════════════
# 4) Study together online (EN)
# ═══════════════════════════════════════════════════════════════════════
PAGES.append(dict(
  slug="study-together", lang="en", pair="online-kutuphane", nav="",
  modified="2026-10-23", modified_human="October 23, 2026",
  title="Study Together Online: A Virtual Library With Friends | Pomi",
  desc="Study together online in a virtual library: in Pomi rooms you and your friends work in the same room, each on their own Pomodoro timer. No camera or mic. Free.",
  short="Study together",
  kicker="Virtual library · Study with friends",
  h1="Study <span class=\"accent\">together</span> online",
  lead="What keeps you at your desk in a library is not the silence, it is the people working around you. Pomi brings that feeling to your phone: join the same room as your friends, and everyone works on their own timer.",
  keywords="study together online, virtual library, online study room, study with friends app, study with me app, body doubling app, co-working, pomi, pomifocus",
  howto=dict(name="How to set up a virtual library with friends in Pomi", steps=[
    ("Create a room", "In Pomi, create a new room; the app gives you a 6-character invite code."),
    ("Share the code", "Send the invite code to your friends, class or study group; anyone who enters it joins the same room."),
    ("Everyone starts their own session", "There is no shared timer: each person starts their own Pomodoro and takes breaks on their own schedule."),
    ("See each other, work in silence", "You can see who is in the room; no camera or microphone needed, and the room chat is there for breaks. Finished sessions grow plants in each person's own garden."),
  ]),
  tldr="""<p>A <strong>virtual library</strong> is an online space where people study at the same time, aware of each other but without talking. In <a href="../en/">Pomi</a> you can open a room with a 6-character invite code and <strong>study together with friends</strong>: everyone is in the same room but on <strong>their own Pomodoro timer</strong>, no camera or microphone is needed, and the app is free. To start right now, the online timer above runs in your browser.</p>""",
  body="""<h2 id="what">What is a virtual library, and why does it work?</h2>
<p>A virtual library (or online study room) recreates the library feeling when you study alone at home: other people working at the same time, silence and fixed work blocks. YouTube "study with me" streams, Discord study servers and camera-on Zoom rooms are all versions of the same idea.</p>
<p>Two well-known effects explain why it works. The first is <strong>social facilitation</strong>: psychologists have long observed that we work more readily on simple, familiar tasks when others are around. The second is <strong>body doubling</strong>: someone quietly working next to you lowers the barrier to getting started, which people who struggle with procrastination and attention often describe. We gathered the details and research in our guide <a href="../blog/study-with-me-how-to-study-together.html">Study with me: why studying together works</a>.</p>

<h2 id="pomi">How studying together works in Pomi</h2>
<ol>
  <li><strong>Create a room.</strong> Open a new room in Pomi; the app gives you a 6-character invite code.</li>
  <li><strong>Share the code.</strong> Send it to friends, your class group or your team; anyone who enters it joins the room.</li>
  <li><strong>Everyone starts their own session.</strong> There is no shared timer. When one person takes a break, nobody else's session is interrupted.</li>
  <li><strong>See each other, work in silence.</strong> You can see who is working in the room; no camera or microphone needed. On breaks, you can message each other in the room chat.</li>
  <li><strong>Make your effort visible.</strong> Every finished session grows a plant in your own pixel garden and scores points for your city on the conquest map.</li>
</ol>
<p class="note">Pomi rooms are opened with an invite code; there is no automatic matching with strangers. If you do not have a study group yet, start by sending the code to classmates. Even when you study alone, your sessions score points for your city on the conquest map, so you are still part of a team.</p>

<h2 id="compare">Ways to study together online, compared</h2>
<div class="table-wrap"><table>
  <thead><tr><th>Option</th><th>Who with</th><th>Camera</th><th>Timer</th><th>Distraction risk</th></tr></thead>
  <tbody>
    <tr><td>YouTube "study with me"</td><td>One-way, with the streamer</td><td>Not needed</td><td>The stream's timer</td><td>Recommendations and comments</td></tr>
    <tr><td>Discord study server</td><td>Large community, mostly strangers</td><td>Optional</td><td>Bot or separate app</td><td>Chat channels are always open</td></tr>
    <tr><td>Zoom / Meet library</td><td>Invited group</td><td>Usually on</td><td>Separate app</td><td>Camera fatigue</td></tr>
    <tr><td>Pomi rooms</td><td>Friends you give the invite code to</td><td>Not needed</td><td>Everyone on their own timer, in the app</td><td>Low: only people you invite, room chat visible to members only</td></tr>
  </tbody>
</table></div>
<p>None of them is the single right answer: Discord suits you if you want to study with strangers in a big community, YouTube if a background presence is enough, and Pomi rooms if you want a regular, quiet study hour with people you know.</p>

<h2 id="rules">6 rules for productive online study sessions</h2>
<ul>
  <li><strong>Set the time in advance.</strong> Say "we are in the room at 8 pm" instead of "let's see tonight". A fixed time is as binding as walking to the library.</li>
  <li><strong>One task per session.</strong> Write down what you will do before you start; let your task, not the room, run the session.</li>
  <li><strong>Use your phone only for the timer.</strong> Turn off notifications; we listed ways to do that in <a href="../blog/how-to-stop-checking-your-phone-while-studying.html">How to stop checking your phone while studying</a>.</li>
  <li><strong>Take breaks independently.</strong> With no shared timer, you rest when you need to and the others are still there when you return.</li>
  <li><strong>Save chat for breaks.</strong> A virtual library is valuable because it is quiet; use the room chat on breaks and mute it during a session.</li>
  <li><strong>Pair it with good study methods.</strong> A timer decides when you work; <a href="../blog/evidence-based-study-techniques.html">evidence-based study techniques</a> decide how.</li>
</ul>

<h2 id="desktop">Can I study together from my computer?</h2>
<p>Pomi rooms run in the iPhone and Android app. At your computer you can use the <a href="../pomodoro-timer/">online Pomodoro timer</a> on this site, but the web timer does not join a room or save your sessions. To appear in the room with your friends, open Pomi on your phone and keep working on your computer.</p>""",
  faq=[
    ("What is a virtual library?", "A virtual library is an online space where people study at the same time, aware of each other but without talking. YouTube study with me streams, Discord servers, video calls and rooms in apps like Pomi are used for this."),
    ("Is studying together in Pomi free?", "Yes. Pomi is free to download, and creating a room to study with friends does not require payment. There are no ads; an optional Pomi Pro subscription is available."),
    ("Do I need to turn on my camera or microphone?", "No. Pomi rooms do not need a camera or microphone; you see who is working in the room and everyone works quietly on their own timer. You can message each other in the room chat on breaks."),
    ("Is there a shared timer in Pomi rooms?", "No. Everyone is in the same room but on their own Pomodoro timer. When someone takes a break or finishes a session, everyone else keeps going."),
    ("Can I study with strangers?", "Pomi rooms are opened with a 6-character invite code; there is no automatic matching with strangers. Anyone you share the code with can join the room."),
    ("Can I join a Pomi room from my computer?", "Pomi rooms run in the iPhone and Android app. On a computer you can use the online Pomodoro timer at pomifocus.com, but that timer does not connect to a room."),
  ],
  cta_h="Open your first room with friends",
  cta_p="Download Pomi, create a room and send the 6-character code to your friends. Free and ad-free on iPhone, iPad and Android.",
  related=["study-with-me-how-to-study-together", "evidence-based-study-techniques", "how-to-stop-checking-your-phone-while-studying"],
))
