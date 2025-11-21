const form = document.getElementById('chat-form');
const msgInput = document.getElementById('msg');
const messages = document.getElementById('messages');

function append(role, text) {
  const el = document.createElement('div');
  el.className = role;
  el.innerText = text;
  messages.appendChild(el);
}

form.addEventListener('submit', async e => {
  e.preventDefault();
  const text = msgInput.value.trim();
  if (!text) return;
  append('user', text);
  msgInput.value = '';

  const resp = await fetch('/api/chat', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message: text})
  });
  const data = await resp.json();
  append('bot', data.reply);
});
