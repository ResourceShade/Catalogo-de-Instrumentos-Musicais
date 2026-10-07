function showToast(msg, icon) {
  var t = document.getElementById('toast');
  if (!t) return;
  t.querySelector('.toast-icon').textContent = icon || '🛒';
  t.querySelector('.toast-msg').textContent  = msg;
  t.classList.add('show');
  setTimeout(function() { t.classList.remove('show'); }, 3000);
}

function finalizarPedido() {
  alert('⚠️ Este recurso está em manutenção.\nPor favor, tente novamente mais tarde.');
}

document.addEventListener('DOMContentLoaded', function() {
  var params = new URLSearchParams(window.location.search);
  if (params.get('adicionado') === '1') {
    showToast('Produto adicionado ao carrinho!', '🛒');
    history.replaceState({}, '', window.location.pathname + (params.get('q') ? '?q=' + params.get('q') : ''));
  }
});
