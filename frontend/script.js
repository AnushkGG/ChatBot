async function sendMessage() {
  const input = document.getElementById("userInput");
  const msg = input.value.trim();
  if (!msg) return;

  appendMessage("You", msg);

  const res = await fetch("http://127.0.0.1:8000/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg }),
  });

  const data = await res.json();
  appendMessage("Bot", data.reply);
  input.value = "";
}

function appendMessage(sender, text) {
  const messages = document.getElementById("messages");
  const msgElem = document.createElement("div");
  msgElem.textContent = `${sender}: ${text}`;
  messages.appendChild(msgElem);
}
