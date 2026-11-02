/* Navigation must remain usable when optional icon or embed services fail. */
(() => {
  const toggle = document.querySelector('.nav-toggle');
  const menu = document.querySelector('.nav-links');
  if (!toggle || !menu) return;
  const setOpen = open => {
    menu.classList.toggle('nav-open', open);
    toggle.classList.toggle('nav-toggle-active', open);
    toggle.setAttribute('aria-expanded', String(open));
  };
  toggle.addEventListener('click', () => setOpen(toggle.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
      setOpen(false);
      toggle.focus();
    }
  });
  menu.addEventListener('click', event => {
    if (event.target.closest('a')) setOpen(false);
  });
  window.matchMedia('(min-width: 769px)').addEventListener('change', () => setOpen(false));
})();
