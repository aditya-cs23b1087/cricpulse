/* ============================================
   CricPulse — Global JavaScript
   HCI: Feedback, Affordance, Flexibility
   ============================================ */

// --- Theme Management (Universal Design: Flexibility) ---
function initTheme() {
  const saved = localStorage.getItem('cricpulse-theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
}
function toggleTheme() {
  const current = document.documentElement.getAttribute('data-theme');
  const next = current === 'dark' ? 'light' : 'dark';
  document.documentElement.setAttribute('data-theme', next);
  localStorage.setItem('cricpulse-theme', next);
  showToast(next === 'dark' ? '🌙 Dark mode enabled' : '☀️ Light mode enabled');
}
initTheme();

// --- Toast Notifications (Nielsen H1: System Status, Shneiderman R3) ---
function showToast(msg, undoCallback) {
  const t = document.getElementById('toast');
  if (!t) return;
  const msgEl = t.querySelector('.toast-msg');
  const undoBtn = t.querySelector('.undo-btn');
  if (msgEl) msgEl.textContent = msg;
  if (undoBtn) {
    undoBtn.style.display = undoCallback ? 'inline-block' : 'none';
    undoBtn.onclick = () => { undoCallback(); hideToast(); };
  }
  t.classList.add('show');
  clearTimeout(window._toastTimer);
  window._toastTimer = setTimeout(hideToast, 3500);
}
function hideToast() {
  const t = document.getElementById('toast');
  if (t) t.classList.remove('show');
}

// --- Keyboard Shortcuts (Shneiderman R2, Nielsen H7: Flexibility) ---
document.addEventListener('keydown', (e) => {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
  switch (e.key) {
    case '?': showToast('⌨️ Shortcuts: D=Dark mode, /=Search, H=Home'); break;
    case 'd': case 'D': toggleTheme(); break;
    case '/': e.preventDefault(); document.querySelector('.nav-search input')?.focus(); break;
    case 'h': case 'H': window.location = 'index.html'; break;
  }
});

// --- Onboarding (Law of Learning, Learnability) ---
function checkOnboarding() {
  if (!localStorage.getItem('cricpulse-onboarded')) {
    const overlay = document.getElementById('onboarding');
    if (overlay) overlay.classList.add('show');
  }
}
function dismissOnboarding() {
  localStorage.setItem('cricpulse-onboarded', 'true');
  const overlay = document.getElementById('onboarding');
  if (overlay) overlay.classList.remove('show');
}

// --- Favorites (Shneiderman R7: Internal Locus of Control) ---
function getFavorites() {
  return JSON.parse(localStorage.getItem('cricpulse-favorites') || '[]');
}
function toggleFavorite(teamId) {
  let favs = getFavorites();
  const idx = favs.indexOf(teamId);
  if (idx > -1) {
    favs.splice(idx, 1);
    showToast('Removed from favorites', () => { favs.push(teamId); localStorage.setItem('cricpulse-favorites', JSON.stringify(favs)); });
  } else {
    favs.push(teamId);
    showToast('⭐ Added to favorites!');
  }
  localStorage.setItem('cricpulse-favorites', JSON.stringify(favs));
}

// --- Search Autocomplete (Recognition over Recall) ---
const searchSuggestions = [
  'IPL 2026', 'Virat Kohli', 'MS Dhoni', 'Jasprit Bumrah', 'India vs Australia',
  'T20 World Cup', 'Points Table', 'CSK', 'MI', 'RCB', 'Live Scores',
  'Rohit Sharma', 'Schedule', 'Fantasy', 'Pat Cummins', 'KL Rahul'
];
function initSearch() {
  const input = document.querySelector('.nav-search input');
  const box = document.getElementById('search-suggestions');
  if (!input || !box) return;
  input.addEventListener('input', () => {
    const val = input.value.toLowerCase().trim();
    if (val.length < 1) { box.style.display = 'none'; return; }
    const matches = searchSuggestions.filter(s => s.toLowerCase().includes(val)).slice(0, 6);
    if (matches.length === 0) { box.style.display = 'none'; return; }
    box.innerHTML = matches.map(m =>
      `<div class="suggestion-item" onclick="window.location='search.html?q=${encodeURIComponent(m)}'">${m}</div>`
    ).join('');
    box.style.display = 'block';
  });
  input.addEventListener('blur', () => setTimeout(() => box.style.display = 'none', 200));
}

// --- Countdown Timer (Scarcity Principle) ---
function startCountdown(id, hours, minutes, seconds) {
  let h = hours, m = minutes, s = seconds;
  setInterval(() => {
    s--; if (s < 0) { s = 59; m--; } if (m < 0) { m = 59; h--; } if (h < 0) h = 0;
    const el = document.getElementById(id);
    if (el) {
      el.querySelector('.cd-hrs').textContent = String(h).padStart(2, '0');
      el.querySelector('.cd-min').textContent = String(m).padStart(2, '0');
      el.querySelector('.cd-sec').textContent = String(s).padStart(2, '0');
    }
  }, 1000);
}

// --- Accessible Keyboard Nav (Universal Design) ---
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('[tabindex="0"]').forEach(el => {
    el.addEventListener('keydown', e => {
      if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); el.click(); }
    });
  });
  initSearch();
  checkOnboarding();
});

// --- Notification count management ---
function updateNotificationBadge(count) {
  const badges = document.querySelectorAll('.notif-badge');
  badges.forEach(b => {
    b.textContent = count;
    b.style.display = count > 0 ? 'flex' : 'none';
  });
}

// --- Animate elements on scroll (Micro-interactions) ---
function initScrollAnimations() {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate-in');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  document.querySelectorAll('.animate-on-scroll').forEach(el => observer.observe(el));
}
document.addEventListener('DOMContentLoaded', initScrollAnimations);
