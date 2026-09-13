# -*- coding: utf-8 -*-
"""English posts. Each is the pair of a Turkish post (hreflang-linked)."""

IOS = "https://apps.apple.com/tr/app/id6784132034"
ANDROID = "https://play.google.com/store/apps/details?id=com.yakupselimucar.pomi"
SITE = "https://yakupselimucar.github.io/pomi-legal/"
D = "2026-09-13"
DH = "September 13, 2026"
RFC = "Sun, 13 Sep 2026 11:30:00 +0300"

POSTS = []

# ─────────────────────────────────────────────────────────────────
# What is the Pomodoro Technique?
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="what-is-the-pomodoro-technique", lang="en", pair="pomodoro-teknigi-nedir",
  section="Basics", date=D, date_human=DH, rfc822=RFC, read=6, words=1100,
  related=["pomodoro-vs-flowtime-vs-52-17", "how-many-pomodoros-a-day", "best-pomodoro-apps-2026"],
  title="What Is the Pomodoro Technique and How Do You Use It? (Step-by-Step Guide)",
  short="What is the Pomodoro Technique",
  h1="What is the <span class=\"accent\">Pomodoro Technique</span>, and how do you use it?",
  lead="Work 25 minutes, rest 5. Where the technique comes from, why it works, the mistakes almost everyone makes, and how to adapt the timings to yourself.",
  desc="What is the Pomodoro Technique and how does it work? The 25/5 cycle, the long-break rule, Francesco Cirillo's original method, common mistakes and how students and remote workers can adapt the timings.",
  keywords="what is the pomodoro technique, pomodoro technique explained, how to use pomodoro, 25 minute work technique, pomodoro method, focus techniques, time management for students",
  tldr="""<p><strong>Short answer:</strong> The Pomodoro Technique splits work into <strong>25-minute blocks of uninterrupted focus</strong> followed by <strong>5-minute breaks</strong>. After four blocks you take a longer break of 15 to 30 minutes. Francesco Cirillo developed it in the late 1980s and named it after the tomato-shaped kitchen timer he used; <em>pomodoro</em> is Italian for tomato.</p>""",
  body="""
<h2 id="what">What is the Pomodoro Technique?</h2>
<p>In the late 1980s, university student Francesco Cirillo could not get himself to study. He grabbed a tomato-shaped mechanical kitchen timer and asked himself whether he could focus for just ten minutes. The method settled into 25-minute blocks over time and became one of the most widely used time management techniques in the world.</p>
<p>The core idea fits in one sentence: <strong>manage attention, not time.</strong> Twenty-five minutes is short enough to start without resistance and has a clear end, so you stop before you burn out.</p>

<h2 id="steps">How to use the Pomodoro Technique in 6 steps</h2>
<ol>
  <li><strong>Pick one task.</strong> Make it concrete: not "study maths" but "derivative problem set, pages 40 to 48".</li>
  <li><strong>Set a timer for 25 minutes.</strong> A kitchen timer, your phone, or a Pomodoro app such as <a href="%s">Pomi</a>.</li>
  <li><strong>Work on that task only until the timer rings.</strong> Write down anything else that pops into your head and come back to it later.</li>
  <li><strong>Stop when the timer rings.</strong> Even mid-sentence. This is the hardest and most important rule.</li>
  <li><strong>Take a 5-minute break.</strong> Away from screens: drink water, walk, look out of the window.</li>
  <li><strong>After four pomodoros, take a 15 to 30 minute break.</strong> Then start the cycle again.</li>
</ol>

<h2 id="why">Why does it work?</h2>
<ul>
  <li><strong>It lowers the cost of starting.</strong> "Three hours of studying" is intimidating; "25 minutes" is not. Once the timer is running, the hardest part is behind you.</li>
  <li><strong>It makes time visible.</strong> Once you know a page of problems takes two pomodoros, planning becomes realistic.</li>
  <li><strong>It forces breaks.</strong> Attention comes in waves, not a straight line. Regular short breaks reduce the mid-afternoon crash.</li>
  <li><strong>It measures interruptions.</strong> Count how many times a pomodoro gets broken and you see the real size of your distractions.</li>
</ul>

<h2 id="mistakes">The 5 most common mistakes</h2>
<ol>
  <li><strong>Checking your phone during the break.</strong> Five minutes becomes twenty and your attention resets. Keep breaks screen-free.</li>
  <li><strong>Working through the bell.</strong> "I'm in flow" turns into exhaustion two hours later. Start another pomodoro if you like, but do not skip the break.</li>
  <li><strong>Choosing a task that is too big.</strong> "Write my thesis" does not fit in one pomodoro. Break it into pieces that finish in one sitting.</li>
  <li><strong>Changing the durations constantly.</strong> Run the classic 25/5 for two weeks first, then adapt.</li>
  <li><strong>Relying on the timer alone.</strong> If notifications are on while the timer runs, the phone wins, not the timer. Turn on focus mode.</li>
</ol>

<h2 id="adapt">Adapting the durations</h2>
<p>25/5 is a starting point, not a sacred rule. Common variants:</p>
<div class="table-wrap">
<table>
  <thead><tr><th>Cycle</th><th>Who it suits</th></tr></thead>
  <tbody>
    <tr><td>15 / 3</td><td>People who struggle to start, ADHD, the first week</td></tr>
    <tr><td>25 / 5</td><td>The classic. Studying, problem sets, email</td></tr>
    <tr><td>50 / 10</td><td>Work that needs a warm-up: coding, writing, deep reading</td></tr>
    <tr><td>90 / 20</td><td>Close to the ultradian rhythm. Experienced users, long dives into one task</td></tr>
  </tbody>
</table>
</div>
<p>In Pomi you can change the work and break lengths in settings; whichever duration you pick, the plant in your garden grows when the session completes. We compared these cycles against Flowtime and 52/17 in a <a href="pomodoro-vs-flowtime-vs-52-17.html">separate article</a>.</p>

<h2 id="students">A note for students</h2>
<p>Do not use Pomodoro for practice exams; sit those under real exam timing. Use it for learning new material, reviewing and working through problem sets. If your friends study at the same time, opening a room in Pomi where everyone runs their own timer noticeably raises motivation; we explain why in the <a href="study-with-me-how-to-study-together.html">study with me article</a>.</p>
""" % SITE,
  faq=[
    ("How long is a pomodoro?", "The classic cycle is 25 minutes of work and a 5-minute break. After four cycles you take a longer break of 15 to 30 minutes. The durations can be adapted, for example to 15/3 or 50/10."),
    ("Who invented the Pomodoro Technique?", "Francesco Cirillo, in the late 1980s while he was a university student. The name comes from the tomato-shaped kitchen timer he used; pomodoro is Italian for tomato."),
    ("What should I do during a Pomodoro break?", "Stay away from screens: drink water, stand up, walk a few steps, look out of the window. A social media break stretches 5 minutes into 20 and resets your focus."),
    ("Is the Pomodoro Technique right for everyone?", "It suits most work, but long creative tasks that need flow may do better with 50/10 or 90/20 blocks. It should not be used for exam simulations, which need real exam timing."),
    ("Do I need an app for Pomodoro?", "No, a kitchen timer is enough. An app makes a difference if you want to log sessions, see statistics and study together with friends. Pomi offers those for free and without ads."),
  ],
  sources=[
    "Cirillo, F. (2018). <em>The Pomodoro Technique</em>. Currency.",
    "Ariga, A. &amp; Lleras, A. (2011). Brief and rare mental \"breaks\" keep you focused. <em>Cognition</em>, 118(3).",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Study with me
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="study-with-me-how-to-study-together", lang="en", pair="study-with-me-birlikte-ders-calisma",
  section="Guide", date=D, date_human=DH, rfc822=RFC, read=5, words=950,
  related=["how-to-stop-procrastinating", "best-pomodoro-apps-2026", "how-to-use-pomi"],
  title="Study With Me: Why Studying Together Works, and How to Do It Remotely",
  short="Study with me guide",
  h1="Study with me: why studying together <span class=\"accent\">works</span>",
  lead="From hour-long silent YouTube videos to Discord libraries to dedicated apps. The mechanism behind social focus, and how to set it up from home without a camera.",
  desc="What is study with me and why does it work? Body doubling and social facilitation explained, YouTube vs Discord vs apps compared, and how to study together remotely with Pomi rooms where everyone runs their own timer.",
  keywords="study with me, study together online, body doubling, virtual study room, focus room app, study with friends app, online library, coworking for students",
  tldr="""<p><strong>Short answer:</strong> Seeing other people work strengthens your brain's "this is work time" signal; psychologists call it <strong>body doubling</strong> and social facilitation. The easiest way to get it at home is to join a focus room with friends at the same time, each running their own timer. No camera or microphone needed.</p>""",
  body="""
<h2 id="what">What is "study with me"?</h2>
<p>"Study with me" started on YouTube as a video genre: someone films themselves studying, and viewers study alongside. The videos run for hours with no talking, usually with a Pomodoro timer and rain sounds, and rack up millions of views. During the pandemic the format moved to 24/7 "silent library" voice channels on Discord, and from there to apps designed specifically for it.</p>

<h2 id="why">Why does it work?</h2>
<ul>
  <li><strong>Body doubling.</strong> Starting and continuing a task is easier when someone else is working nearby. The effect is well documented in people with ADHD, but it works for almost everyone.</li>
  <li><strong>Social facilitation.</strong> Robert Zajonc showed in 1965 that the presence of others improves performance on simple, well-practised tasks. Reviewing and solving problem sets fall squarely in that category.</li>
  <li><strong>The appointment effect.</strong> "We meet in the room at 9" is far more binding than "I'll study at some point".</li>
  <li><strong>Normalisation.</strong> When everyone around you is working, working becomes the default, and excuses to procrastinate shrink.</li>
</ul>

<h2 id="options">Three ways: YouTube, Discord, app</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Method</th><th>Pros</th><th>Cons</th></tr></thead>
  <tbody>
    <tr><td>YouTube video</td><td>Zero setup; pick any length and atmosphere</td><td>One-way, nobody sees you; recommendations distract</td></tr>
    <tr><td>Discord server</td><td>Real people, live, large communities</td><td>Chat distracts; camera pressure; setup and moderation overhead</td></tr>
    <tr><td>Focus app (Pomi)</td><td>Private room with friends, everyone on their own timer, progress logged, on your phone</td><td>Requires installing an app; community smaller than Discord</td></tr>
  </tbody>
</table>
</div>

<h2 id="pomi">How Pomi rooms work</h2>
<p>You create a room in Pomi and the app gives you a <strong>6-character invite code</strong>. Send it to your friends and they join. In the room you see everyone's name and timer status, but <strong>each person starts their own timer</strong>. There is no shared countdown: when someone finishes their 25 minutes and takes a break, everyone else's session keeps running. That removes the tension of "if one person leaves, everyone's tree dies" designs.</p>
<p>Every completed session adds a plant to your own garden and scores points for your city on the <a href="../#conquest">conquest map</a>. Friends from the same city working in the same room are literally working together to win regions for their city.</p>
<p class="note sky">No camera, no microphone, no chat. The room exists to give the feeling of "we are quietly working together", not to talk.</p>

<h2 id="rules">5 rules for a good study-with-me session</h2>
<ol>
  <li><strong>Set a time and share it.</strong> "Tonight at 8, room code ABC123." The appointment effect starts here.</li>
  <li><strong>Everyone writes their task in advance.</strong> Deciding what to study after joining burns the first pomodoro.</li>
  <li><strong>Talk during breaks, not sessions.</strong> Fit the chat into the 5 minutes.</li>
  <li><strong>Aim for at least 4 pomodoros.</strong> One session is not worth setting up a room; two hours makes a real study block.</li>
  <li><strong>Share your numbers at the end.</strong> "I did 6 sessions today" is the strongest reason to come back tomorrow.</li>
</ol>
<p>If you have not chosen a timer yet, see the <a href="best-pomodoro-apps-2026.html">Pomodoro app comparison</a>; for the technique itself, the <a href="what-is-the-pomodoro-technique.html">Pomodoro guide</a>.</p>
""",
  faq=[
    ("What does study with me mean?", "It means someone streams or records themselves studying while viewers study at the same time. The format has since moved to Discord rooms and to apps like Pomi that let friends work in the same room, each on their own timer."),
    ("What is body doubling?", "The effect where having another person present while you work makes it easier to start and keep going. It is especially strong in people with ADHD and works in virtual rooms too."),
    ("Is there a shared timer in Pomi rooms?", "No. Everyone in a room starts and stops their own timer. When one person takes a break, nobody else's session is affected. The room exists to create the feeling of working together."),
    ("How do I join a Pomi room?", "The person who created the room shares a 6-character invite code. Enter it in the Rooms tab and you are in. No camera or microphone is required."),
  ],
  sources=[
    "Zajonc, R. B. (1965). Social facilitation. <em>Science</em>, 149(3681).",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Pomodoro vs Flowtime vs 52/17
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="pomodoro-vs-flowtime-vs-52-17", lang="en", pair="pomodoro-mu-flowtime-mi-52-17-odak-teknikleri",
  section="Comparison", date=D, date_human=DH, rfc822=RFC, read=7, words=1250,
  related=["what-is-the-pomodoro-technique", "how-many-pomodoros-a-day", "best-pomodoro-apps-2026"],
  title="Pomodoro vs 52/17 vs Flowtime: An Honest Comparison of Focus Techniques",
  short="Pomodoro vs 52/17 vs Flowtime",
  h1="Pomodoro, 52/17 or <span class=\"accent\">Flowtime</span>?",
  lead="Five popular focus techniques compared on the same questions: who they suit, which work they fit, and where they break down. By the end you can pick one.",
  desc="Pomodoro vs 52/17 vs Flowtime vs 90-minute ultradian blocks vs time blocking. The origin, strengths, weaknesses and ideal work type for each focus technique, plus how to combine them.",
  keywords="pomodoro alternatives, 52 17 rule, flowtime technique, focus techniques compared, time blocking vs pomodoro, ultradian rhythm work, deep work technique",
  tldr="""<p><strong>Short answer:</strong> If starting is your problem and the work splits into pieces, use <strong>Pomodoro (25/5)</strong>. If you spend long days at a computer, try <strong>52/17</strong>. If being interrupted mid-flow drives you mad, use <strong>Flowtime</strong>. For coding, writing and research that need a warm-up, <strong>90/20</strong>. If your calendar is busy, put <strong>time blocking</strong> on top of any of them. They are not mutually exclusive; most people run two at once.</p>""",
  body="""
<h2 id="why">Why the technique matters</h2>
<p>Every focus technique addresses the same two problems: <strong>failing to start</strong> and <strong>failing to keep going</strong>. They differ in how. Pomodoro makes starting easy with short, hard limits; Flowtime removes the limits to protect flow; 52/17 and 90/20 move the limit closer to the body's natural rhythm. The right one depends on which problem hurts you more.</p>

<h2 id="table">Five techniques in one table</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Technique</th><th>Cycle</th><th>Origin</th><th>Best for</th><th>Weak spot</th></tr></thead>
  <tbody>
    <tr><td>Pomodoro</td><td>25 min work / 5 min break, long break after 4</td><td>Francesco Cirillo, late 1980s</td><td>Studying, problem sets, email, tasks you dislike</td><td>The bell interrupts flow</td></tr>
    <tr><td>52/17</td><td>52 min work / 17 min break</td><td>DeskTime usage data, 2014</td><td>Office and computer work</td><td>52 minutes is long for beginners</td></tr>
    <tr><td>Flowtime</td><td>Work until you lose focus, log it, break proportionally</td><td>Zoë Read-Bivens, 2016</td><td>Creative work, coding, writing</td><td>Needs discipline; falls apart without logging</td></tr>
    <tr><td>90/20 (ultradian)</td><td>90 min work / 20 min break</td><td>Kleitman's sleep-cycle research</td><td>Deep reading, thesis, design</td><td>Only 3-4 blocks a day; fragile under interruption</td></tr>
    <tr><td>Time blocking</td><td>A calendar slot for every task</td><td>Popularised by Cal Newport</td><td>Days full of meetings and mixed tasks</td><td>Says nothing about what happens inside the block</td></tr>
  </tbody>
</table>
</div>

<h2 id="pomodoro">Pomodoro: 25 / 5</h2>
<p>Simple and strict: 25 minutes on one task, 5 minutes off, a 15 to 30 minute break after four rounds. You stop when the bell rings, even mid-sentence. The full method is in our <a href="what-is-the-pomodoro-technique.html">Pomodoro guide</a>.</p>
<ul>
  <li><strong>Strength:</strong> The lowest barrier to starting. Even on your least motivated day, 25 minutes is acceptable. Counting interruptions shows you the real size of your distractions.</li>
  <li><strong>Weakness:</strong> The bell rings at minute 20 just as you enter flow. Cirillo does this on purpose ("the break is sacred"), but for programmers and writers the rule can be expensive.</li>
  <li><strong>For:</strong> Students, procrastinators, people with ADHD, anyone whose work splits into small pieces.</li>
</ul>

<h2 id="52-17">52/17: what the data said</h2>
<p>In 2014 the time-tracking app DeskTime published that its most productive 10 percent of users worked for an average of <strong>52 minutes and then broke for 17</strong>. It is not a controlled experiment, just an observation from usage data, but the numbers make a sensible middle ground for office workers. The break is long enough that you actually leave the screen.</p>
<ul>
  <li><strong>Strength:</strong> Enough time to warm up, enough break to really rest.</li>
  <li><strong>Weakness:</strong> 52 uninterrupted minutes is hard if you are not used to it. If the 17 minutes go to social media the technique loses its point.</li>
  <li><strong>For:</strong> Full-day computer workers, people who find Pomodoro too choppy.</li>
</ul>

<h2 id="flowtime">Flowtime: no timer, but a log</h2>
<p>Proposed by Zoë Read-Bivens in 2016, Flowtime removes Pomodoro's most criticised rule: the forced interruption. You pick a task, note the start time, work until your attention drifts or you tire, and note the end time. The break is proportional to the work: 5 minutes for 25, 8 for 50, 15 for 90.</p>
<ul>
  <li><strong>Strength:</strong> Protects flow. Over time the log reveals your real focus span; most people discover they peak around 35 to 45 minutes.</li>
  <li><strong>Weakness:</strong> Without an external limit it is easy to fall into "just a bit more". Stop logging and the technique evaporates.</li>
  <li><strong>For:</strong> Experienced focusers, programmers, writers, designers.</li>
</ul>

<h2 id="90-20">90/20: the ultradian rhythm</h2>
<p>Sleep researcher Nathaniel Kleitman proposed that the 90-minute cycles of sleep continue as a rest-activity wave through the waking day. 90/20 tries to fit work to that wave. Anders Ericsson's study of expert violinists points the same way: the best students practised in blocks of roughly 90 minutes and rarely more than 4 hours a day in total.</p>
<ul>
  <li><strong>Strength:</strong> Allows a genuine dive into deep work.</li>
  <li><strong>Weakness:</strong> At most 3 to 4 blocks a day. Finding 90 uninterrupted minutes in an open office or a busy home is hard.</li>
  <li><strong>For:</strong> Thesis writers, researchers, anyone who can protect their mornings.</li>
</ul>

<h2 id="time-blocking">Time blocking: the calendar technique</h2>
<p>This is a planning method rather than a rhythm. At the start of the day, or the night before, you give every task a slot in your calendar: 9:00 to 10:30 report, 10:30 to 11:00 email, 11:00 to 12:30 code. It says nothing about what happens inside the block, so it pairs with Pomodoro or 52/17. On a meeting-heavy day it is the most realistic technique because it makes the gaps between meetings visible.</p>

<h2 id="combine">Combining techniques</h2>
<p>In practice people rarely stick to one. Three combinations that work:</p>
<ol>
  <li><strong>Block + Pomodoro:</strong> A 2-hour "study" block on the calendar with 4 pomodoros inside. The safest setup for students.</li>
  <li><strong>Warm up with Pomodoro, continue with Flowtime:</strong> Start the day with one 25; if you are in flow, switch the timer off and log the time. For reluctant mornings.</li>
  <li><strong>90/20 in the morning, 25/5 in the afternoon:</strong> Deep work while the mind is fresh, short rounds when energy drops.</li>
</ol>
<p>Pomi lets you set work and break lengths freely, so the same app runs 25/5, 52/17 or 90/20; the plant in your garden grows whenever a session completes. How many rounds a day is realistic is covered in a <a href="how-many-pomodoros-a-day.html">separate article</a>.</p>

<h2 id="choose">How to choose: three questions</h2>
<ul>
  <li><strong>Is my real problem starting?</strong> If yes, Pomodoro. Short limits break starting resistance.</li>
  <li><strong>Does being interrupted in flow make me angry?</strong> If yes, Flowtime or 90/20.</li>
  <li><strong>Is my day full of meetings and interruptions?</strong> If yes, time blocking first, Pomodoro in the gaps.</li>
</ul>
<p>Whichever you pick, run it unchanged for two weeks. Switching techniques can be the most sophisticated form of not working.</p>
""",
  faq=[
    ("What is the 52/17 rule?", "A schedule of 52 minutes of uninterrupted work followed by a 17-minute break. It was derived in 2014 from the average behaviour of the most productive users of the time-tracking app DeskTime; it is an observation from usage data rather than a controlled experiment."),
    ("What is the Flowtime technique?", "A method with no forced timer: you work until your attention drifts, log the start and end times, then take a break proportional to the time worked. Zoë Read-Bivens proposed it in 2016 to fix Pomodoro's problem of interrupting flow."),
    ("Is Pomodoro or Flowtime better?", "Pomodoro is better if you struggle to start and your work splits into pieces; Flowtime is better for creative work where interruptions are costly. Many people start with Pomodoro and move to Flowtime as they gain experience, or use both."),
    ("What is the 90-minute rule?", "A schedule of 90 minutes of work and 20 minutes of rest, derived from Kleitman's research on ultradian rhythms. It suits deep, long work, but you can only do three or four blocks a day."),
    ("Can I run 52/17 or 90/20 in Pomi?", "Yes. Work and break durations are adjustable in Pomi's settings. Whatever the length, a completed session adds a plant to your garden and scores points for your city."),
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
# How many pomodoros a day
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="how-many-pomodoros-a-day", lang="en", pair="gunde-kac-pomodoro-yapmali",
  section="Guide", date=D, date_human=DH, rfc822=RFC, read=6, words=1050,
  related=["what-is-the-pomodoro-technique", "pomodoro-vs-flowtime-vs-52-17", "evidence-based-study-techniques"],
  title="How Many Pomodoros a Day? Realistic Targets and the Mistake Everyone Makes",
  short="How many pomodoros a day",
  h1="How many <span class=\"accent\">pomodoros</span> a day?",
  lead="\"I did 16 pomodoros\" sounds impressive and is usually the wrong goal. Realistic numbers for students, workers and thesis writers, how to raise your count, and when to stop.",
  desc="How many pomodoros should you do per day? Realistic targets for students, full-time workers and remote workers, the 4-hour deep-work ceiling, a plan to raise your count gradually, and burnout warning signs.",
  keywords="how many pomodoros a day, pomodoro daily goal, how many pomodoros should i do, how many hours to study a day, deep work hours per day, focus time per day",
  tldr="""<p><strong>Short answer:</strong> If you are new, <strong>4 pomodoros a day</strong> (100 minutes of net focus) is a good target. Once it is a habit, the sustainable ceiling for most students and workers is <strong>8 to 12</strong>, which is 3.5 to 5 hours of real focus and more than most full office days contain. Sixteen or more is a recipe for burnout outside short bursts like exam week.</p>""",
  body="""
<h2 id="wrong-goal">Why "more is better" is wrong</h2>
<p>A pomodoro count measures <strong>input</strong>, not <strong>output</strong>. You can sit through eight sessions and solve nothing, or finish a topic in three. The number is still useful, because it is the one thing you can measure and compare with yourself over time.</p>
<p>The second problem: a pomodoro is not 25 minutes but <strong>30</strong>, once you include the break. With long breaks, 8 pomodoros take about 4.5 hours. Sixteen means 9 hours, with no room for meals, commuting, classes or meetings.</p>

<h2 id="numbers">How many for whom?</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Situation</th><th>Daily target</th><th>Net focus</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td>Beginner</td><td>3-4</td><td>75-100 min</td><td>For the first two weeks, aim for consistency, not count</td></tr>
    <tr><td>Student attending classes</td><td>4-6</td><td>100-150 min</td><td>Outside class hours; up to 8 at weekends</td></tr>
    <tr><td>Full-time exam prep</td><td>10-14</td><td>4-6 hours</td><td>For two to three month stretches; do not sustain 6 weeks without a rest day</td></tr>
    <tr><td>Full-time employee</td><td>6-8</td><td>2.5-3.5 hours</td><td>The rest of the day goes to meetings, email and shallow work</td></tr>
    <tr><td>Remote / freelance</td><td>8-10</td><td>3.5-4 hours</td><td>Fewer interruptions, so the ceiling is slightly higher</td></tr>
    <tr><td>Thesis, book, research</td><td>6-8 (long blocks)</td><td>3-4 hours</td><td>With 50/10 the count halves, the time stays the same</td></tr>
  </tbody>
</table>
</div>

<h2 id="ceiling">The 4-hour ceiling</h2>
<p>The upper limits in that table are not arbitrary. In the 1993 study that started the "10,000 hours" debate, Anders Ericsson found that the best violin students practised deliberately for no more than about 4 hours a day; longer sessions lowered quality. Observations of writers and mathematicians point the same way: in deep, attention-demanding work, 4 to 5 hours a day is the ceiling for most people. Beyond it, work either slides into shallow tasks or becomes a debt paid the next day.</p>
<p class="note">This is a ceiling for <em>intense focus</em>, not total work. Reading, review and editing can sit on top of it.</p>

<h2 id="raise">How to raise your count</h2>
<ol>
  <li><strong>Consistency first.</strong> Three pomodoros every day for two weeks. Not missing a day matters more than hitting eight.</li>
  <li><strong>Add one session a week.</strong> From 3 to 4, from 4 to 5. No jumps; a jump today means zero tomorrow.</li>
  <li><strong>Protect the morning block.</strong> Put the first four pomodoros in the earliest free hours. Anything added in the afternoon is a bonus.</li>
  <li><strong>Count interruptions.</strong> Cirillo's original method marks every interruption. The session count will not rise until the interruption count falls.</li>
  <li><strong>Keep the count visible.</strong> A tally on paper, an X on a calendar, or the garden in Pomi. Visible progress is the cheapest way to raise the number.</li>
</ol>

<h2 id="stop">When to stop</h2>
<p>Three signs you are borrowing from tomorrow: reading the same paragraph three times, reaching for your phone more often in breaks, and not remembering what you did at the end of a session. On a day like that, a walk instead of the sixth pomodoro saves the eight you will do tomorrow.</p>

<h2 id="weekly">Think weekly, not daily</h2>
<p>A daily target makes one bad day feel like failure. A weekly target is more forgiving: 30 pomodoros a week can be 4 one day and 8 the next. Pomi's weekly statistics and weekly league work on exactly this logic; they judge your week, not your day.</p>
""",
  faq=[
    ("How many pomodoros should I do a day?", "Three to four for beginners, eight to twelve for experienced users. Twelve pomodoros is about 5 hours of net focus, which is close to the daily ceiling for deep work."),
    ("How many hours is 8 pomodoros?", "About 4.5 hours including breaks. The net focus time is 8 × 25 = 200 minutes, or 3 hours and 20 minutes."),
    ("Is it possible to do 16 pomodoros a day?", "Possible for short periods, not sustainable. Sixteen pomodoros with breaks is 9 hours. Outside exceptions like exam week, more than 12 usually causes a productivity drop the next day."),
    ("How many hours should I study a day?", "For a student attending classes, 2 to 2.5 hours of net focus outside class (4 to 6 pomodoros) is enough. For full-time exam preparation, 4 to 6 hours of net focus is the upper limit, with the rest of the time going to review and lighter work."),
    ("How do I track my pomodoro count?", "A paper tally is the simplest. If you use an app, Pomi adds a plant to your garden for every completed session and shows the total in weekly statistics, so you can see progress without counting."),
  ],
  sources=[
    "Ericsson, K. A., Krampe, R. T. &amp; Tesch-Römer, C. (1993). The role of deliberate practice in the acquisition of expert performance. <em>Psychological Review</em>, 100(3).",
    "Cirillo, F. (2018). <em>The Pomodoro Technique</em>. Currency.",
    "Newport, C. (2016). <em>Deep Work</em>. Grand Central Publishing.",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Procrastination
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="how-to-stop-procrastinating", lang="en", pair="erteleme-aliskanligini-yenmek",
  section="Basics", date=D, date_human=DH, rfc822=RFC, read=7, words=1250,
  related=["what-is-the-pomodoro-technique", "study-with-me-how-to-study-together", "how-to-stop-checking-your-phone-while-studying"],
  title="How to Stop Procrastinating: Why We Do It and What Actually Works Today",
  short="How to stop procrastinating",
  h1="How to stop <span class=\"accent\">procrastinating</span>",
  lead="Procrastination is not a time management problem; it is an emotion management problem. That is what the research says, and the solutions that follow look nothing like \"be more disciplined\".",
  desc="Why do we procrastinate and how do we stop? The emotional root of procrastination according to research, the 2-minute rule, implementation intentions, Pomodoro and studying together: 7 methods you can use today.",
  keywords="how to stop procrastinating, why do i procrastinate, procrastination psychology, 2 minute rule, how to start studying, academic procrastination, motivation to study",
  tldr="""<p><strong>Short answer:</strong> Procrastination is not laziness; it is a short-term escape from an unpleasant feeling such as boredom, anxiety or self-doubt. So the fix is to shrink the feeling: <strong>make the task small enough to start in 2 minutes</strong>, <strong>write down when and where</strong> you will do it, <strong>set a 25-minute timer</strong>, and if possible <strong>work near other people</strong>. Once the first 5 minutes pass, half the feeling is gone.</p>""",
  body="""
<h2 id="what">What procrastination is, and is not</h2>
<p>Procrastination is voluntarily delaying a task even though you expect to be worse off for it. The key phrase is "even though you expect": there is no lack of information, and usually no lack of a plan. Piers Steel's 2007 meta-analysis of 691 studies found that 80 to 95 percent of university students procrastinate regularly and about half consider it a problem. Procrastination is the default, not the exception.</p>
<p>Steel found the strongest predictors of procrastination to be how <strong>unpleasant</strong> the task is, how <strong>distant</strong> the reward is, the person's <strong>impulsiveness</strong>, and low <strong>confidence</strong> in being able to do it. Time management skill sits near the bottom of the list.</p>

<h2 id="emotion">The real mechanism: short-term mood repair</h2>
<p>The framework proposed by Fuschia Sirois and Timothy Pychyl in 2013 is now the field's main model: procrastination is <strong>sacrificing your future self to fix how you feel right now</strong>. Opening the textbook creates boredom, anxiety or a sense of "I can't do this"; reaching for the phone relieves that instantly. The brain learns the loop. Guilt follows, and guilt drives more avoidance.</p>
<p>The practical consequence: "get angry at yourself and be disciplined" <strong>increases</strong> procrastination because it inflates the bad feeling. In a study by the same group, students who forgave themselves for procrastinating before a first exam procrastinated less before the second.</p>

<h2 id="methods">7 methods you can use today</h2>

<h3>1. Shrink the task to 2 minutes</h3>
<p>David Allen's rule, repurposed: instead of "study the chapter", "open the book and read the first heading". A two-minute task creates a small feeling, so the avoidance is small too. Continuing is far easier than starting.</p>

<h3>2. Write an implementation intention: when, where, what</h3>
<p>Peter Gollwitzer's research found that people who wrote plans in the form "in situation Y I will do Z" reached their goals two to three times more often than people who just set a goal. The sentence looks like this: <em>"Tomorrow at 9:00, at the kitchen table, I will open maths problem set page 40."</em> You move the decision from 9 a.m. tomorrow to tonight.</p>

<h3>3. Set a 25-minute timer</h3>
<p>Pomodoro works well against procrastination because the end is known in advance. "I'll study for three hours" is vague and frightening; "25 minutes, then I get up" is bearable. Once the timer starts, the hardest part, starting, is over. See the <a href="what-is-the-pomodoro-technique.html">Pomodoro guide</a>.</p>

<h3>4. Set up the environment in advance</h3>
<p>Reduce the start-up cost of the avoided task to zero: book open, notebook next to it, phone in another room, water on the desk. A desk prepared the night before removes five small decisions in the morning.</p>

<h3>5. Work near other people</h3>
<p>A library, a café, or an online focus room. Seeing someone else work lowers the starting threshold; it is called body doubling. Opening a room in Pomi with friends, each on their own timer, gives you that effect at home. The mechanism is explained in the <a href="study-with-me-how-to-study-together.html">study with me article</a>.</p>

<h3>6. Make progress visible</h3>
<p>One cause of procrastination is that the reward is far away. Fill the gap with small, visible rewards: an X on the calendar, a tally, a plant added to a garden for every finished session. The system does not matter; what matters is that today's work leaves a mark today.</p>

<h3>7. Forgive yourself, then go back to the 2 minutes</h3>
<p>This is a research finding, not a call to go easy. Every minute you spend angry at yourself for procrastinating feeds the feeling that procrastination runs on. "Yesterday didn't happen; I'm opening the book now" breaks the loop.</p>

<h2 id="chronic">When you need more than this</h2>
<p>If procrastination covers every area of life, has lasted months and includes sleep, relationships or health, it may sit on top of ADHD, depression or an anxiety disorder. The methods above still help but will not be enough on their own; talking to a professional is the shortest route.</p>

<h2 id="summary">One-sentence summary</h2>
<p>Because procrastination is about feelings, so is the fix: make the task small, decide in advance, limit the time, do not stay alone, and forgive yourself. All of it fits inside one 25-minute session.</p>
""",
  faq=[
    ("Why do I keep procrastinating?", "Research shows procrastination is a short-term escape from the unpleasant feeling a task creates, such as boredom, anxiety or self-doubt. It is an emotion regulation problem rather than laziness or poor time management, which is why criticising yourself makes it worse."),
    ("What is the fastest way to stop procrastinating?", "Shrink the task until it can be started in 2 minutes and set a 25-minute timer. Starting is the hardest part; continuing once the timer runs is comparatively easy."),
    ("What is the 2-minute rule?", "Reducing the start of a task to the smallest step that takes two minutes, such as \"open the book and read the first paragraph\". A small step creates a small feeling, so there is less to avoid."),
    ("Does the Pomodoro Technique help with procrastination?", "Yes, especially with the problem of starting. The fixed, short duration lowers starting resistance, and the mandatory breaks prevent burnout. Over the long run it works best combined with studying near others and visible progress."),
    ("Is procrastination a disorder?", "Not on its own; the large majority of students procrastinate regularly. If it covers every area of life, has lasted months and disrupts daily functioning, it may be linked to ADHD, depression or anxiety, and it is worth consulting a professional."),
  ],
  sources=[
    "Steel, P. (2007). The nature of procrastination: A meta-analytic and theoretical review of quintessential self-regulatory failure. <em>Psychological Bulletin</em>, 133(1).",
    "Sirois, F. &amp; Pychyl, T. (2013). Procrastination and the priority of short-term mood regulation: Consequences for future self. <em>Social and Personality Psychology Compass</em>, 7(2).",
    "Wohl, M. J. A., Pychyl, T. A. &amp; Bennett, S. H. (2010). I forgive myself, now I can study. <em>Personality and Individual Differences</em>, 48(7).",
    "Gollwitzer, P. M. (1999). Implementation intentions: Strong effects of simple plans. <em>American Psychologist</em>, 54(7).",
    "Allen, D. (2001). <em>Getting Things Done</em>. Viking.",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Background sounds
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="best-background-sounds-for-studying", lang="en", pair="odaklanmak-icin-en-iyi-sesler",
  section="Guide", date=D, date_human=DH, rfc822=RFC, read=6, words=1100,
  related=["best-focus-apps-for-students", "what-is-the-pomodoro-technique", "how-to-use-pomi"],
  title="The Best Background Sounds for Studying: Rain, Café, White Noise and Music Compared",
  short="Best background sounds for studying",
  h1="The best <span class=\"accent\">background sounds</span> for studying",
  lead="Silence, rain or lo-fi? The research is surprisingly clear: it depends on the task and on the sound. Which sound helps which work, and which one hurts.",
  desc="The best background sounds for studying and working: rain, café ambience, white, pink and brown noise, instrumental music and lo-fi compared. What research says about which sound suits which task.",
  keywords="best background sounds for studying, music while studying, white noise vs brown noise, rain sounds for focus, coffee shop sounds, lo-fi study, focus music, ambient noise concentration",
  tldr="""<p><strong>Short answer:</strong> For reading and writing, <strong>music with lyrics hurts</strong>; wordless, steady sounds (rain, brown noise, a low café murmur) are neutral or helpful. For mechanical work such as review and problem sets, music you like can boost motivation. The general rule: <strong>if the sound does not change, it stays in the background; if it changes, it pulls attention.</strong></p>""",
  body="""
<h2 id="why">Why sound works (or doesn't)</h2>
<p>Attention responds to change. In a quiet room, a creaking door, a neighbour's voice or a distant horn pulls you out every time. A steady background sound covers those changes; this is called <strong>masking</strong>. Rain works not because of a magic frequency but because it is predictable.</p>
<p>On the other hand, if the sound carries information, such as lyrics or intelligible speech, the language areas of your brain process it whether you want them to or not. That is why the same sound can help in one task and hurt in another.</p>

<h2 id="table">Sound types and the work they suit</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Sound</th><th>Reading / writing</th><th>Problem sets / review</th><th>Creative work</th><th>Note</th></tr></thead>
  <tbody>
    <tr><td>Total silence</td><td>Good (if the room is quiet)</td><td>Good</td><td>Fair</td><td>Can be the worst option in a noisy home</td></tr>
    <tr><td>Rain / nature</td><td>Very good</td><td>Good</td><td>Good</td><td>Steady, carries no information; the safest choice</td></tr>
    <tr><td>Café murmur</td><td>Good (if speech is unintelligible)</td><td>Good</td><td>Very good</td><td>Moderate noise can boost creativity</td></tr>
    <tr><td>White noise</td><td>Good</td><td>Good</td><td>Fair</td><td>Hissy; some people find it irritating</td></tr>
    <tr><td>Pink / brown noise</td><td>Very good</td><td>Good</td><td>Fair</td><td>Deeper, easier to listen to for long sessions</td></tr>
    <tr><td>Instrumental / lo-fi</td><td>Fair</td><td>Good</td><td>Good</td><td>Pick tracks with little change in tempo and dynamics</td></tr>
    <tr><td>Music with lyrics</td><td>Bad</td><td>Fair</td><td>Fair</td><td>Measurably lowers reading comprehension</td></tr>
    <tr><td>Podcast / video</td><td>Very bad</td><td>Bad</td><td>Bad</td><td>Both compete for language processing; one loses</td></tr>
  </tbody>
</table>
</div>

<h2 id="research">What the research says</h2>
<ul>
  <li><strong>Lyrics and reading:</strong> In Perham and Currie's 2014 study, participants listening to lyrical music they liked scored clearly lower on reading comprehension than those in silence or with instrumental music. Liking the song did not help.</li>
  <li><strong>Moderate noise and creativity:</strong> Mehta, Zhu and Cheema (2012) found that ambient noise around 70 decibels, roughly a busy café, improved creative problem solving compared with silence, while 85 decibels made it worse. This is the basis of the coffee-shop myth, and it is partly true.</li>
  <li><strong>White noise and attention:</strong> Söderlund and colleagues (2007) found white noise improved memory performance in children with attention difficulties but slightly reduced it in children without. The benefit depends on the person.</li>
  <li><strong>Masking:</strong> Open-office research consistently shows intelligible speech to be the most disruptive sound. When a steady background sound covers it, performance recovers.</li>
</ul>

<h2 id="colours">White, pink, brown: what's the difference?</h2>
<p>All three are random noise; the difference is how energy is spread across frequencies. <strong>White</strong> noise has equal power at every frequency and sounds hissy, like radio static. <strong>Pink</strong> noise turns down the highs and sounds like heavy rain. <strong>Brown</strong> noise goes deeper still, like a distant waterfall or an aircraft cabin. For long sessions most people find pink or brown less tiring; try each and decide.</p>

<h2 id="rules">5 rules for using sound well</h2>
<ol>
  <li><strong>Start the sound with the session, stop it with the break.</strong> Over time the sound becomes a "work time" signal; Pavlov works in your favour here.</li>
  <li><strong>Keep the volume low.</strong> The goal is to cover the environment, not to drown it. Stay below conversation level.</li>
  <li><strong>Do not fiddle with playlists.</strong> Every track choice is a decision and every decision costs attention. Pick one long sound or a mixed ambience.</li>
  <li><strong>Change the sound with the task.</strong> Rain for reading, lo-fi for problem sets, café for brainstorming.</li>
  <li><strong>Headphones are not always needed.</strong> Quiet rain from a speaker gives the same masking without ear fatigue.</li>
</ol>

<h2 id="pomi">Focus sounds in Pomi</h2>
<p>Pomi includes rain, café, forest and other sounds, and you can set each one's level separately and mix them: light rain over a distant café murmur, for example. The sounds run with the timer and stop when the session ends, so you never open another app to hunt for a playlist. For other tools, see the <a href="best-focus-apps-for-students.html">focus apps guide</a>.</p>
""",
  faq=[
    ("Is listening to music while studying bad?", "Music with lyrics measurably reduces comprehension in language-heavy tasks such as reading and writing. Instrumental, steady music or nature sounds are neutral or helpful for most people. For mechanical tasks such as problem sets, music you enjoy can improve motivation."),
    ("What is the best sound for concentration?", "There is no single answer, but the safest options are steady sounds that carry no information: rain, brown noise, an unintelligible café murmur. They mask sudden changes in the environment and reduce attention breaks."),
    ("What is the difference between white noise and brown noise?", "Both are random noise. White noise has equal power at all frequencies and sounds hissy; brown noise concentrates energy in low frequencies and sounds like a waterfall or an aircraft cabin. Most people find brown or pink noise more comfortable for long listening."),
    ("Why does café noise help some people focus?", "A moderate, steady murmur of around 70 decibels masks sudden sounds and, according to research, slightly improves creative thinking. If the conversations become intelligible, the effect reverses."),
    ("Is lo-fi music good for studying?", "Usually yes: it is wordless, repetitive and has little dynamic change, so it stays in the background. For reading-heavy work, completely information-free sounds such as rain or noise are still safer."),
  ],
  sources=[
    "Perham, N. &amp; Currie, H. (2014). Does listening to preferred music improve reading comprehension performance? <em>Applied Cognitive Psychology</em>, 28(2).",
    "Mehta, R., Zhu, R. &amp; Cheema, A. (2012). Is noise always bad? Exploring the effects of ambient noise on creative cognition. <em>Journal of Consumer Research</em>, 39(4).",
    "Söderlund, G., Sikström, S. &amp; Smart, A. (2007). Listen to the noise: Noise is beneficial for cognitive performance in ADHD. <em>Journal of Child Psychology and Psychiatry</em>, 48(8).",
    "Haapakangas, A., Hongisto, V. et al. (2014). Effects of five speech masking sounds on performance and acoustic satisfaction. <em>Acta Acustica united with Acustica</em>, 100(2).",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Phone while studying
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="how-to-stop-checking-your-phone-while-studying", lang="en", pair="ders-calisirken-telefonu-birakmak",
  section="Students", date=D, date_human=DH, rfc822=RFC, read=6, words=1100,
  related=["how-to-stop-procrastinating", "forest-app-alternatives", "what-is-the-pomodoro-technique"],
  title="How to Stop Checking Your Phone While Studying: 9 Ways That Don't Need Willpower",
  short="Stop checking your phone while studying",
  h1="How to stop <span class=\"accent\">checking your phone</span> while studying",
  lead="If the phone is on the desk, even face down and silent, part of your attention is on it. That is what the research says. Nine methods that change the environment instead of relying on willpower.",
  desc="How to stop checking your phone while studying: the mere-presence research, putting the phone in another room, greyscale, focus mode, notification settings, the break rule and Pomodoro. Nine practical methods.",
  keywords="stop checking phone while studying, phone distraction studying, how to focus without phone, phone addiction study, focus mode studying, greyscale phone, put phone away studying",
  tldr="""<p><strong>Short answer:</strong> Trust distance, not willpower. Put the phone <strong>in another room</strong>; if you can't, in a bag, face down. <strong>Silence notifications for the whole session</strong>, switch the screen to greyscale, move social apps off the home screen. Instead of banning the phone, <strong>move it to the break</strong> and cap it with a timer. Set these up once and you stop having to decide every day.</p>""",
  body="""
<h2 id="problem">The problem is not looking; it is the phone being there</h2>
<p>In a 2017 experiment with about 800 participants, Adrian Ward and colleagues at the University of Texas had people put their phones in one of three places: on the desk, in a pocket or bag, or in another room. All phones were silenced and nobody touched them. Even so, people whose phones were <strong>on the desk scored measurably lower on working memory and fluid intelligence tests</strong> than those whose phones were in another room. The researchers called it "brain drain": ignoring the phone costs attention continuously.</p>
<p>So deciding "I won't look" is not enough. If the phone is in view, the cost is already being paid. The fix is <strong>distance</strong>, not willpower.</p>

<h2 id="methods">9 methods, easiest first</h2>

<h3>1. Put it in another room</h3>
<p>The single most effective method. Having to get up and walk kills most of the urge. If someone else is home, hand it to them; handing over is more binding than locking.</p>

<h3>2. Get it out of sight</h3>
<p>If another room is not possible: in a bag, a drawer, or at least face down behind you. In Ward's experiment even a phone in a pocket beat one on the desk.</p>

<h3>3. No notifications for the whole session</h3>
<p>Focus mode on iPhone, Do Not Disturb on Android. Set it up once so it switches on automatically for your 25-minute sessions. You can allow calls from one or two people for emergencies; do not allow messaging apps.</p>

<h3>4. Switch to greyscale</h3>
<p>Colour is the strongest pull apps have. Turning on greyscale in accessibility settings makes the phone a boring device. Schedule it to switch on during study hours.</p>

<h3>5. Move social apps off the home screen</h3>
<p>No need to delete them. Move them to the second or third page inside a folder. Having to search for them breaks the "just a quick look" reflex; most opens are reflex, not decision.</p>

<h3>6. Don't ban the phone; move it to the break</h3>
<p>Bans grow desire. Make the rule: <strong>none during the session, allowed in the break, with a timer.</strong> Three of the five break minutes can go to the phone; when the timer rings, it goes down. This makes the 25 minutes more bearable.</p>

<h3>7. Keep the timer somewhere other than the phone screen</h3>
<p>If the timer lives on the phone, you have a perfect excuse to keep the phone on the desk. Use a kitchen timer, or start the app and turn the phone face down at a distance. Pomi's timer keeps counting with the screen off and the app in the background: start it, flip it, move it away.</p>

<h3>8. An interruption notebook</h3>
<p>When the urge to "quickly search this" or "message them" arrives mid-session, write it on paper. Writing it down usually dissolves the urge; if not, do it in the break. The least known and most useful rule in Cirillo's original method.</p>

<h3>9. Write your reason and stick it to the back of the phone</h3>
<p>It looks simple, but it works: "Med school in June." The one sentence you see when you pick the phone up. Occasionally that is enough.</p>

<h2 id="apps">How useful are blocking apps?</h2>
<p>Forest, Flora, Opal and similar apps gamify putting the phone down: leave the app and the tree dies, or apps lock. They work well in two situations: when the phone <strong>cannot go to another room</strong> (dorm, bus, studio flat) and when <strong>gamification motivates you</strong>. For most people, another room is both free and more effective. We compared the options in the <a href="forest-app-alternatives.html">Forest alternatives article</a>.</p>

<h2 id="pomi">Pomi's approach</h2>
<p>Pomi does not lock your phone; it is designed for you to start the timer and move the phone away. The plant added to your garden and the points scored for your city when the session ends are the visible reward for "25 minutes without looking". If you are in a room with friends, reaching for the phone while everyone's timers are running feels a little harder; social pressure works in your favour there.</p>

<h2 id="setup">A two-minute setup</h2>
<ol>
  <li>Create a focus mode that switches on automatically during study hours.</li>
  <li>Set up a greyscale shortcut.</li>
  <li>Move social apps into a folder.</li>
  <li>Put paper and a pen on the desk (interruption notebook).</li>
  <li>Next session, leave the phone in another room. Strange on day one, normal by day three.</li>
</ol>
""",
  faq=[
    ("Why is it hard to study with my phone on the desk?", "Research shows that a phone in view lowers working memory performance even when it is silent and face down. Ignoring it costs attention continuously. That is why the most effective fix is putting the phone in another room."),
    ("Should I turn my phone off completely while studying?", "Putting it in another room is usually enough and easier to sustain than switching it off. In focus mode you can allow calls from one or two people for emergencies; messaging apps should not be exceptions."),
    ("Do phone blocking apps work?", "Yes when you cannot move the phone to another room, or when gamification motivates you. For most people, physical distance is both free and more effective. Forest, Flora and Opal are the best-known examples of this category."),
    ("What if my Pomodoro timer is on my phone?", "Start the timer, then turn the phone face down and move it away. Apps like Pomi keep counting with the screen off and in the background. A kitchen timer or a watch works too."),
    ("Can I check my phone during the break?", "Yes, with a timer. At most three of the five break minutes should go to the phone, and it goes down when the timer rings. A ban during sessions plus limited permission in breaks keeps the rule sustainable."),
  ],
  sources=[
    "Ward, A. F., Duke, K., Gneezy, A. &amp; Bos, M. W. (2017). Brain Drain: The mere presence of one's own smartphone reduces available cognitive capacity. <em>Journal of the Association for Consumer Research</em>, 2(2).",
    "Thornton, B., Faires, A., Robbins, M. &amp; Rollins, E. (2014). The mere presence of a cell phone may be distracting. <em>Social Psychology</em>, 45(6).",
    "Cirillo, F. (2018). <em>The Pomodoro Technique</em>. Currency.",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Evidence-based study techniques
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="evidence-based-study-techniques", lang="en", pair="verimli-ders-calisma-teknikleri",
  section="Students", date=D, date_human=DH, rfc822=RFC, read=8, words=1450,
  related=["how-many-pomodoros-a-day", "what-is-the-pomodoro-technique", "best-focus-apps-for-students"],
  title="Evidence-Based Study Techniques: 7 Methods Research Shows Actually Work",
  short="Evidence-based study techniques",
  h1="Study techniques that <span class=\"accent\">actually work</span>: 7 methods backed by research",
  lead="Highlighting and re-reading are the two most common study methods, and both rank among the least effective. What 40 years of learning science recommends instead, and how to fit each method into a Pomodoro session.",
  desc="Scientifically proven study techniques: active recall, spaced repetition, interleaving, self-testing, the Feynman technique, Pomodoro and sleep. The research behind each one and how to apply it in 25 minutes.",
  keywords="evidence based study techniques, effective study methods, active recall, spaced repetition, interleaving, feynman technique, how to study effectively, learning science, retrieval practice",
  tldr="""<p><strong>Short answer:</strong> The two techniques with the strongest evidence are <strong>self-testing (active recall)</strong> and <strong>spaced repetition</strong>. Add <strong>interleaving</strong> (mixing topics) and <strong>explaining in your own words</strong> and retention climbs noticeably. Re-reading, highlighting and summarising are weak on their own. Pomodoro is the container: spend the last 3 minutes of every 25 recalling with the book closed.</p>""",
  body="""
<h2 id="source">Where this list comes from</h2>
<p>In 2013 John Dunlosky and colleagues evaluated the ten most common study techniques across hundreds of studies and rated each one high, moderate or low utility. The result is uncomfortable: the most used methods (re-reading, highlighting) scored <strong>low</strong>; the least used (self-testing, spacing) scored <strong>high</strong>. The list below is based on that review and the research since.</p>

<div class="table-wrap">
<table>
  <thead><tr><th>Technique</th><th>Strength of evidence</th><th>How often students use it</th></tr></thead>
  <tbody>
    <tr><td>Self-testing (active recall)</td><td>High</td><td>Rarely</td></tr>
    <tr><td>Spaced repetition</td><td>High</td><td>Rarely</td></tr>
    <tr><td>Interleaving</td><td>Moderate</td><td>Very rarely</td></tr>
    <tr><td>Self-explanation / Feynman</td><td>Moderate</td><td>Rarely</td></tr>
    <tr><td>Summarising</td><td>Low to moderate</td><td>Common</td></tr>
    <tr><td>Highlighting</td><td>Low</td><td>Very common</td></tr>
    <tr><td>Re-reading</td><td>Low</td><td>Most common</td></tr>
  </tbody>
</table>
</div>

<h2 id="1">1. Active recall: close the book and remember</h2>
<p><strong>What:</strong> Pulling information out of memory instead of reading it again. Solving problems, explaining with the book closed, writing on a blank page, writing your own questions.</p>
<p><strong>Evidence:</strong> In Roediger and Karpicke's 2006 experiment, students who read a passage four times remembered clearly less a week later than students who read it once and tried to recall it three times; and the re-readers <em>believed</em> they had learned more. The familiarity that re-reading creates gets mistaken for knowing.</p>
<p><strong>In 25 minutes:</strong> Study for 20, close the book and write what you remember for 3, check the gaps for 2. This single change raises study efficiency more than anything else.</p>

<h2 id="2">2. Spaced repetition: not all at once</h2>
<p><strong>What:</strong> Spreading three hours on a topic across three days instead of one sitting, then short reviews after 3 days, 1 week, 3 weeks.</p>
<p><strong>Evidence:</strong> Cepeda and colleagues' 2006 meta-analysis of 254 studies showed a consistent advantage of spaced over massed practice. The best gap depends on how far away the test is: for an exam a month out, about a week between reviews works well.</p>
<p><strong>Apply:</strong> Put a "Friday: review the week" block in your weekly plan. If you use flashcards, use a tool such as Anki that sets the gaps automatically.</p>

<h2 id="3">3. Interleaving: mix the topics</h2>
<p><strong>What:</strong> Mixing problems from different topics instead of solving 30 of the same kind in a row (blocked practice).</p>
<p><strong>Evidence:</strong> In Rohrer and Taylor's 2007 study, students who solved maths problems in mixed order made more errors during practice but scored roughly twice as high on a test a week later than students who practised in blocks. Mixing also trains the question "which method do I use here?", which is exactly what exams ask.</p>
<p><strong>Apply:</strong> In a problem-solving block, 30 mixed problems from three topics instead of 10 per topic. It feels uncomfortable; the difficulty is what works.</p>

<h2 id="4">4. The Feynman technique: explain it to a 12-year-old</h2>
<p><strong>What:</strong> Write or say the topic in plain language, in your own words, as if to someone who knows nothing. Where you get stuck is what you do not know.</p>
<p><strong>Evidence:</strong> "Self-explanation" earns moderate utility in Dunlosky's review; its real power is combining active recall with gap detection. What you cannot explain, you have not learned.</p>
<p><strong>In 25 minutes:</strong> Study a topic for 15, then write "I'm explaining this to a friend" on a blank page for 10. Mark the sentences where you stall; they are the topic of your next session.</p>

<h2 id="5">5. Pomodoro: the container</h2>
<p><strong>What:</strong> 25 minutes on one task, 5 minutes off. The full guide is <a href="what-is-the-pomodoro-technique.html">here</a>.</p>
<p><strong>Why it is on the list:</strong> Pomodoro is not a learning technique; it is an attention technique. But the four methods above demand attention, and Pomodoro slices attention into pieces. Put active recall in the last 3 minutes of every session and the session itself becomes a learning tool. In Pomi, linking each session to a task lets you see how many sessions each topic got, which makes spacing easier to plan.</p>

<h2 id="6">6. Sleep: free consolidation</h2>
<p><strong>What:</strong> 7 to 9 hours a night, including the night before the exam.</p>
<p><strong>Evidence:</strong> Most of the transfer of the day's learning into long-term memory happens during sleep, particularly in deep sleep and REM. The studies collected by Walker show that a sleepless night also cuts the next day's capacity to learn new material. Studying until 3 a.m. loses twice: what you studied does not consolidate, and you cannot learn tomorrow.</p>
<p><strong>Apply:</strong> Finish your last session an hour before bed and make it a review session; what comes right before sleep consolidates best.</p>

<h2 id="7">7. Studying together, if you do it right</h2>
<p><strong>What:</strong> Same time, same room, everyone on their own work. Not talking.</p>
<p><strong>Evidence:</strong> Social facilitation research has shown since the 1960s that the presence of others improves performance on well-practised tasks. Review and problem sets are exactly that. Details in the <a href="study-with-me-how-to-study-together.html">study with me article</a>.</p>
<p><strong>Apply:</strong> Three evenings a week, fixed time, 4 pomodoros. If you cannot meet in person, a room in Pomi: everyone joins on their own timer and talk waits for the break.</p>

<h2 id="combine">Fitting it all into one week</h2>
<ul>
  <li><strong>Every session:</strong> last 3 minutes recalling with the book closed (active recall).</li>
  <li><strong>Every problem block:</strong> topics mixed (interleaving).</li>
  <li><strong>Every day:</strong> one review session before bed (spacing + sleep).</li>
  <li><strong>Every week:</strong> Friday morning review of the week and one topic explained on a blank page (Feynman).</li>
  <li><strong>Three evenings a week:</strong> a room with friends (studying together).</li>
</ul>
<p>How many sessions a day is realistic for all this is covered in <a href="how-many-pomodoros-a-day.html">how many pomodoros a day</a>.</p>
""",
  faq=[
    ("What is the most effective study technique?", "The technique with the strongest research support is self-testing, also called active recall: retrieving information from memory with the book closed instead of re-reading. Spaced repetition comes second. Used together they produce the highest retention."),
    ("Why don't re-reading and highlighting work?", "Both are passive and create a feeling of familiarity; the more familiar the text feels, the more you think you know it, but you cannot retrieve it in an exam. In experiments, students who read four times remembered less than those who read once and recalled three times."),
    ("How do I do spaced repetition?", "Spread a topic across several days instead of one long sitting, then review briefly after 3 days, 1 week and 3 weeks. For an exam a month away, about a week between reviews works well. Flashcard apps set the gaps automatically."),
    ("What is the Feynman technique?", "Writing or saying a topic in plain words as if explaining it to someone who knows nothing. Where you get stuck is what you have not learned, and the next session focuses there. It combines active recall with finding gaps."),
    ("Does the Pomodoro Technique improve learning?", "On its own it is an attention technique, not a learning technique. But if you spend the last 3 minutes of every 25-minute session recalling with the book closed, the session becomes an active recall tool. In Pomi, linking sessions to tasks shows how much time each topic received."),
  ],
  sources=[
    "Dunlosky, J., Rawson, K. A., Marsh, E. J., Nathan, M. J. &amp; Willingham, D. T. (2013). Improving students' learning with effective learning techniques. <em>Psychological Science in the Public Interest</em>, 14(1).",
    "Roediger, H. L. &amp; Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. <em>Psychological Science</em>, 17(3).",
    "Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T. &amp; Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. <em>Psychological Bulletin</em>, 132(3).",
    "Rohrer, D. &amp; Taylor, K. (2007). The shuffling of mathematics problems improves learning. <em>Instructional Science</em>, 35(6).",
    "Walker, M. (2017). <em>Why We Sleep</em>. Scribner.",
    "Zajonc, R. B. (1965). Social facilitation. <em>Science</em>, 149(3681).",
  ],
))

# ─────────────────────────────────────────────────────────────────
# Forest alternatives
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="forest-app-alternatives", lang="en", pair="forest-alternatifi-ucretsiz-uygulamalar",
  section="Comparison", date=D, date_human=DH, rfc822=RFC, read=6, words=1100,
  related=["best-pomodoro-apps-2026", "how-to-stop-checking-your-phone-while-studying", "does-gamification-help-you-focus"],
  title="6 Free Forest App Alternatives for Focus (2026)",
  short="Forest app alternatives",
  h1="Looking for a <span class=\"accent\">Forest</span> alternative? 6 free apps",
  lead="Forest is paid on iOS and ad-supported on Android. Six apps that do the same job free and without ads, some adding more. Which one fits which need.",
  desc="Free alternatives to the Forest app: Pomi, Flora, Focus To-Do, Study Bunny, Focus Plant and Pomofocus compared on tree-planting mechanics, phone locking, studying together and ads.",
  keywords="forest app alternative, free forest app, apps like forest, tree planting focus app, flora vs forest, phone lock app free, free focus app no ads",
  itemlist=[("Pomi", SITE), ("Flora", "https://flora.appfinca.com/"), ("Focus To-Do", "https://www.focustodo.cn/"), ("Study Bunny", "https://apps.apple.com/app/id1219395424"), ("Focus Plant", "https://apps.apple.com/app/id1482938010"), ("Pomofocus", "https://pomofocus.io/")],
  tldr="""<p><strong>Short answer:</strong> Forest's <strong>closest free equivalent is Flora</strong>: the same tree mechanic, shared sessions with a friend. If you want a growing garden instead of trees, rooms with friends and a city competition, <strong>Pomi</strong>. If a task list matters most, <strong>Focus To-Do</strong>. On a computer, <strong>Pomofocus</strong>. None of them charge up front on iOS.</p>""",
  body="""
<h2 id="forest">Giving Forest its due first</h2>
<p>Forest is the app that grew the focus-app category. The mechanic is clever: start a session and you plant a sapling; leave the app during the session and it withers. Trees accumulate into a forest, and virtual coins can fund real tree planting. A browser extension covers the computer.</p>
<p>People look for alternatives for three reasons: it is <strong>paid on iOS</strong> (one-time), the <strong>free Android version has ads</strong>, and the mechanic is <strong>one-dimensional</strong>; the fear of killing a tree works for the first months, then you get used to it. Group planting, where one person leaving kills everyone's tree, also creates friction in some friend groups.</p>

<h2 id="table">Comparison</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>App</th><th>Mechanic</th><th>Free tier</th><th>Ads</th><th>Phone lock</th><th>Study together</th><th>Platforms</th></tr></thead>
  <tbody>
    <tr><td>Forest (reference)</td><td>Plant a tree; leave and it dies</td><td>Android yes, iOS no</td><td>In Android free tier</td><td>Yes (app permission)</td><td>Group tree; one break kills it for all</td><td>iOS, Android, browser</td></tr>
    <tr><td>Pomi</td><td>A plant per session in a garden; conquest map and league</td><td>Yes, full timer</td><td>None</td><td>No (encourages distance)</td><td>Rooms, everyone on their own timer</td><td>iOS, Android</td></tr>
    <tr><td>Flora</td><td>Plant a tree; leave and it dies</td><td>Yes</td><td>None</td><td>Yes</td><td>Shared tree; one break kills it for all</td><td>iOS, Android</td></tr>
    <tr><td>Focus To-Do</td><td>Timer + task manager</td><td>Yes</td><td>None</td><td>Partial</td><td>No</td><td>iOS, Android, desktop, web</td></tr>
    <tr><td>Study Bunny</td><td>Feed a bunny, earn coins</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>iOS, Android</td></tr>
    <tr><td>Focus Plant</td><td>Collect raindrops, grow plants</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Limited</td><td>iOS, Android</td></tr>
    <tr><td>Pomofocus</td><td>Plain web timer</td><td>Yes</td><td>Yes</td><td>No</td><td>No</td><td>Web</td></tr>
  </tbody>
</table>
</div>
<p class="note">Based on store listings as of September 2026. Prices and features change; check the store before downloading.</p>

<h2 id="apps">The apps, one by one</h2>

<div class="app-card">
  <h3>1. Flora <span class="tag">Closest substitute</span></h3>
  <p>Forest's mechanic, free and without ads. Plant a sapling, leave and it dies; start a shared session with a friend. There is also an optional mode where you pledge money to charity if you break the session. If all you want from Forest is the tree and the lock, the search ends here.</p>
  <dl><dt>Missing</dt><dd>Shallow statistics; no task management; in group sessions one person's break kills the tree for everyone.</dd></dl>
</div>

<div class="app-card ours">
  <h3>2. Pomi <span class="tag rose">Study together</span> <span class="tag">No ads</span></h3>
  <p>A garden instead of trees: every completed session adds a new plant to your pixel garden and the collection grows over time. Two core differences from Forest. First, in <strong>rooms</strong> everyone runs their own timer; when your friend takes a break your session is untouched, so there is no friction. Second, the <strong>conquest map</strong>: your focus minutes score points for your city, and 81 cities compete for regions in 7-day seasons. Tasks, mixable focus sounds and a weekly league round it out.</p>
  <dl>
    <dt>Best for</dt><dd>Students who study with friends; people motivated more by "let my garden grow" than by "don't let my tree die"</dd>
    <dt>Missing</dt><dd>Does not lock the phone (deliberately); no web or desktop version.</dd>
    <dt>Get it</dt><dd><a href="%s" rel="noopener">App Store</a> · <a href="%s" rel="noopener">Google Play</a></dd>
  </dl>
</div>

<div class="app-card">
  <h3>3. Focus To-Do <span class="tag sky">Task-focused</span></h3>
  <p>No gamification; instead a full task manager and sync across all devices. If you used Forest "to keep track of myself" and never cared about the trees, this is a better tool. The free tier is ad-free and generous.</p>
  <dl><dt>Missing</dt><dd>Busy interface; no motivation layer.</dd></dl>
</div>

<div class="app-card">
  <h3>4. Study Bunny <span class="tag sun">Character</span></h3>
  <p>A bunny you feed by studying, coins and a shop. Popular with high-school students. Cute and free, but ad-heavy and dated.</p>
  <dl><dt>Missing</dt><dd>Ads; no social features.</dd></dl>
</div>

<div class="app-card">
  <h3>5. Focus Plant <span class="tag">Tree mechanic</span></h3>
  <p>Visually the closest alternative to Forest: focusing collects raindrops, raindrops grow plants. Has a phone lock. The free tier shows ads.</p>
  <dl><dt>Missing</dt><dd>Ads; limited co-working.</dd></dl>
</div>

<div class="app-card">
  <h3>6. Pomofocus <span class="tag sky">Web</span></h3>
  <p>No install, no account, a plain timer in the browser. If you work at a computer and want a replacement for Forest's browser extension, it does the job.</p>
  <dl><dt>Missing</dt><dd>No mobile app; the timer stops when the tab closes; ads.</dd></dl>
</div>

<h2 id="lock">Do you actually need a phone lock?</h2>
<p>Forest's appeal is that it punishes you for leaving the app. That helps where you cannot put the phone in another room (dorm, bus, studio flat). But research shows that a phone lying on the desk lowers attention even when it is locked; a lock does not replace distance. That is why Pomi chose "start the timer, move the phone away" over locking. Details in the <a href="how-to-stop-checking-your-phone-while-studying.html">phone article</a>.</p>

<h2 id="choose">Which one?</h2>
<ul>
  <li><strong>I want Forest for free:</strong> Flora.</li>
  <li><strong>I study with friends and don't want friction:</strong> Pomi.</li>
  <li><strong>My task list matters:</strong> Focus To-Do.</li>
  <li><strong>I'm at a computer:</strong> Pomofocus.</li>
  <li><strong>I want a cute character:</strong> Study Bunny, or Pomi's plant collection.</li>
</ul>
<p>For a broader comparison see <a href="best-pomodoro-apps-2026.html">the best Pomodoro apps in 2026</a>. Whether gamification works at all is discussed in a <a href="does-gamification-help-you-focus.html">separate article</a>.</p>
""" % (IOS, ANDROID),
  faq=[
    ("Is there a free alternative to Forest?", "Yes. Flora offers the same tree-planting and phone-locking mechanic free and without ads. Pomi is also free and ad-free; instead of trees it adds a plant to your garden per session and adds rooms with friends and a city competition."),
    ("Why is Forest paid on iOS?", "The developer chose a one-time purchase model on iOS, with an ad-supported free version on Android. If you do not want to pay up front, Flora and Pomi offer free starts."),
    ("What is the difference between Flora and Forest?", "The mechanic is nearly identical: plant a sapling, leave and it dies, shared sessions with a friend. Flora is free and ad-free; Forest's browser extension and real-tree programme are not in Flora."),
    ("Does a focus app that doesn't lock the phone work?", "Yes, because research shows a phone in view lowers attention even when locked. Starting the timer and putting the phone in another room is more effective than a lock. Pomi is designed around that approach."),
    ("What does Forest have that Pomi doesn't?", "A phone lock, a browser extension and a real-tree planting programme. What Pomi has that Forest doesn't: rooms where everyone runs their own timer, a conquest map where 81 cities compete, a weekly league and mixable focus sounds."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# How to use Pomi
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="how-to-use-pomi", lang="en", pair="pomi-nasil-kullanilir",
  section="Pomi", date=D, date_human=DH, rfc822=RFC, read=7, words=1250,
  related=["study-with-me-how-to-study-together", "does-gamification-help-you-focus", "what-is-the-pomodoro-technique"],
  title="How to Use Pomi: A Beginner's Guide to the Garden, Rooms, Conquest Map and League",
  short="How to use Pomi",
  h1="How to use <span class=\"accent\">Pomi</span>: a beginner's guide",
  lead="From your first session to your first plant, from your first room to the first region you win for your city. What every part of Pomi does, how to set it up, and which settings to change.",
  desc="Pomi user guide: starting your first Pomodoro session, adding tasks, the pixel garden and plant collection, creating a room with an invite code, the conquest map, the weekly league, focus sounds, timer settings and Pomi Pro.",
  keywords="how to use pomi, pomi app guide, pomi rooms invite code, pomi conquest map, pomi garden, pomi pro, pomodoro app tutorial, pomi study app",
  tldr="""<p><strong>Short answer:</strong> Pomi's flow is three steps: <strong>pick a task, start the timer, focus for 25 minutes.</strong> When the session ends a plant is added to your garden and your focus minutes score points for your city on the conquest map. To work with friends, open a room and share the 6-character code; everyone in the room runs their own timer. The timer is free, ad-free and works offline.</p>""",
  howto=dict(name="Completing your first focus session in Pomi", steps=[
    ("Add a task", "In the Tasks tab, write what you are working on today. Every session is linked to a task."),
    ("Set the duration", "Default is 25 minutes of work and a 5-minute break. Change it to 15/3, 50/10 or similar in settings."),
    ("Start the timer and move the phone away", "The timer keeps counting with the screen off and the app in the background."),
    ("Optionally turn on sounds or join a room", "Mix rain, café and forest sounds; join your friends' room with an invite code."),
    ("Complete the session", "A new plant joins your garden, your focus minutes score points for your city, and you move up the weekly league."),
  ]),
  body="""
<h2 id="first">Your first session: three steps</h2>
<ol>
  <li><strong>Add a task.</strong> In the Tasks tab, write something concrete: "derivative problem set 40-48". Every session is linked to a task, so at the end of the day you can see how many sessions each piece of work received.</li>
  <li><strong>Start the timer.</strong> The default cycle is 25 minutes of work and a 5-minute break. While the retro pixel timer runs, do one thing. You can turn the phone face down and move it away; the timer keeps counting with the screen off and the app in the background.</li>
  <li><strong>Complete the session.</strong> When time is up, a new plant joins your garden and your focus minutes are added to your city's score. The break timer starts automatically.</li>
</ol>
<p class="note mint">If you abandon a session, no plant is added. No penalty, no withered tree; the session simply does not count. For the technique itself, see the <a href="what-is-the-pomodoro-technique.html">Pomodoro guide</a>.</p>

<h2 id="garden">The pixel garden and collection</h2>
<p>The garden is a visual record of your focus history. Every completed session is a plant; plants come in species, growth stages and rarities. New species unlock as you focus, and the collection screen shows which ones you have found and which are missing. Reading last month's work at a glance from the garden tends to motivate more than the raw number does.</p>

<h2 id="rooms">Rooms: with friends, each on your own timer</h2>
<p>When you create a room from the Rooms tab, the app generates a <strong>6-character invite code</strong>. Send it to your friends; they enter it in the Rooms tab to join. In the room you see everyone's name and timer status.</p>
<p>An important design decision: <strong>there is no shared timer.</strong> Everyone starts and ends their own session whenever they like. You can be mid-session while a friend takes a break; your session is unaffected. There is no camera, microphone or chat either; the room exists to create the feeling of "we are quietly working together". Why that works is explained in the <a href="study-with-me-how-to-study-together.html">study with me article</a>.</p>
<p>For a good room routine: fix a time ("every evening at 8"), have everyone write their task in advance, and save talking for the break.</p>

<h2 id="conquest">The conquest map</h2>
<p>The feature that sets Pomi apart from other timers. You pick your city in your profile; the minutes of every session you complete are added to your city's score. As the score grows, regions on the map turn your city's colour. Regions change hands through the day: you take one today, a rival city takes it back tomorrow. Seasons last <strong>7 days</strong>; at the end of a season the city holding the most regions wins. Turkey's 81 cities compete. It is the mechanism that makes you feel part of a team even when you study alone.</p>

<h2 id="league">The weekly league</h2>
<p>The league is an individual ranking: you compete with other users in the same league on weekly focus time, and at the end of the week you move up or down depending on your position. You also see where your city stands overall. The league's purpose is to judge your week rather than your day; one bad day does not ruin the week.</p>

<h2 id="sounds">Focus sounds</h2>
<p>You can turn on rain, café, forest and other sounds during a session, adjust each one's level separately and mix them: light rain over a distant café murmur, say. The sounds stop with the timer. Which sound suits which work is covered in the <a href="best-background-sounds-for-studying.html">background sounds article</a>.</p>

<h2 id="settings">Settings: durations and theme</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Setting</th><th>What it does</th><th>Suggestion</th></tr></thead>
  <tbody>
    <tr><td>Work duration</td><td>Session length</td><td>Start with 25; 40-50 for problem sets</td></tr>
    <tr><td>Short break</td><td>Break between sessions</td><td>5; 8-10 for long sessions</td></tr>
    <tr><td>Long break</td><td>Break after four sessions</td><td>15-30</td></tr>
    <tr><td>Dark mode</td><td>Dark theme for night use</td><td>For evening sessions</td></tr>
    <tr><td>City</td><td>Where your conquest map points go</td><td>Pick once; be in the same city as your friends</td></tr>
  </tbody>
</table>
</div>

<h2 id="stats">Statistics</h2>
<p>A weekly focus-hours chart, completed session count and a breakdown by task. "Did I really give time to my weak subject this week?" becomes a number rather than a guess. For realistic weekly targets see <a href="how-many-pomodoros-a-day.html">how many pomodoros a day</a>.</p>

<h2 id="pro">Free and Pomi Pro</h2>
<p>The timer, garden, tasks, rooms and conquest map are in the free version, and there are <strong>no ads</strong>. Pomi Pro is an optional subscription with extra features and personalisation. You manage it through your store account and can cancel any time. Restoring purchases and deleting your account are covered on the <a href="../support.html">support page</a>.</p>

<h2 id="offline">Offline and background</h2>
<p>The timer and garden work without internet; rooms, the conquest map and the league need a connection. Sessions completed offline are credited to your city when the connection returns. The timer keeps counting when the app is closed; allow notifications and you will be told when a session or break ends.</p>

<h2 id="tips">5 tips for the first week</h2>
<ol>
  <li>For the first three days, just the timer and tasks; look at rooms and the map later.</li>
  <li>Aim for 3 to 4 sessions a day and raise the count once a week.</li>
  <li>Pick your city and invite one friend from the same city; the map makes sense from then on.</li>
  <li>Open a room at a fixed time each evening; share the code once, the room persists.</li>
  <li>Check the statistics on Sunday evening and write one target for next week.</li>
</ol>
""",
  faq=[
    ("Is Pomi free?", "Yes. The timer, garden, tasks, rooms and conquest map are free, with no ads. Pomi Pro is an optional subscription with extra features and can be cancelled at any time."),
    ("How do I create a room in Pomi?", "Create a new room from the Rooms tab; the app gives you a 6-character invite code. Send it to your friends, who join by entering the code in their Rooms tab. Everyone in the room runs their own timer."),
    ("Does Pomi work offline?", "The timer and garden work without internet. Rooms, the conquest map and the league need a connection; sessions completed offline are credited to your city when you reconnect."),
    ("What happens if I abandon a session?", "No plant is added and the session does not count. There is no penalty or withered tree; you start the next session clean."),
    ("Can I change the work duration in Pomi?", "Yes. Work, short-break and long-break durations are adjustable in settings; cycles like 15/3, 25/5 or 50/10 all work. A completed session adds a plant to the garden regardless of length."),
    ("Which devices is Pomi available on?", "iPhone and iPad (iOS 15 or later) and Android. There is no web or desktop version at the moment."),
  ],
))

# ─────────────────────────────────────────────────────────────────
# Gamification
# ─────────────────────────────────────────────────────────────────
POSTS.append(dict(
  slug="does-gamification-help-you-focus", lang="en", pair="odak-uygulamalarinda-oyunlastirma-ise-yarar-mi",
  section="Basics", date=D, date_human=DH, rfc822=RFC, read=7, words=1200,
  related=["how-to-stop-procrastinating", "forest-app-alternatives", "how-to-use-pomi"],
  title="Does Gamification Actually Help You Focus? An Honest Look at Trees, Gardens and Leagues",
  short="Does gamification help you focus",
  h1="Does gamification actually <span class=\"accent\">help you focus</span>?",
  lead="Dying trees, growing gardens, streaks you must not break. What the research says, which mechanics last, which fade in weeks, and what we deliberately did not build as makers of a focus app.",
  desc="Does gamification work in focus and productivity apps? Research findings, punishment vs reward mechanics, the streak trap, self-determination theory, team goals and the design decisions behind Pomi.",
  keywords="does gamification work, gamification productivity, gamified focus app, streaks motivation, reward vs punishment motivation, self determination theory apps, forest tree dies, motivation app design",
  tldr="""<p><strong>Short answer:</strong> Yes, with conditions. Research shows gamification raises engagement <strong>in the short term</strong>, while <strong>long-term</strong> effects depend on the mechanic and the person. What works: visible progress, meaningful feedback, team goals. What fails: fear of punishment, streaks that reset everything, and rewards unrelated to the work. If gamification cannot make you like the work, it only makes starting easier; that is still worth a lot.</p>""",
  body="""
<h2 id="research">What the research says</h2>
<p>The most cited review in the field, by Hamari, Koivisto and Sarsa in 2014, examined 24 empirical studies. The conclusion: gamification mostly produces positive effects, but the effect depends strongly on <strong>context and user</strong>, and most studies were short. There is a "novelty effect" problem: a new mechanic works in the first weeks and fades once you are used to it.</p>
<p>The deeper explanation comes from Deci and Ryan's self-determination theory. People need three things: <strong>competence</strong> (seeing progress), <strong>autonomy</strong> (it being my choice) and <strong>relatedness</strong> (connection with others). Gamification that feeds those three supports intrinsic motivation; gamification that pushes from outside (punishment, pressure, artificial competition) can weaken it over time.</p>

<h2 id="mechanics">Mechanic by mechanic: what works, what doesn't</h2>
<div class="table-wrap">
<table>
  <thead><tr><th>Mechanic</th><th>Example</th><th>Short term</th><th>Long term</th><th>Risk</th></tr></thead>
  <tbody>
    <tr><td>Punishment / loss</td><td>Tree dies if you leave the app</td><td>Strong</td><td>Fades</td><td>Anxiety; quitting the app</td></tr>
    <tr><td>Growing collection</td><td>A plant per session, garden grows</td><td>Moderate</td><td>Good</td><td>Saturation (the 100th plant)</td></tr>
    <tr><td>Streak</td><td>"37 days in a row"</td><td>Strong</td><td>Splits people</td><td>Missing one day and quitting</td></tr>
    <tr><td>Points and levels</td><td>XP, ranks</td><td>Moderate</td><td>Weak</td><td>Unrelated to the work; loses meaning</td></tr>
    <tr><td>Team goal</td><td>Winning regions for your city</td><td>Moderate</td><td>Good</td><td>Disengagement if my contribution is invisible</td></tr>
    <tr><td>Social presence</td><td>Working in a room with friends</td><td>Good</td><td>Good</td><td>Comparison pressure</td></tr>
    <tr><td>Informative feedback</td><td>Weekly focus chart</td><td>Weak</td><td>Good</td><td>Almost none</td></tr>
  </tbody>
</table>
</div>

<h3>Why punishment works for months and then fades</h3>
<p>Loss aversion is a powerful drive; the dying tree uses exactly that. But punishment reduces the reason for doing the work to "don't let the tree die". Self-determination theory predicts this <strong>crowds out</strong> intrinsic motivation, and in practice that is what happens: the user either stops caring about the punishment or deletes the app. Punishment can be a first push that makes starting easier; it cannot be what sustains you.</p>

<h3>The streak trap</h3>
<p>Streaks turn one missed day into a catastrophe. Habit research finds that missing a single day does no measurable harm to habit formation (Lally and colleagues, 2010), yet the streak mechanic makes it feel like the opposite, and "it's broken anyway" makes quitting easy. If streaks are used at all, they should be weekly and forgive one missed day.</p>

<h3>Why team goals are durable</h3>
<p>They feed the need for relatedness and tie your effort to something larger than yourself. "If I don't work today my city loses a region" lasts longer than an individual score. The condition: the contribution must be visible. A user who cannot see their contribution drifts away from the team.</p>

<h2 id="pomi">What we built in Pomi, what we didn't, and why</h2>
<p>Building a focus app, we looked at this research and made the following calls. You may disagree, but the reasoning should be transparent:</p>
<ul>
  <li><strong>No punishment.</strong> An abandoned session adds no plant, but nothing withers, dies or resets. We did not want motivation built on anxiety.</li>
  <li><strong>A growing collection.</strong> The garden has species, stages and rarity layers to delay saturation; the 100th plant can be a new species.</li>
  <li><strong>No daily streak; a weekly league instead.</strong> The league judges the week; one bad day does not ruin it.</li>
  <li><strong>A team goal: the conquest map.</strong> Your focus minutes score for your city and 81 cities compete in 7-day seasons. The contribution is visible: you see your city's colour on the map and how many people are focusing right now.</li>
  <li><strong>Social presence, not social pressure.</strong> In rooms everyone runs their own timer; nobody can break anyone else's session, and nobody gets blamed for killing a tree.</li>
  <li><strong>The boring but effective part too.</strong> The weekly statistics chart is not a game at all, and over the long run it is the most useful feedback in the app.</li>
</ul>

<h2 id="who">Who it works for, and who it doesn't</h2>
<p>Gamification helps most for <strong>people who struggle to start</strong> and <strong>people who quit because they cannot see progress</strong>. For someone who already enjoys the work and does it regularly, it is unnecessary and can even distract; that person is happier with a plain timer. If you do not know which you are, try two weeks with a gamified app and two weeks with a plain timer, then compare the weekly totals. Let the number decide.</p>

<h2 id="summary">Summary</h2>
<p>Gamification is not magic. Done well, it makes starting easier, makes progress visible and gives someone working alone a sense of team. Done badly, it produces anxiety and gets deleted within weeks. The difference lies in how closely the mechanic is tied to the work itself and to basic human needs.</p>
""",
  faq=[
    ("Does gamification really improve productivity?", "Research shows it increases engagement in the short term, while long-term effects depend on the mechanic and the person. Visible progress, meaningful feedback and team goals hold up; punishment and artificial points fade within weeks."),
    ("Why does the dying tree in Forest work?", "It uses loss aversion and is strong for the first months. But punishment-based motivation weakens over time; users either stop caring about the penalty or quit the app. It is a good starter and a weak sustainer."),
    ("Are streaks harmful?", "It depends on the person. For some they are a strong push, but because they turn one missed day into a catastrophe they also make quitting easy. Research shows missing one day does not harm habit formation; if streaks are used they should be weekly and forgiving."),
    ("Why doesn't Pomi use punishment?", "Because research suggests anxiety-based motivation crowds out intrinsic motivation over time. An abandoned session adds no plant, but nothing withers or resets; progress is made visible through the garden, the weekly league and the conquest map instead."),
    ("Who is gamification not suitable for?", "People who already enjoy the work and do it regularly; for them it is unnecessary and can distract. Such a person does better with a plain timer. If unsure, compare two weeks with a gamified app against two weeks with a plain timer using weekly totals."),
  ],
  sources=[
    "Hamari, J., Koivisto, J. &amp; Sarsa, H. (2014). Does gamification work? A literature review of empirical studies on gamification. <em>Proceedings of the 47th Hawaii International Conference on System Sciences</em>.",
    "Deci, E. L. &amp; Ryan, R. M. (2000). The \"what\" and \"why\" of goal pursuits: Human needs and the self-determination of behavior. <em>Psychological Inquiry</em>, 11(4).",
    "Deci, E. L., Koestner, R. &amp; Ryan, R. M. (1999). A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation. <em>Psychological Bulletin</em>, 125(6).",
    "Lally, P., van Jaarsveld, C. H. M., Potts, H. W. W. &amp; Wardle, J. (2010). How are habits formed: Modelling habit formation in the real world. <em>European Journal of Social Psychology</em>, 40(6).",
  ],
))
