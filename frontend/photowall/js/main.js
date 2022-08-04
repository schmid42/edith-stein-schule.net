require('../scss/main.scss');

import * as basicLightbox from 'basiclightbox'

const photosThumb = document.querySelectorAll('.photo-thumb');
const photosOrig  = document.querySelectorAll('.photo-orig');

const boxes = [];

photosOrig.forEach((photo, i) => {
    const photoInstance = basicLightbox.create(photo);
    boxes.push(photoInstance);
});

photosThumb.forEach((photo, i) => {
    photo.addEventListener('click', (event) => {
        boxes[i].show();
    });
});
