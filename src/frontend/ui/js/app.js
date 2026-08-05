// import { sendQuery } from "./api.js";
import { addMessage, addLoadingMessage } from "./chat.js";
import { addDownloadItem } from "./downloads.js";

const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");

async function handleSend() {

    const query = userInput.value.trim();

    if (!query) return;

    addMessage("user", query);

    userInput.value = "";

    const loadingRow = addLoadingMessage();

    try {

        const response = await sendQuery(query);

        loadingRow.remove();

        addMessage("ai", response.answer);

        if (response.files) {

            response.files.forEach(file => {
                addDownloadItem(file.name, file.url);
            });
        }

    }
    catch (error) {

        loadingRow.remove();

        addMessage(
            "ai",
            "Error communicating with backend."
        );

        console.error(error);
    }
}

sendButton.addEventListener("click", handleSend);

userInput.addEventListener("keydown", (e) => {

    if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        handleSend();
    }
});