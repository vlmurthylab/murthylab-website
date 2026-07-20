/* Play each theme figure once, when it first scrolls into view.
   The figures are inert without this: main.css only hides parts of a figure
   that carries .armed, and .armed is added here. If this script fails to load
   or IntersectionObserver is missing, every figure renders complete. */
(function () {
  var figs = document.querySelectorAll('svg.res-fig');
  if (!figs.length) return;

  // Arm the figures from script, never from the markup: if this file fails to
  // load, nothing is hidden and every figure renders complete.
  function arm() { figs.forEach(function (f) { f.classList.add('armed'); }); }

  // Anyone who has asked for reduced motion sees the finished state, no
  // observer, no animation.
  var still = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)');
  if (still && still.matches) return;          // leave them unarmed = complete
  if (!('IntersectionObserver' in window)) return;

  arm();

  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      e.target.classList.add('in');
      io.unobserve(e.target);   // once only
    });
  }, { threshold: 0.35, rootMargin: '0px 0px -8% 0px' });

  figs.forEach(function (f) { io.observe(f); });
})();
