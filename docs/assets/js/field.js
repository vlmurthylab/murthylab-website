/* Flow-reserve field.
   A lattice of vessels. Most sit below the threshold of detection; a subset
   resolve. Literal to the science: signal that standard tools cannot see. */
(function () {
  var c = document.getElementById('field');
  if (!c) return;
  var ctx = c.getContext('2d');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var pts = [], raf = null, t0 = null;

  function build() {
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    var w = c.clientWidth, h = c.clientHeight;
    c.width = w * dpr; c.height = h * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);

    pts = [];
    var gap = w < 640 ? 26 : 34;
    var cols = Math.ceil(w / gap), rows = Math.ceil(h / gap);
    for (var i = 0; i <= cols; i++) {
      for (var j = 0; j <= rows; j++) {
        // radial falloff from a focus point, jittered — perfusion-like
        var x = i * gap + (((i * 7 + j * 13) % 11) - 5) * 1.1;
        var y = j * gap + (((i * 11 + j * 5) % 9) - 4) * 1.1;
        var dx = (x - w * 0.30) / (w * 0.62);
        var dy = (y - h * 0.52) / (h * 0.92);
        var d = Math.sqrt(dx * dx + dy * dy);
        var reserve = Math.max(0, 1 - d * 0.92) + (((i * 31 + j * 17) % 100) / 100 - 0.5) * 0.34;
        pts.push({
          x: x, y: y,
          r: reserve,                       // "flow reserve" 0..1
          delay: 220 + d * 900 + ((i * 3 + j * 7) % 13) * 45
        });
      }
    }
  }

  function draw(ts) {
    if (t0 === null) t0 = ts;
    var el = ts - t0;
    var w = c.clientWidth, h = c.clientHeight;
    ctx.clearRect(0, 0, w, h);

    for (var k = 0; k < pts.length; k++) {
      var p = pts[k];
      var prog = reduce ? 1 : Math.min(1, Math.max(0, (el - p.delay) / 850));
      if (prog <= 0) continue;
      var ease = 1 - Math.pow(1 - prog, 3);

      // below-threshold points stay faint; above-threshold resolve to amber
      var above = p.r > 0.52;
      var a = above ? (0.10 + p.r * 0.62) * ease : (0.05 + p.r * 0.13) * ease;
      var rad = above ? 1.0 + p.r * 2.0 : 0.85;

      ctx.beginPath();
      ctx.arc(p.x, p.y, rad * (0.55 + 0.45 * ease), 0, 6.2832);
      ctx.fillStyle = above
        ? 'rgba(200,127,50,' + a.toFixed(3) + ')'
        : 'rgba(190,200,212,' + a.toFixed(3) + ')';
      ctx.fill();
    }

    if (!reduce && el < 4200) raf = requestAnimationFrame(draw);
  }

  function start() {
    if (raf) cancelAnimationFrame(raf);
    t0 = null; build();
    raf = requestAnimationFrame(draw);
  }

  var rz;
  window.addEventListener('resize', function () {
    clearTimeout(rz); rz = setTimeout(start, 180);
  });
  start();
})();
