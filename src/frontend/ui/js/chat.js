const chatSpace = document.getElementById("chatSpace");

export function addMessage(type, text) {

    const row = document.createElement("div");
    row.classList.add("message-row", `${type}-msg`);

    const avatar = document.createElement("img");
    avatar.classList.add("avatar");

    avatar.src =
        type === "ai"
            ? "/static/assets/icons/ai_icon.svg"
            : "/static/assets/icons/user_icon.svg";

    const bubble = document.createElement("div");
    bubble.classList.add("message-bubble");

    bubble.textContent = text;

    if (type === "ai") {
        row.appendChild(avatar);
        row.appendChild(bubble);
    }
    else {
        row.appendChild(bubble);
        row.appendChild(avatar);
    }

    chatSpace.appendChild(row);

    scrollToBottom();
}

export function addLoadingMessage() {

    const row = document.createElement("div");
    row.classList.add("message-row", "ai-msg");

    row.innerHTML = `
        <img src="/static/assets/icons/ai_icon.svg" class="avatar">

        <div class="message-bubble loading-bubble">
            Thinking...
        </div>
    `;

    chatSpace.appendChild(row);

    scrollToBottom();

    return row;
}

function scrollToBottom() {
    chatSpace.scrollTop = chatSpace.scrollHeight;
}