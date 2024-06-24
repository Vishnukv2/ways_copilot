const chat = `
            <div class="px-6 pt-6 pb-8 border-b">
                <h1 class="text-xl font-semibold">Mostly Used tags</h1>
                <div class="flex flex-wrap w-full gap-2 mt-4 max-h-[5rem] overflow-y-auto">
                    <button
                        class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300">#login</button>
                    <button
                        class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300">#login</button>
                    <button
                        class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300">#login</button>
                    <button
                        class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300">#login</button>
                    <button
                        class="bg-blue-100 text-blue-800 text-xs font-medium px-2.5 py-0.5 rounded-full dark:bg-blue-900 dark:text-blue-300">#login</button>
                </div>
            </div>
            <div id="chatContainer" class='flex flex-col px-4 flex-1 overflow-auto gap-4 my-4 mt-6'>
                <div id="welcomeMsg" class="my-auto">
                    <img class="w-20 h-20 mx-auto" src="logo.png" alt="">
                    <p class="text-4xl text-center font-semibold">Copilot</p>
                    <p class="text-lg text-center mt-2">Your AI companion</p>
                </div>
                <div id="loader" class="self-center py-3 px-4 bg-blue-700 rounded-xl hidden gap-2 items-center justify-center text-sm fixed bottom-24">
                    <svg aria-hidden="true" class="w-4 h-4 text-gray-200 animate-spin dark:text-gray-500 fill-white" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
                    <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
                    </svg>
                    <p>Generating Response</p>
                </div>
            </div>
            <form id="chat-form" class='sticky bottom-0 px-4'>
                <div
                    class="flex items-center justify-center w-full px-4 pr-4 overflow-hidden max-h-60 grow sm:rounded-md sm:border">
                    <textarea id="chat-input" tabIndex="0" rows="1" placeholder="Send a message."
                        class="min-h-[60px] w-full resize-none bg-transparent px-2 py-[1.3rem] focus-within:outline-none sm:text-sm"></textarea>
                    <button type="submit" class="px-3 py-2 text-sm font-medium text-center text-white bg-blue-700 rounded-lg hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">Send</button>
            </form>
`;

class Chat extends HTMLElement {
    connectedCallback() {
        const classes = 'flex flex-col h-full max-h-screen overflow-y-auto pb-4 border-l';
        this.innerHTML = chat;
        this.classList.add(...classes.split(' '));
    }
}

customElements.define('chat-box', Chat);