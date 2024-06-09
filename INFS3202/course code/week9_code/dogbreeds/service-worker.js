self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => {
      return response || fetch(event.request);
    })
  );
});

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('dog-breeds-cache').then((cache) => {
      return cache.addAll([
        '/dogbreeds/',
        '/dogbreeds/index.html',
        '/dogbreeds/manifest.json',
        '/dogbreeds/icon-192x192.png',
        '/dogbreeds/icon-512x512.png',
      ]);
    })
  );
});