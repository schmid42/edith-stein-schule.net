require('../scss/main.scss');


console.log("Hello from main!");

// Get all "navbar-burger" elements
const burgers = document.querySelectorAll('.navbar-burger');

for (const burger of burgers) {
    burger.addEventListener('click', (event) => {
        const targetId = burger.dataset.target;
        const target = document.getElementById(targetId);
        burger.classList.toggle('is-active');
        target.classList.toggle('is-active');
    });
}
