require('../scss/main.scss');

import * as PIXI from 'pixi.js';

document.addEventListener('DOMContentLoaded', () => {

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

    const canvasContainer = document.querySelector('#canvas-container');

    let app = new PIXI.Application({
        width: 900,
        height: 675,
        backgroundColor: 0x000000
    });

    canvasContainer.appendChild(app.view);

});