// 判断是否支持serviceWorker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/service-worker.js', {scope: './'}).then(function(registration) {
      // 注册成功
      console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, function(err) {
      // 注册失败
      console.log('ServiceWorker registration failed: ', err);
    });
  });
}
