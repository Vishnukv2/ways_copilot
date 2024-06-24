const sidebar = `
        <div class="border-b p-4 pt-0 mt-6">
                <h1 class="text-xl font-semibold mb-6">Meet with our Avatars</h1>
                <div class="flex gap-4 items-center justify-between mb-4">
                    <img class="w-16 h-16 rounded-full object-center object-cover" src="Rupam.jpg" alt="Avatar"
                        class="avatar">
                    <img class="w-16 h-16 rounded-full object-center object-cover" src="amit.jpg" alt="Avatar"
                        class="avatar">
                    <img class="w-16 h-16 rounded-full object-center object-cover" src="sapna.jpeg" alt="Avatar"
                        class="avatar">
                    <img class="w-16 h-16 rounded-full object-center object-cover" src="logo.png" alt="Avatar"
                        class="avatar">
                </div>
            </div>
            <h1 class="mt-2 text-lg font-semibold px-4">RenoSwift Documentation</h1>
            <ul class="mb-4">
                <li class="list mt-2 cursor-pointer hover:underline ml-4 px-4">
                    <a href="/landing.html">Landing Page</a>
                </li>
                <li class="list mt-2 cursor-pointer hover:underline ml-4 px-4">
                    <a href="/layout.html">WEBSOURCECODE/FRONTEND/SRC/APP/(USER)/ LAYOUT.TSX</a>
                </li>
                <li class="list mt-2 cursor-pointer hover:underline ml-4 px-4"><a href="/pay.html">WEBSOURCECODE/FRONTEND/SRC/APP/(USER)/ PAY</a></li>
                <li class="list mt-2 cursor-pointer hover:underline ml-4 px-4"><a href="/contact.html">CONTACT</a></li>
                <li class="list mt-2 cursor-pointer hover:underline ml-4 px-4"><a href="/about.html">ABOUT</a></li>
                <li class="list mt-2 cursor-pointer hover:underline ml-4 px-4"><a href="/dashboard.html">ADMIN DASHBOARD</a></li>
            </ul>
            </ul>
`;

class Sidebar extends HTMLElement {
    connectedCallback() {
        const classes = "flex flex-col gap-2 h-full max-h-screen overflow-y-auto border-r";
        this.innerHTML = sidebar;
        this.classList.add(...classes.split(' '));
    }
}

customElements.define('side-bar', Sidebar);