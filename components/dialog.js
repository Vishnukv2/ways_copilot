const dialog = `
                <dialog id="otpDialog" class="w-full bg-transparent">
                    <div class="w-full mx-auto max-w-md p-4 bg-white border border-gray-200 rounded-lg shadow sm:p-6 md:p-8 dark:bg-gray-800 dark:border-gray-700">
                        <form id="otp-form" class="space-y-6">
                            <h5 class="text-xl font-medium text-white">Enter your passcode</h5>
                            <input type="text" name="password" id="otp-password" placeholder="••••••••"
                                class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-600 dark:border-gray-500 dark:placeholder-gray-400 dark:text-white"
                                required autocomplete="off" />
                            <p class="text-red-500"></p>
                            <button type="submit"
                                class="w-full text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center">Submit</button>
                        </form>
                    </div>
                </dialog>
`;

class Dialog extends HTMLElement {
    connectedCallback() {
        this.innerHTML = dialog;
    }
}

customElements.define('dialog-box', Dialog);