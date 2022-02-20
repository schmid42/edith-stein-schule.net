require('../scss/main.scss');

import Glide from '@glidejs/glide'

let gliderElement = document.querySelector(".glider")

let glide = new Glide('.glide', {
    autoplay: 5000,
})

glide.mount()

console.log("Hello from home!");