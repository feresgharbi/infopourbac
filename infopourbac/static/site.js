// InfoPourBac : bouton « Copier » et sommaire actif. La page fonctionne aussi sans ce script.
(function () {
  document.querySelectorAll('figure.code .copy').forEach(function (b) {
    b.addEventListener('click', function () {
      var code = b.closest('figure').querySelector('pre').innerText;
      var done = function (ok) { b.textContent = ok ? 'Copié ✓' : 'Sélectionne le code'; setTimeout(function () { b.textContent = 'Copier'; }, 1600); };
      if (navigator.clipboard) navigator.clipboard.writeText(code).then(function () { done(true); }, function () { done(false); });
      else done(false);
    });
  });
  var links = document.querySelectorAll('.toc a');
  if (!links.length || !('IntersectionObserver' in window)) return;
  var map = {};
  links.forEach(function (a) { map[a.getAttribute('href').slice(1)] = a; });
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (e.isIntersecting && map[e.target.id]) {
        links.forEach(function (a) { a.classList.remove('on'); });
        map[e.target.id].classList.add('on');
      }
    });
  }, { rootMargin: '-20% 0px -70% 0px' });
  document.querySelectorAll('.article section[id]').forEach(function (s) { io.observe(s); });
})();
