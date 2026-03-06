const menuToggle = document.getElementById('menuToggle');
const siteNav = document.getElementById('siteNav');

if (menuToggle && siteNav) {
  menuToggle.addEventListener('click', () => {
    const isOpen = siteNav.classList.toggle('is-open');
    menuToggle.setAttribute('aria-expanded', String(isOpen));
  });
}

(function setupAnalytics() {
  if (window.location.pathname.startsWith('/analytics')) {
    return;
  }

  const endpoint = '/analytics/collect';
  const visitorKey = 'portfolio_visitor_id';
  const sessionKey = 'portfolio_session_id';
  const startedAt = Date.now();

  function randomId() {
    if (window.crypto && typeof window.crypto.randomUUID === 'function') {
      return window.crypto.randomUUID();
    }
    return `${Date.now()}-${Math.random().toString(36).slice(2)}`;
  }

  function getOrCreate(storage, key) {
    let value = storage.getItem(key);
    if (!value) {
      value = randomId();
      storage.setItem(key, value);
    }
    return value;
  }

  const visitorId = getOrCreate(window.localStorage, visitorKey);
  const sessionId = getOrCreate(window.sessionStorage, sessionKey);

  function sendEvent(eventType, metadata = {}) {
    const payload = {
      event_type: eventType,
      path: window.location.pathname,
      referrer: document.referrer || null,
      visitor_id: visitorId,
      session_id: sessionId,
      metadata,
    };

    const body = JSON.stringify(payload);

    if (navigator.sendBeacon) {
      const blob = new Blob([body], { type: 'application/json' });
      navigator.sendBeacon(endpoint, blob);
      return;
    }

    fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body,
      keepalive: true,
    }).catch(() => undefined);
  }

  sendEvent('page_view', { title: document.title });

  let scroll50Sent = false;
  let scroll90Sent = false;

  function onScroll() {
    const doc = document.documentElement;
    const scrollable = doc.scrollHeight - doc.clientHeight;
    if (scrollable <= 0) {
      return;
    }
    const pct = (window.scrollY / scrollable) * 100;

    if (!scroll50Sent && pct >= 50) {
      scroll50Sent = true;
      sendEvent('scroll_50');
    }
    if (!scroll90Sent && pct >= 90) {
      scroll90Sent = true;
      sendEvent('scroll_90');
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });

  window.setTimeout(() => {
    sendEvent('engaged_30s');
  }, 30_000);

  document.addEventListener('click', (event) => {
    const target = event.target;
    if (!(target instanceof Element)) {
      return;
    }

    const link = target.closest('a');
    if (!link || !link.href) {
      return;
    }

    const url = new URL(link.href, window.location.origin);
    if (url.origin !== window.location.origin) {
      sendEvent('external_click', { href: url.href, domain: url.hostname });
      return;
    }

    if (url.pathname === '/resume/download') {
      sendEvent('resume_download_click', { href: url.pathname });
    }

    if (url.pathname === '/dissertation/download') {
      sendEvent('dissertation_download_click', { href: url.pathname });
    }
  });

  window.addEventListener('pagehide', () => {
    const seconds = Math.round((Date.now() - startedAt) / 1000);
    if (seconds >= 10) {
      sendEvent('dwell_10s_plus', { seconds });
    }
  });
})();
