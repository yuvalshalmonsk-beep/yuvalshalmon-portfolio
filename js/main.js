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

// Hero: cycle through the "Shalmon" lettering styles (Figma: After delay 300ms, loop)
(function () {
  const box = document.querySelector('[data-cycle]');
  if (!box) return;
  const frames = [...box.querySelectorAll('img')];
  const still = window.matchMedia('(prefers-reduced-motion: reduce)');
  const delay = +box.dataset.cycle || 300;
  let i = 0, timer = null;
  const step = () => { frames[i].classList.remove('is-on'); i = (i + 1) % frames.length; frames[i].classList.add('is-on'); };
  const start = () => { if (!timer && !still.matches) timer = setInterval(step, delay); };
  const stop = () => { clearInterval(timer); timer = null; };
  new IntersectionObserver(([e]) => (e.isIntersecting ? start() : stop())).observe(box);
  still.addEventListener('change', () => (still.matches ? stop() : start()));
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
  const OVERLAP = 4; // same -4px overlap as between every pill in the Figma
  const TOP = 80;    // always spread out near the very top
  const NUDGE = 6;   // ignore tiny scroll jitters
  let compact = false, lastY = scrollY, ticking = false;
  const place = () => {
    if (!compact || getComputedStyle(talk).display === 'none') {
      left.style.transform = talk.style.transform = '';
      return;
    }
    // measure in the nav's own (unzoomed) coordinates
    const navW = nav.clientWidth;
    const lw = left.offsetWidth, tw = talk.offsetWidth;
    const total = lw + tw - OVERLAP;
    const start = (navW - total) / 2;
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
