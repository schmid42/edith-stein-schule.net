require('../scss/main.scss');

import * as basicLightbox from 'basiclightbox'

document.addEventListener('DOMContentLoaded', () => {

    const photosThumb = document.querySelectorAll('.photo-thumb');
    const photosOrig = document.querySelectorAll('.photo-orig');

    // stores all lightbox instances
    const boxes = [];

    // create a lightbox per photo and store it
    photosOrig.forEach((photo, i) => {
        const photoInstance = basicLightbox.create(photo);
        boxes.push(photoInstance);
    });

    // add click handler to thumbnail to show connected lightbox
    photosThumb.forEach((photo, i) => {
        photo.addEventListener('click', (event) => {
            boxes[i].show();
        });
    });

});
