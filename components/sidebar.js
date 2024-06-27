const sidebar = `
        <div class="border-b p-4 pt-0 mt-6">
                <h1 class="text-xl font-semibold mb-6">Meet with our Avatars</h1>
                <div class="flex gap-3 items-center justify-between mb-4">
                    <img class="w-20 h-20 rounded-full object-center object-cover" src="Rupam.jpg" alt="Avatar"
                        class="avatar">
                    <img class="w-20 h-20 rounded-full object-center object-cover" src="amit.jpg" alt="Avatar"
                        class="avatar">
                    <img class="w-20 h-20 rounded-full object-center object-cover" src="sapna.jpeg" alt="Avatar"
                        class="avatar">
                </div>
            </div>
            <h1 class="mt-2 text-2xl font-semibold px-4">Master Documentation</h1>
            <ul class="mb-4">
                <li class="list mt-2  text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4">
                    <a href="/landing.html">Landing Page</a>
                </li>
                <li class="list mt-2 text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4">
                    <a href="/login.html">Login Page</a>
                </li>
                <li class="list mt-2 text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4">
                    <a href="/signup.html">SignUp Page</a>
                </li>
                 <li class="list mt-2 text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4">
                    <a href="/pay.html">Payment Page</a>
                </li>

                <li class="list mt-2 text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4"><a href="/contact.html">Contact Page</a></li>
                <li class="list mt-2  text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4"><a href="/about.html">About Page</a></li>
                <li class="list mt-2  text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4"><a href="/adminlogin.html">Admin Login Page</a></li>
                <li class="list mt-2  text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4"><a href="/admindash.html">Admin Dashboard Page</a></li>
                <li class="list mt-2  text-xl font-semibold text-serif cursor-pointer hover:underline ml-4 px-4"><a href="/userdash.html">User Dashboard Page</a></li>
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