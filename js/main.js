// Menu overlay
function openMenu(){document.getElementById('menuOverlay').classList.add('open');}
function closeMenu(){document.getElementById('menuOverlay').classList.remove('open');}

// Bio modals (team page)
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
