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
