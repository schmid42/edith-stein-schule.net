require('../scss/main.scss')

import * as PIXI from 'pixi.js'

document.addEventListener('DOMContentLoaded', () => {

    let active = 'teamwork'

    function showContent() {
        // get all navigation list elements
        const listElements = document.querySelectorAll('div.tabs > ul > li')

        // get all navigation link elements
        const linkElements = document.querySelectorAll('div.tabs > ul > li > a')

        linkElements.forEach((linkElement, i) => {
            switch(i) {
                case 0:
                    linkElement.addEventListener('click', () => {
                        active = 'teamwork'
                        showContent()
                    })
                    break
                case 1:
                    linkElement.addEventListener('click', () => {
                        active = 'community'
                        showContent()
                    })
                    break
                case 2:
                    linkElement.addEventListener('click', () => {
                        active = 'trust'
                        showContent()
                    })
                    break
                case 3:
                    linkElement.addEventListener('click', () => {
                        active = 'learning'
                        showContent()
                    })
                    break
                case 4:
                    linkElement.addEventListener('click', () => {
                        active = 'schoollife'
                        showContent()
                    })
                    break
            }
        })

        // get all tab content elements
        const contentElements = document.querySelectorAll('section.tab-content > div.content')

        listElements.forEach((listElement, i) => {
            switch(i) {
                case 0:
                    if(active === 'teamwork') {
                        listElement.classList.add('is-active')
                        contentElements[i].classList.remove('is-hidden')
                    } else {
                        listElement.classList.remove('is-active')
                        contentElements[i].classList.add('is-hidden')
                    }
                    break
                case 1:
                    if(active === 'community') {
                        listElement.classList.add('is-active')
                        contentElements[i].classList.remove('is-hidden')
                    } else {
                        listElement.classList.remove('is-active')
                        contentElements[i].classList.add('is-hidden')
                    }
                    break
                case 2:
                    if(active === 'trust') {
                        listElement.classList.add('is-active')
                        contentElements[i].classList.remove('is-hidden')
                    } else {
                        listElement.classList.remove('is-active')
                        contentElements[i].classList.add('is-hidden')
                    }
                    break
                case 3:
                    if(active === 'learning') {
                        listElement.classList.add('is-active')
                        contentElements[i].classList.remove('is-hidden')
                    } else {
                        listElement.classList.remove('is-active')
                        contentElements[i].classList.add('is-hidden')
                    }
                    break
                case 4:
                    if(active === 'schoollife') {
                        listElement.classList.add('is-active')
                        contentElements[i].classList.remove('is-hidden')
                    } else {
                        listElement.classList.remove('is-active')
                        contentElements[i].classList.add('is-hidden')
                    }
                    break
                default:
                    // should never happen

            }
        })
    }

    showContent()
    

    // get all "navbar-burger" elements
    const burgers = document.querySelectorAll('.navbar-burger')

    for (const burger of burgers) {
        burger.addEventListener('click', (event) => {
            const targetId = burger.dataset.target
            const target = document.getElementById(targetId)
            burger.classList.toggle('is-active')
            target.classList.toggle('is-active')
        })
    }

    const canvasContainer = document.querySelector('#canvas-container')

    const app = new PIXI.Application({
        resolution: window.devicePixelRatio || 1,
        autoDensity: true,
        width: 1000,
        height: 528,
        backgroundColor: 0xFFFFFF,
        backgroundAlpha: 1
    })

    canvasContainer.appendChild(app.view)

    // load textures
    const dotTexture                = PIXI.Texture.from('../media/images/dot.original.png')

    const communityActiveTexture    = PIXI.Texture.from('../media/images/gemeinschaft_active.original.png')
    const communityInactiveTexture  = PIXI.Texture.from('../media/images/gemeinschaft_inactive.original.png')

    const learningActiveTexture     = PIXI.Texture.from('../media/images/lernen_active.original.png')
    const learningInactiveTexture   = PIXI.Texture.from('../media/images/lernen_inactive.original.png')

    const schoollifeActiveTexture   = PIXI.Texture.from('../media/images/schulleben_active.original.png')
    const schoollifeInactiveTexture = PIXI.Texture.from('../media/images/schulleben_inactive.original.png')

    const trustActiveTexture        = PIXI.Texture.from('../media/images/vertrauen_active.original.png')
    const trustInactiveTexture      = PIXI.Texture.from('../media/images/vertrauen_inactive.original.png')

    const teamworkActiveTexture     = PIXI.Texture.from('../media/images/zusammenarbeit_active.original.png')
    const teamworkInactiveTexture   = PIXI.Texture.from('../media/images/zusammenarbeit_inactive.original.png')

    // create sprites
    const dot          = new PIXI.Sprite(dotTexture)
    const community    = new PIXI.Sprite(communityInactiveTexture)
    const learning     = new PIXI.Sprite(learningInactiveTexture)
    const schoollife   = new PIXI.Sprite(schoollifeInactiveTexture)
    const trust        = new PIXI.Sprite(trustInactiveTexture)
    const teamwork     = new PIXI.Sprite(teamworkInactiveTexture)

    // set sprite coordinates
    dot.x = 360
    dot.y = 300
    community.x = 220
    community.y = 60
    learning.x = 650
    learning.y = 230
    schoollife.x = 710
    schoollife.y = 430
    trust.x = 510
    trust.y = 0
    teamwork.x = 0
    teamwork.y = 350

    // set interactivity
    dot.interactive = false
    dot.buttonMode = false
    community.interactive   = true
    community.buttonMode    = true
    learning.interactive   = true
    learning.buttonMode    = true
    schoollife.interactive   = true
    schoollife.buttonMode    = true
    trust.interactive   = true
    trust.buttonMode    = true
    teamwork.interactive   = true
    teamwork.buttonMode    = true

    // setup eventhanlder
    community.on('pointerdown', () => {
        active = 'community'
        showContent()
    })
    community.on('pointerover', (event) => {
        community.texture = communityActiveTexture
    })
    community.on('pointerout', () => {
        community.texture = communityInactiveTexture
    })

    learning.on('pointerdown', () => {
        active = 'learning'
        showContent()
    })
    learning.on('pointerover', (event) => {
        learning.texture = learningActiveTexture
    })
    learning.on('pointerout', () => {
        learning.texture = learningInactiveTexture
    })

    schoollife.on('pointerdown', () => {
        active = 'schoollife'
        showContent()
    })
    schoollife.on('pointerover', (event) => {
        schoollife.texture = schoollifeActiveTexture
    })
    schoollife.on('pointerout', () => {
        schoollife.texture = schoollifeInactiveTexture
    })

    trust.on('pointerdown', () => {
        active = 'trust'
        showContent()
    })
    trust.on('pointerover', (event) => {
        trust.texture = trustActiveTexture
    })
    trust.on('pointerout', () => {
        trust.texture = trustInactiveTexture
    })

    teamwork.on('pointerdown', () => {
        active = 'teamwork'
        showContent()
    })
    teamwork.on('pointerover', (event) => {
        teamwork.texture = teamworkActiveTexture
    })
    teamwork.on('pointerout', () => {
        teamwork.texture = teamworkInactiveTexture
    })

    // add sprites to stage
    app.stage.addChild(dot)
    app.stage.addChild(community)
    app.stage.addChild(learning)
    app.stage.addChild(schoollife)
    app.stage.addChild(trust)
    app.stage.addChild(teamwork)

})

