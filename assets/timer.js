/* ════════════════════════════════════════════════════════════════
   Pomi web Pomodoro sayacı — /pomodoro-sayaci/, /pomodoro-timer/,
   /online-kutuphane/, /study-together/ sayfalarında çalışır.

   Metinler sayfadaki <script id="timerText" type="application/json">
   bloğundan gelir (build_blog.py → landing_content.TIMER_UI), böylece
   tek dosya iki dilde çalışır.

   Neden bitiş zamanı (endAt): arka plandaki sekmelerde tarayıcı
   setInterval'ı yavaşlatır; saniye saymak süreyi kaydırır. Kalan süre her
   tikte Date.now() ile yeniden hesaplanır.
   ════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  const root = document.getElementById('timer');
  const textEl = document.getElementById('timerText');
  if (!root || !textEl) return;

  let T = {};
  try { T = JSON.parse(textEl.textContent); } catch (e) { /* metinsiz de çalışsın */ }

  const $ = id => document.getElementById(id);
  const clockEl = $('timerClock'), stateEl = $('timerState'), toggleBtn = $('timerToggle');
  const countEl = $('timerCount'), plantsEl = $('timerPlants');
  const modeBtns = Array.from(root.querySelectorAll('.timer-modes button'));
  const inputs = {
    focus: $('setFocus'), short: $('setShort'), long: $('setLong'), every: $('setEvery'),
    noise: $('setNoise'), auto: $('setAuto'), chime: $('setChime'), notify: $('setNotify')
  };
  const baseTitle = document.title;

  /* ── Kalıcı ayarlar (yalnızca bu tarayıcıda) ── */
  const STORE_KEY = 'pomi-web-timer';
  const DEFAULTS = { focus: 25, short: 5, long: 15, every: 4, noise: 'off', auto: false, chime: true, notify: false };
  const LIMITS = { focus: [1, 180], short: [1, 60], long: [1, 90], every: [2, 12] };

  function load() {
    try { return Object.assign({}, DEFAULTS, JSON.parse(localStorage.getItem(STORE_KEY) || '{}')); }
    catch (e) { return Object.assign({}, DEFAULTS); }
  }
  function save() {
    try { localStorage.setItem(STORE_KEY, JSON.stringify(settings)); } catch (e) { /* özel mod */ }
  }

  const today = () => new Date().toISOString().slice(0, 10);
  function loadCount() {
    try {
      const d = JSON.parse(localStorage.getItem(STORE_KEY + '-day') || '{}');
      return d.date === today() ? (d.count | 0) : 0;
    } catch (e) { return 0; }
  }
  function saveCount() {
    try { localStorage.setItem(STORE_KEY + '-day', JSON.stringify({ date: today(), count: completed })); } catch (e) { /* özel mod */ }
  }

  let settings = load();
  let completed = loadCount();
  let mode = 'focus';
  let running = false;
  let endAt = 0;
  let remaining = settings.focus * 60000;
  let tickId = 0;

  /* ── Görünüm ── */
  const fmt = ms => {
    const s = Math.max(0, Math.ceil(ms / 1000));
    return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0');
  };
  const runLabel = () => ({ focus: T.focusRun, short: T.shortRun, long: T.longRun })[mode] || '';

  function render() {
    const left = running ? endAt - Date.now() : remaining;
    clockEl.textContent = fmt(left);
    const label = running ? runLabel() : (T.paused || '');
    document.title = running || left !== duration(mode) ? fmt(left) + ' · ' + label + ' — Pomi' : baseTitle;
  }

  function renderMode() {
    root.setAttribute('data-mode', mode);
    modeBtns.forEach(b => b.setAttribute('aria-pressed', String(b.dataset.mode === mode)));
  }

  /* Bugünkü seanslar: her seans bir piksel domates (uygulamadaki bahçenin küçük hâli). */
  const PLANT = '<svg viewBox="0 0 16 16" shape-rendering="crispEdges"><rect x="7" y="2" width="2" height="2" fill="#2FB99B"/><rect x="5" y="3" width="6" height="2" fill="#2FB99B"/><rect x="3" y="5" width="10" height="8" fill="#27223D"/><rect x="4" y="6" width="8" height="6" fill="#E8455B"/><rect x="5" y="7" width="2" height="1" fill="#FF7A8C"/></svg>';
  function renderGarden() {
    countEl.textContent = completed;
    const shown = Math.min(completed, 12);
    plantsEl.innerHTML = PLANT.repeat(shown) + (completed > shown ? '<span>+' + (completed - shown) + '</span>' : '');
  }

  function setState(text) { stateEl.textContent = text; }

  /* ── Sayaç ── */
  const duration = m => settings[m === 'focus' ? 'focus' : m] * 60000;

  function tick() {
    if (!running) return;
    if (endAt - Date.now() <= 0) { finish(); return; }
    render();
  }

  function start() {
    if (running) return;
    running = true;
    endAt = Date.now() + remaining;
    clearInterval(tickId);
    tickId = setInterval(tick, 250);
    toggleBtn.textContent = T.pause || 'Pause';
    setState(runLabel());
    unlockAudio();
    syncNoise();
    render();
  }

  function pause() {
    if (!running) return;
    running = false;
    remaining = Math.max(0, endAt - Date.now());
    clearInterval(tickId);
    toggleBtn.textContent = T.resume || 'Resume';
    setState(T.paused || '');
    syncNoise();
    render();
  }

  function setMode(next, keepState) {
    running = false;
    clearInterval(tickId);
    mode = next;
    remaining = duration(mode);
    renderMode();
    toggleBtn.textContent = T.start || 'Start';
    if (!keepState) setState(T.ready || '');
    syncNoise();
    render();
  }

  function nextMode() {
    if (mode !== 'focus') return 'focus';
    return completed > 0 && completed % settings.every === 0 ? 'long' : 'short';
  }

  function finish() {
    const wasFocus = mode === 'focus';
    if (wasFocus) { completed += 1; saveCount(); renderGarden(); }
    if (settings.chime) chime();
    if (settings.notify) notify(wasFocus ? T.notifyFocus : T.notifyBreak);
    setMode(nextMode(), true);
    setState(wasFocus ? T.doneFocus : T.doneBreak);
    if (settings.auto) start();
  }

  function reset() { setMode(mode); }
  function skip() { setMode(nextMode()); }

  /* ── Ses: zil ve arka plan gürültüsü (dosya indirmeden, Web Audio ile) ── */
  let ctx = null, noiseNode = null, noiseGain = null;
  function unlockAudio() {
    if (ctx) { if (ctx.state === 'suspended') ctx.resume(); return; }
    const AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return;
    try { ctx = new AC(); } catch (e) { ctx = null; }
  }

  function chime() {
    unlockAudio();
    if (!ctx) return;
    const now = ctx.currentTime;
    [880, 1318.5].forEach((f, i) => {
      const o = ctx.createOscillator(), g = ctx.createGain();
      o.type = 'sine'; o.frequency.value = f;
      g.gain.setValueAtTime(0.0001, now + i * 0.22);
      g.gain.exponentialRampToValueAtTime(0.25, now + i * 0.22 + 0.02);
      g.gain.exponentialRampToValueAtTime(0.0001, now + i * 0.22 + 0.9);
      o.connect(g).connect(ctx.destination);
      o.start(now + i * 0.22); o.stop(now + i * 0.22 + 1);
    });
  }

  /* Kahverengi: beyaz gürültünün entegrali (derin uğultu). Pembe: Paul Kellet'in filtresi. */
  function noiseBuffer(kind) {
    const len = ctx.sampleRate * 4, buf = ctx.createBuffer(1, len, ctx.sampleRate), d = buf.getChannelData(0);
    let last = 0, b0 = 0, b1 = 0, b2 = 0, b3 = 0, b4 = 0, b5 = 0, b6 = 0;
    for (let i = 0; i < len; i++) {
      const w = Math.random() * 2 - 1;
      if (kind === 'brown') {
        last = (last + 0.02 * w) / 1.02; d[i] = last * 3.5;
      } else {
        b0 = 0.99886 * b0 + w * 0.0555179; b1 = 0.99332 * b1 + w * 0.0750759;
        b2 = 0.96900 * b2 + w * 0.1538520; b3 = 0.86650 * b3 + w * 0.3104856;
        b4 = 0.55000 * b4 + w * 0.5329522; b5 = -0.7616 * b5 - w * 0.0168980;
        d[i] = (b0 + b1 + b2 + b3 + b4 + b5 + b6 + w * 0.5362) * 0.11; b6 = w * 0.115926;
      }
    }
    return buf;
  }

  function stopNoise() {
    if (noiseNode) { try { noiseNode.stop(); } catch (e) { /* zaten durdu */ } noiseNode.disconnect(); noiseNode = null; }
  }

  /* Gürültü yalnızca odak seansı çalışırken açık; molada susar. */
  function syncNoise() {
    const want = running && mode === 'focus' && settings.noise !== 'off';
    if (!want) { stopNoise(); return; }
    unlockAudio();
    if (!ctx) return;
    if (noiseNode && noiseNode._kind === settings.noise) return;
    stopNoise();
    noiseGain = noiseGain || ctx.createGain();
    noiseGain.gain.value = 0.35;
    noiseGain.connect(ctx.destination);
    noiseNode = ctx.createBufferSource();
    noiseNode.buffer = noiseBuffer(settings.noise);
    noiseNode.loop = true;
    noiseNode._kind = settings.noise;
    noiseNode.connect(noiseGain);
    noiseNode.start();
  }

  /* ── Bildirim ── */
  function notify(body) {
    if (!('Notification' in window) || Notification.permission !== 'granted') return;
    try { new Notification(T.notifyTitle || 'Pomi', { body: body || '', tag: 'pomi-timer' }); } catch (e) { /* mobil Safari */ }
  }

  /* ── Ayarlar ── */
  function fillInputs() {
    ['focus', 'short', 'long', 'every'].forEach(k => { inputs[k].value = settings[k]; });
    inputs.noise.value = settings.noise;
    inputs.auto.checked = settings.auto;
    inputs.chime.checked = settings.chime;
    inputs.notify.checked = settings.notify && 'Notification' in window && Notification.permission === 'granted';
  }

  ['focus', 'short', 'long', 'every'].forEach(k => {
    inputs[k].addEventListener('change', () => {
      const [min, max] = LIMITS[k];
      const v = Math.min(max, Math.max(min, parseInt(inputs[k].value, 10) || DEFAULTS[k]));
      inputs[k].value = v;
      settings[k] = v;
      save();
      if (!running && k === mode) { remaining = duration(mode); render(); }
    });
  });
  inputs.noise.addEventListener('change', () => { settings.noise = inputs.noise.value; save(); syncNoise(); });
  inputs.auto.addEventListener('change', () => { settings.auto = inputs.auto.checked; save(); });
  inputs.chime.addEventListener('change', () => { settings.chime = inputs.chime.checked; save(); });
  inputs.notify.addEventListener('change', async () => {
    if (!inputs.notify.checked) { settings.notify = false; save(); return; }
    if (!('Notification' in window)) { inputs.notify.checked = false; setState(T.notifyDenied || ''); return; }
    let perm = Notification.permission;
    if (perm === 'default') {
      try { perm = await Notification.requestPermission(); } catch (e) { perm = 'denied'; }
    }
    settings.notify = perm === 'granted';
    inputs.notify.checked = settings.notify;
    if (!settings.notify) setState(T.notifyDenied || '');
    save();
  });

  /* ── Olaylar ── */
  toggleBtn.addEventListener('click', () => (running ? pause() : start()));
  $('timerReset').addEventListener('click', reset);
  $('timerSkip').addEventListener('click', skip);
  modeBtns.forEach(b => b.addEventListener('click', () => setMode(b.dataset.mode)));

  document.addEventListener('keydown', e => {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const tag = (e.target && e.target.tagName) || '';
    if (/^(INPUT|SELECT|TEXTAREA|BUTTON|SUMMARY|A)$/.test(tag) || (e.target && e.target.isContentEditable)) return;
    if (e.code === 'Space') { e.preventDefault(); running ? pause() : start(); }
    else if (e.key === 'r' || e.key === 'R') { reset(); }
  });

  /* Sekmeye dönünce bekleyen bitişi hemen işle (arka planda tik gecikmiş olabilir). */
  document.addEventListener('visibilitychange', () => { if (!document.hidden) tick(); });

  fillInputs();
  renderMode();
  renderGarden();
  remaining = duration(mode);
  render();
})();
