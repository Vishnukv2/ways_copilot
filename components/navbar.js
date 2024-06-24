const navbar = `
<a href="copilot.html"><img class="w-10 h-10" src="logo.png" alt=""></a>
<hr class="w-[1px] h-[90%] bg-white">
<p class="font-semibold">WaysAhead's CoPilot</p>
`;

class Navbar extends HTMLElement {
    connectedCallback() {
        const classes = "col-span-3 flex gap-4 items-center justify-start p-4 border-b border-white";
        this.innerHTML = navbar;
        this.classList.add(...classes.split(' '));
    }
}

customElements.define('nav-bar', Navbar);