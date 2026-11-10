// Live Tel Aviv clock in the footer ("12:18 PM - IDT")
(function () {
  const els = document.querySelectorAll('[data-clock]');
  if (!els.length) return;
  const fmt = new Intl.DateTimeFormat('en-US', {
    timeZone: 'Asia/Jerusalem', hour: 'numeric', minute: '2-digit', hour12: true, timeZoneName: 'short'
  });
  const tick = () => {
    const parts = fmt.formatToParts(new Date());
    const get = (t) => (parts.find((p) => p.type === t) || {}).value || '';
    // Intl gives "GMT+2"/"GMT+3"; show Israel's own abbreviations instead
    const offset = get('timeZoneName');
    const zone = offset === 'GMT+3' ? 'IDT' : offset === 'GMT+2' ? 'IST' : offset;
    const text = `${get('hour')}:${get('minute')} ${get('dayPeriod')} - ${zone}`;
    els.forEach((el) => (el.textContent = text));
  };
  tick();
  setInterval(tick, 15000);
})();

// Gentle fade-up as sections enter the viewport
(function () {
  const items = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window)) {
    items.forEach((el) => el.classList.add('is-in'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
    });
  }, { rootMargin: '0px 0px -8% 0px' });
  items.forEach((el) => io.observe(el));
})();

// Frame loops: every [data-cycle] swaps its images every N ms (Figma "After delay").
// Used by the hero lettering and the Act logo / line / statue loops.
(function () {
  const still = matchMedia('(prefers-reduced-motion: reduce)');
  document.querySelectorAll('[data-cycle]').forEach((box) => {
    const frames = [...box.querySelectorAll('img')];
    if (frames.length < 2) return;
    const delay = +box.dataset.cycle || 300;
    let i = 0, timer = null;
    const step = () => { frames[i].classList.remove('is-on'); i = (i + 1) % frames.length; frames[i].classList.add('is-on'); };
    const start = () => { if (!timer && !still.matches) { frames.forEach((f) => (f.loading = 'eager')); timer = setInterval(step, delay); } };
    const stop = () => { clearInterval(timer); timer = null; };
    new IntersectionObserver(([e]) => (e.isIntersecting ? start() : stop())).observe(box);
  });
})();

// Act relief carousel: 5 reliefs move one slot left every 1.05s (+0.45s ease)
(function () {
  const box = document.querySelector('[data-carousel]');
  if (!box) return;
  const items = [...box.querySelectorAll('.relief')];
  const W = 1551, H = 872; // Figma frame size
  // slots: off-left, left, centre, right, off-right  (x, y, w, h, opacity)
  const SLOTS = [[-390, 369, 345, 245, 0], [24, 315, 410, 292, 1], [448, 191, 655, 466, 1], [1117, 315, 410, 292, 1], [1596, 369, 345, 245, 0]];
  // Figma frame 01: relief 1 centre, 2 right, 3 off-right, 4 off-left, 5 left
  let pos = [2, 3, 4, 0, 1];
  const place = (instant) => items.forEach((el, k) => {
    const [x, y, w, h, o] = SLOTS[pos[k]];
    el.classList.toggle('no-anim', !!instant);
    Object.assign(el.style, { left: x / W * 100 + '%', top: y / H * 100 + '%', width: w / W * 100 + '%', height: h / H * 100 + '%', opacity: o });
  });
  place(true);
  const step = () => {
    pos = pos.map((p) => (p + 4) % 5); // everyone moves one slot to the left; off-left wraps to off-right
    items.forEach((el, k) => { if (pos[k] === 4) { el.classList.add('no-anim'); } });
    place(false);
    items.forEach((el, k) => { if (pos[k] === 4) { const [x, y, w, h] = SLOTS[4]; el.classList.add('no-anim'); Object.assign(el.style, { left: x / W * 100 + '%', top: y / H * 100 + '%', width: w / W * 100 + '%', height: h / H * 100 + '%' }); } });
  };
  let timer = null;
  const start = () => { if (!timer && !matchMedia('(prefers-reduced-motion: reduce)').matches) { items.forEach((i) => (i.loading = 'eager')); timer = setInterval(step, 1500); } };
  const stop = () => { clearInterval(timer); timer = null; };
  new IntersectionObserver(([e]) => (e.isIntersecting ? start() : stop())).observe(box);
})();

// Menu: scrolling down gathers everything into one centred row
// (and "Let's talk" turns pink). Scrolling up, anywhere on the page,
// spreads it back out to the sides.
(function () {
  const nav = document.querySelector('.nav');
  if (!nav) return;
  const left = nav.querySelector('.nav__left');
  const talk = nav.querySelector('.talk');
  if (!left || !talk) return;
  if (nav.classList.contains('nav--glass')) return; // glass menu: always one centred capsule, no gather
  const ov = parseFloat(getComputedStyle(nav).getPropertyValue('--nav-overlap'));
  const OVERLAP = isNaN(ov) ? 4 : ov; // same -4px overlap as between every pill in the Figma (glass menu: 0)
  const TOP = 80;    // always spread out near the very top
  const NUDGE = 6;   // ignore tiny scroll jitters
  let compact = false, lastY = scrollY, ticking = false;
  const place = () => {
    if (!compact || getComputedStyle(talk).display === 'none' || innerWidth <= 760) {
      left.style.transform = talk.style.transform = '';
      return;
    }
    // measure in the nav's own (unzoomed) coordinates
    const navW = nav.clientWidth;
    const lw = left.offsetWidth, tw = talk.offsetWidth;
    const total = lw + tw - OVERLAP;
    const start = (navW - total) / 2 - 5; // Figma: the row starts at x=491 on the 1440 frame
    left.style.transform = `translateX(${start - left.offsetLeft}px)`;
    talk.style.transform = `translateX(${start + lw - OVERLAP - talk.offsetLeft}px)`;
  };
  const set = (c) => { if (c !== compact) { compact = c; nav.classList.toggle('is-compact', c); place(); } };
  const update = () => {
    const y = scrollY, dy = y - lastY;
    if (y < TOP) set(false);
    else if (dy > NUDGE) set(true);    // scrolling down
    else if (dy < -NUDGE) set(false);  // scrolling up
    if (Math.abs(dy) > NUDGE || y < TOP) lastY = y;
    ticking = false;
  };
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener('resize', place);
  update();
})();

// Project cards: "View project" sticker that follows the cursor
(function () {
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  const cards = document.querySelectorAll('.card');
  if (!cards.length) return;
  const tag = document.createElement('div');
  tag.className = 'cursor-tag'; tag.textContent = 'View project'; tag.setAttribute('aria-hidden', 'true');
  document.body.appendChild(tag);
  let x = 0, y = 0, tx = 0, ty = 0, raf = null;
  const loop = () => {
    x += (tx - x) * 0.22; y += (ty - y) * 0.22;
    tag.style.left = x + 'px'; tag.style.top = y + 'px';
    raf = Math.abs(tx - x) + Math.abs(ty - y) > 0.3 ? requestAnimationFrame(loop) : null;
  };
  addEventListener('pointermove', (e) => { tx = e.clientX; ty = e.clientY; if (!raf) raf = requestAnimationFrame(loop); }, { passive: true });
  cards.forEach((c) => {
    c.addEventListener('pointerenter', (e) => { x = tx = e.clientX; y = ty = e.clientY; loop(); tag.classList.add('is-on'); });
    c.addEventListener('pointerleave', () => tag.classList.remove('is-on'));
  });
})();

// Magnetic buttons: they lean a little toward the cursor
(function () {
  if (!matchMedia('(hover: hover) and (pointer: fine)').matches) return;
  if (matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  document.querySelectorAll('[data-magnetic]').forEach((el) => {
    const pull = 0.3, reach = 90;
    const near = (e) => {
      const r = el.getBoundingClientRect();
      const dx = e.clientX - (r.left + r.width / 2), dy = e.clientY - (r.top + r.height / 2);
      if (Math.hypot(dx, dy) < reach + r.width / 2) el.style.transform = `translate(${dx * pull}px, ${dy * pull}px)`;
      else el.style.transform = '';
    };
    addEventListener('pointermove', near, { passive: true });
  });
})();

// Videos: mobile browsers often ignore the autoplay attribute (iPhone in
// Low Power Mode, data saver, videos that start off-screen). Start every
// muted loop from code as soon as it comes into view, pause it when it
// leaves, and if the phone still refuses, start them on the first touch.
(function () {
  const vids = [...document.querySelectorAll('video[autoplay]')];
  if (!vids.length) return;
  const visible = new Set();
  const play = (v) => { v.muted = true; const p = v.play(); if (p && p.catch) p.catch(() => {}); };
  const io = new IntersectionObserver((entries) => entries.forEach((e) => {
    if (e.isIntersecting) { visible.add(e.target); play(e.target); }
    else { visible.delete(e.target); e.target.pause(); }
  }), { rootMargin: '200px 0px' });
  vids.forEach((v) => { v.muted = true; v.playsInline = true; io.observe(v); });
  const kick = () => visible.forEach((v) => { if (v.paused) play(v); });
  ['touchend', 'click', 'scroll'].forEach((t) => addEventListener(t, kick, { passive: true }));
})();

// Post Nature — Plant Profile: leader lines grow out of the screen, then each card appears
(function () {
  document.querySelectorAll('[data-pp]').forEach((pp) => {
    if (!('IntersectionObserver' in window)) { pp.classList.add('is-in'); return; }
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { pp.classList.add('is-in'); io.disconnect(); } }, { threshold: 0.35 });
    io.observe(pp);
  });
})();

// Post Nature — Interface 02: storyboard callouts follow the video's own timeline
(function () {
  document.querySelectorAll('[data-sb]').forEach((sb) => {
    const video = sb.querySelector('video');
    const cards = [...sb.querySelectorAll('.sb-card')];
    const groups = [...sb.querySelectorAll('.sb__lines g')];
    if (!video || !cards.length) return;
    const spans = cards.map((c) => [+c.dataset.from, +c.dataset.to]);
    let raf = null;
    const tick = () => {
      const t = video.currentTime;
      spans.forEach(([a, z], i) => {
        const on = t >= a && t < z;
        cards[i].classList.toggle('is-on', on);
        groups[i].classList.toggle('is-on', on);
      });
      raf = video.paused ? null : requestAnimationFrame(tick);
    };
    const run = () => { if (!raf) raf = requestAnimationFrame(tick); };
    video.addEventListener('playing', run);
    video.addEventListener('seeked', run);
    video.addEventListener('pause', () => { cancelAnimationFrame(raf); raf = null; });
    if (!video.paused) run();
  });
})();

// Post Nature — 10 plants carousel: arrows / click a side card to bring it forward,
// click the centre card to open it large.
(function () {
  const root = document.querySelector('[data-plants]');
  if (!root) return;
  const slides = [...root.querySelectorAll('.pc__slide')];
  const count = root.querySelector('.pc__count b');
  const name = root.querySelector('.pc__name');
  const curDot = root.querySelector('.pc__cur');
  const dots = [...root.querySelectorAll('.pc__dot')];
  dots.forEach((d) => d.addEventListener('click', () => go(+d.dataset.i)));
  let inView = false;
  new IntersectionObserver(([e]) => { inView = e.isIntersecting; place(); }, { rootMargin: '150px 0px' }).observe(root);
  const N = slides.length;
  const W = 1440, H = 730;
  // x, y, w, h, colour, opacity — Figma frame "10 Plants. 7 Stages Each."
  const DESK = { '-3': [-620, 160, 297, 491, '#efeeea', 0], '-2': [-211, 119, 297, 491, '#efeeea', 1], '-1': [114, 57, 373, 616, '#e4e3df', 1],
    0: [515, 15, 423, 699, '#cbcbcb', 1], 1: [966, 57, 373, 616, '#e4e3df', 1], 2: [1367, 119, 297, 491, '#efeeea', 1], 3: [1760, 160, 297, 491, '#efeeea', 0] };
  const MOB = { '-3': [-1400, 260, 700, 1157, '#efeeea', 0], '-2': [-1400, 260, 700, 1157, '#efeeea', 0], '-1': [-560, 200, 700, 1157, '#e4e3df', 1],
    0: [270, 20, 900, 1487, '#cbcbcb', 1], 1: [1300, 200, 700, 1157, '#e4e3df', 1], 2: [2140, 260, 700, 1157, '#efeeea', 0], 3: [2140, 260, 700, 1157, '#efeeea', 0] };
  // keep every card at the video's real proportions (702×1280), centred on its Figma slot
  const AR = 702 / 1280;
  [DESK, MOB].forEach((S) => Object.keys(S).forEach((k) => { const s = S[k]; const w = s[3] * AR; s[0] = s[0] + (s[2] - w) / 2; s[2] = w; }));
  const mob = matchMedia('(max-width: 760px)');
  let cur = 0;
  const rel = (i) => { let d = (i - cur) % N; if (d > N / 2) d -= N; if (d < -N / 2) d += N; return d; };
  const place = () => {
    const S = mob.matches ? MOB : DESK, h = mob.matches ? 1560 : H;
    slides.forEach((s, i) => {
      const d = Math.max(-3, Math.min(3, rel(i)));
      const prev = s.dataset.d;
      // a slide wrapping round the back jumps without animating
      if (prev !== undefined && Math.abs(prev - d) > 2) s.classList.add('no-anim'); else s.classList.remove('no-anim');
      const [x, y, w, hh, bg, o] = S[d];
      Object.assign(s.style, { left: x / W * 100 + '%', top: y / h * 100 + '%', width: w / W * 100 + '%', height: hh / h * 100 + '%', opacity: o, zIndex: 10 - Math.abs(d) });
      s.style.setProperty('--bg', bg);
      s.dataset.d = d;
      s.classList.toggle('is-center', d === 0);
      s.tabIndex = Math.abs(d) <= 1 ? 0 : -1;
      s.setAttribute('aria-hidden', Math.abs(d) > 2 ? 'true' : 'false');
      const v = s.querySelector('video');
      if (v) { if (inView && Math.abs(d) <= 1) { v.preload = 'auto'; const p = v.play(); if (p && p.catch) p.catch(() => {}); } else v.pause(); }
    });
    if (count) count.textContent = String(cur + 1).padStart(2, '0');
    if (name) name.textContent = slides[cur].dataset.name || '';
    if (curDot) curDot.style.transform = `translateX(${cur * 17}px)`;
    dots.forEach((d, i) => d.setAttribute('aria-selected', i === cur ? 'true' : 'false'));
  };
  const go = (n) => { cur = (n + N) % N; place(); };
  root.querySelectorAll('.pc__btn').forEach((b) => b.addEventListener('click', () => go(cur + +b.dataset.dir)));
  root.addEventListener('keydown', (e) => { if (e.key === 'ArrowRight') go(cur + 1); if (e.key === 'ArrowLeft') go(cur - 1); });
  // swipe on touch screens
  let sx = null;
  root.addEventListener('touchstart', (e) => { sx = e.touches[0].clientX; }, { passive: true });
  root.addEventListener('touchend', (e) => { if (sx === null) return; const dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 40) go(cur + (dx < 0 ? 1 : -1)); sx = null; });
  mob.addEventListener('change', place);

  // lightbox controls: play/pause + a timeline you can click or drag to skip through the stages
  const fmt = (s) => { s = Math.max(0, Math.floor(s || 0)); return Math.floor(s / 60) + ':' + String(s % 60).padStart(2, '0'); };
  const scrubber = (v, host) => {
    const bar = document.createElement('div'); bar.className = 'pc-ctl';
    bar.innerHTML = '<button class="pc-ctl__play" type="button" aria-label="Pause"><svg viewBox="0 0 16 16" aria-hidden="true"><path class="i-pause" d="M4 3h3v10H4zM9 3h3v10H9z"/><path class="i-play" d="M4.5 2.5l9 5.5-9 5.5z"/></svg></button>' +
      '<div class="pc-ctl__track" role="slider" tabindex="0" aria-label="Video position" aria-valuemin="0" aria-valuemax="100" aria-valuenow="0"><div class="pc-ctl__fill"></div><div class="pc-ctl__knob"></div></div>' +
      '<span class="pc-ctl__time">0:00 / 0:00</span>';
    host.appendChild(bar);
    const btn = bar.querySelector('.pc-ctl__play'), track = bar.querySelector('.pc-ctl__track');
    const fill = bar.querySelector('.pc-ctl__fill'), knob = bar.querySelector('.pc-ctl__knob'), time = bar.querySelector('.pc-ctl__time');
    let dragging = false, raf = null;
    const draw = () => {
      const d = v.duration || 0, p = d ? v.currentTime / d : 0;
      fill.style.width = p * 100 + '%'; knob.style.left = p * 100 + '%';
      time.textContent = fmt(v.currentTime) + ' / ' + fmt(d);
      track.setAttribute('aria-valuenow', Math.round(p * 100));
      raf = host.isConnected ? requestAnimationFrame(draw) : null;
    };
    raf = requestAnimationFrame(draw);
    const sync = () => { bar.classList.toggle('is-paused', v.paused); btn.setAttribute('aria-label', v.paused ? 'Play' : 'Pause'); };
    v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
    btn.addEventListener('click', () => (v.paused ? v.play().catch(() => {}) : v.pause()));
    const seekTo = (e) => { const r = track.getBoundingClientRect(); const p = Math.min(1, Math.max(0, (e.clientX - r.left) / r.width)); if (v.duration) v.currentTime = p * v.duration; };
    track.addEventListener('pointerdown', (e) => { dragging = true; track.setPointerCapture(e.pointerId); bar.classList.add('is-drag'); seekTo(e); });
    track.addEventListener('pointermove', (e) => { if (dragging) seekTo(e); });
    const end = () => { dragging = false; bar.classList.remove('is-drag'); };
    track.addEventListener('pointerup', end); track.addEventListener('pointercancel', end);
    track.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowLeft') { e.preventDefault(); e.stopPropagation(); v.currentTime = Math.min(v.duration || 0, Math.max(0, v.currentTime + (e.key === 'ArrowRight' ? 5 : -5))); }
      if (e.key === ' ') { e.preventDefault(); btn.click(); }
    });
  };

  // lightbox (grows out of the clicked card)
  const lb = document.querySelector('.pc-lightbox');
  const box = lb && lb.querySelector('.pc-lightbox__box');
  let from = null;
  const open = (s) => {
    if (!lb) return;
    const src = s.querySelector('video');
    box.innerHTML = '';
    if (src) {
      const v = document.createElement('video');
      Object.assign(v, { src: src.currentSrc || src.src, poster: src.poster, muted: true, loop: true, playsInline: true, autoplay: true });
      v.setAttribute('muted', ''); v.setAttribute('playsinline', '');
      v.addEventListener('loadedmetadata', () => { try { v.currentTime = src.currentTime || 0; } catch (e) {} }, { once: true });
      box.appendChild(v); v.play().catch(() => {});
      src.pause();
    }
    const cap = document.createElement('p'); cap.className = 'pc-lightbox__name'; cap.textContent = s.dataset.name || ''; box.appendChild(cap);
    const v = box.querySelector('video'); if (v) scrubber(v, box);
    lb.hidden = false; document.body.classList.add('no-scroll');
    box.style.transition = 'none'; box.style.transform = 'none';
    const a = s.getBoundingClientRect(), b = box.getBoundingClientRect();
    from = s;
    box.style.transition = 'none';
    box.style.transform = `translate(${a.left - b.left}px, ${a.top - b.top}px) scale(${a.width / b.width}, ${a.height / b.height})`;
    requestAnimationFrame(() => requestAnimationFrame(() => {
      box.style.transition = 'transform .6s cubic-bezier(.2,.75,.15,1)'; box.style.transform = 'none'; lb.classList.add('is-open');
      lb.querySelector('.pc-lightbox__close').focus({ preventScroll: true });
    }));
  };
  const close = () => {
    if (!lb || lb.hidden) return;
    const a = from.getBoundingClientRect(), b = box.getBoundingClientRect();
    box.style.transition = 'transform .45s cubic-bezier(.5,0,.3,1)';
    box.style.transform = `translate(${a.left - b.left}px, ${a.top - b.top}px) scale(${a.width / b.width}, ${a.height / b.height})`;
    lb.classList.remove('is-open');
    setTimeout(() => { lb.hidden = true; box.innerHTML = ''; document.body.classList.remove('no-scroll'); from.focus({ preventScroll: true }); place(); }, 450);
  };
  slides.forEach((s, i) => s.addEventListener('click', () => { if (rel(i) === 0) open(s); else go(i); }));
  if (lb) {
    lb.addEventListener('click', (e) => { if (e.target === lb || e.target.closest('.pc-lightbox__close')) close(); });
    addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
  }
  place();
})();

// Email link: "mailto:" does nothing on computers without a mail app set up
// (most people use Gmail in the browser). On a computer, clicking copies the
// address and says so; on a phone it still opens the mail app (and copies too).
(function () {
  const links = document.querySelectorAll('a[href^="mailto:"]');
  if (!links.length) return;
  const desktop = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const copy = (text) => {
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text);
    const t = document.createElement('textarea'); t.value = text; t.style.cssText = 'position:fixed;opacity:0';
    document.body.appendChild(t); t.select(); try { document.execCommand('copy'); } catch (e) {} t.remove();
    return Promise.resolve();
  };
  links.forEach((a) => {
    const addr = a.href.replace('mailto:', '').split('?')[0];
    a.title = addr;
    a.addEventListener('click', (e) => {
      if (desktop) e.preventDefault();
      copy(addr).then(() => {
        let tip = a.querySelector('.copied');
        if (!tip) { tip = document.createElement('span'); tip.className = 'copied'; tip.setAttribute('role', 'status'); a.appendChild(tip); }
        tip.textContent = 'Email copied ✓';
        tip.classList.add('is-on');
        clearTimeout(a._t); a._t = setTimeout(() => tip.classList.remove('is-on'), 2200);
      }).catch(() => { if (desktop) location.href = a.href; });
    });
  });
})();

// Phone menu: the "menu" pill opens a panel with the rest of the links
(function () {
  const btn = document.querySelector('.menu-btn');
  const panel = document.getElementById('mnav');
  if (!btn || !panel) return;
  const root = document.documentElement;
  const setOpen = (open) => {
    if (open) { panel.hidden = false; requestAnimationFrame(() => root.classList.add('menu-open')); }
    else { root.classList.remove('menu-open'); setTimeout(() => { if (!root.classList.contains('menu-open')) panel.hidden = true; }, 380); }
    btn.setAttribute('aria-expanded', open ? 'true' : 'false');
  };
  btn.addEventListener('click', () => setOpen(!root.classList.contains('menu-open')));
  panel.addEventListener('click', (e) => { if (e.target.closest('a')) setOpen(false); });
  document.addEventListener('click', (e) => { if (root.classList.contains('menu-open') && !e.target.closest('.mnav, .menu-btn')) setOpen(false); });
  addEventListener('keydown', (e) => { if (e.key === 'Escape') setOpen(false); });
  matchMedia('(min-width: 761px)').addEventListener('change', (e) => { if (e.matches) setOpen(false); });
})();
