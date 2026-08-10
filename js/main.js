// Progressive enhancement gate: reveal styles only apply when JS runs
document.documentElement.classList.add('js');

// ---------------------------------------------------------------- menu
function toggleMenu(){
  const overlay = document.getElementById('menuOverlay');
  const btn = document.querySelector('.menu-btn');
  const open = overlay.classList.toggle('open');
  btn.classList.toggle('active', open);
  btn.setAttribute('aria-expanded', open);
  document.body.classList.toggle('menu-open', open);
}
function closeMenu(){
  const overlay = document.getElementById('menuOverlay');
  overlay.classList.remove('open');
  const btn = document.querySelector('.menu-btn');
  if(btn){ btn.classList.remove('active'); btn.setAttribute('aria-expanded','false'); }
  document.body.classList.remove('menu-open');
}
// kept for compatibility with any onclick="openMenu()" markup
function openMenu(){ toggleMenu(); }

// ---------------------------------------------------------------- bio modals
let lastFocus = null;
function openBio(id){
  lastFocus = document.activeElement;
  const m = document.getElementById('bio-' + id);
  if(m){ m.classList.add('open'); m.querySelector('.bio-close').focus(); }
}
function closeBio(){
  document.querySelectorAll('.modal-backdrop.open').forEach(m => m.classList.remove('open'));
  if(lastFocus) lastFocus.focus();
}
document.addEventListener('keydown', e => {
  if(e.key === 'Escape'){ closeBio(); closeMenu(); }
});
document.addEventListener('click', e => {
  if(e.target.classList && e.target.classList.contains('modal-backdrop')) closeBio();
});

// ---------------------------------------------------------------- scroll reveal
(function(){
  const els = document.querySelectorAll('.reveal');
  if(!els.length) return;
  if(!('IntersectionObserver' in window)){
    els.forEach(el => el.classList.add('in'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    // stagger elements that arrive in the same batch
    let i = 0;
    entries.forEach(entry => {
      if(entry.isIntersecting){
        entry.target.style.transitionDelay = Math.min(i * 80, 320) + 'ms';
        entry.target.classList.add('in');
        io.unobserve(entry.target);
        i++;
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  els.forEach(el => io.observe(el));
})();
