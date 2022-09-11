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

    const app = new PIXI.Application({
        resolution: window.devicePixelRatio || 1,
        autoDensity: true,
        width: 1000,
        height: 528,
        backgroundColor: 0xc0c0c0,
        backgroundAlpha: 1
    });

    canvasContainer.appendChild(app.view);

    const textureButton = PIXI.Texture.from('media/images/dot.original.png');
    const button = new PIXI.Sprite(textureButton);
    button.x = 360;
    button.y = 300;
    
    button.interactive = true;
    button.buttonMode = true;
    
    app.stage.addChild(button);
});

