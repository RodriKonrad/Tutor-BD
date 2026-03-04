document.addEventListener('DOMContentLoaded', function () {
  const form = document.getElementById('chat-form');
  const input = document.getElementById('chat-input');
  const messages = document.getElementById('messages');

  function appendMessage(role, text) {
    const el = document.createElement('div');
    el.className = 'message ' + role;
    const content = document.createElement('div');
    content.className = 'message-content';
    content.textContent = text;
    el.appendChild(content);
    messages.appendChild(el);
    messages.scrollTop = messages.scrollHeight;
  }

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    const txt = input.value.trim();
    if (!txt) return;
    appendMessage('user', txt);
    input.value = '';
    input.focus();

    // Send message to backend (Gemini AI)
    fetch('/chat/send', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: txt })
    })
    .then(response => response.json())
    .then(data => {
      if (data.status === 'success') {
        appendMessage('bot', data.response);
      } else {
        appendMessage('bot', 'Error: ' + data.error);
      }
    })
    .catch(error => {
      appendMessage('bot', 'Error de conexión: ' + error);
    });
  });

  // Send on Enter (no shift)
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      form.dispatchEvent(new Event('submit', { cancelable: true }));
    }
  });
});
