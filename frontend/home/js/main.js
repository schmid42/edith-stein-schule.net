require('../scss/main.scss');

import Glide from '@glidejs/glide'

document.addEventListener('DOMContentLoaded', () => {

    let gliderElement = document.querySelector(".glider")
    let glide = new Glide('.glide', {
        autoplay: 5000,
    })
    glide.mount();

});
