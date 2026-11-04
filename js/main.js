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
