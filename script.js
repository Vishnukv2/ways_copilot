const messages = [];

function getUserChatBubble(message) {
    const time = new Date().toLocaleTimeString('en-US', {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    });

    return `
        <div class="flex items-start gap-2.5 chat-bubble user" >
            <img class="w-8 h-8 rounded-full" alt="user" src="you.png"
                alt="Jese image">
                <div
                    class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 rounded-e-xl rounded-es-xl bg-blue-700">
                    <div class="flex items-center space-x-2 rtl:space-x-reverse">
                        <span class="text-sm font-semibold text-gray-900 dark:text-white">You</span>
                        <span class="text-sm font-normal text-gray-500 dark:text-gray-400">${time}</span>
                    </div>
                    <p class="text-sm font-normal py-2.5 text-gray-900 dark:text-white">${message}</p>
                </div>
        </div>
    `;
}

function getBotChatBubble(message) {
    const time = new Date().toLocaleTimeString('en-US', {
        hour: 'numeric',
        minute: 'numeric',
        hour12: true
    });

    return `
        <div class="flex items-start gap-2.5 chat-bubble bot" >
                <div
                    class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 rounded-xl rounded-tr-none bg-[#2b2b2b]">
                    <div class="flex items-center space-x-2 rtl:space-x-reverse">
                        <span class="text-sm font-semibold text-gray-900 dark:text-white">WaysAhead's CoPilot</span>
                        <span class="text-sm font-normal text-gray-500 dark:text-gray-400">${time}</span>
                    </div>
                    <p class="text-sm font-normal py-2.5 text-gray-900 dark:text-white">${message}</p>
                </div>
                <img class="w-8 h-8 rounded-full" alt="user" src="pilot.jpeg"
                alt="Jese image">
        </div>
    `;
}

function appendMessage(message, sender) {
    const welcomeMsgDiv = document.getElementById("welcomeMsg");
    welcomeMsgDiv.style.display = "none";

    const chatContainer = document.getElementById("chatContainer");
    const chatBubble = document.createElement("div");
    if (sender === "user") {
        chatBubble.innerHTML = getUserChatBubble(message);
    } else {
        chatBubble.innerHTML = getBotChatBubble(message);
    }
    chatContainer.appendChild(chatBubble);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

async function getBotResponse(message) {
    const loader = document.getElementById("loader");

    loader.classList.remove("hidden");
    loader.classList.add("flex");

    const response = await fetch("https://copilot.waysaheadglobal.com/api/ask", {
        method: "POST",
        body: JSON.stringify({ question: message }),
        headers: {
            "Content-Type": "application/json"
        }
    });
    const data = await response.json();
    messages.push({
        message: data.response,
        sender: "bot"
    });
    appendMessage(data.response, "bot");

    loader.classList.remove("flex");
    loader.classList.add("hidden");
}

document.getElementById("chat-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const input = document.getElementById("chat-input");
    const message = input.value;
    messages.push({
        message,
        sender: "user"
    });
    appendMessage(message, "user");
    getBotResponse(message);
    input.value = "";
});

window.onload = () => {
    if (sessionStorage.getItem("loggedIn") !== "true") {
        document.getElementById("otpDialog").showModal();
    }
}

document.getElementById("otp-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const password = document.getElementById("otp-password").value;

    if (password === "2406") {
        sessionStorage.setItem("loggedIn", "true");
        document.getElementById("otpDialog").close();
    } else {
        document.getElementById("otp-password").nextElementSibling.innerText = "Invalid passcode";
    }
});