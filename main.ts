namespace SpriteKind {
    export const Coin = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile0`, function (sprite, location) {
    Level += 1
    if (Level <= LevelCount) {
        GenerateMap()
    } else {
        game.over(true, effects.confetti)
    }
})
function InitFlower () {
    for (let 值 of tiles.getTilesByType(assets.tile`myTile3`)) {
        flower = sprites.create(img`
            . . . . . . . . 
            . . . . . . . . 
            . . . . . . . . 
            . . c c c . . . 
            . c c 6 6 c . . 
            c c 3 3 f 6 c . 
            c 6 c f 6 3 c . 
            c 3 6 3 3 3 c . 
            c 3 6 6 3 3 c . 
            c 3 3 6 6 3 c . 
            . c 3 3 3 6 . . 
            . . 6 7 6 . . . 
            . . 6 6 8 8 8 6 
            . . 6 8 7 7 7 6 
            . . 8 7 7 7 6 . 
            . . 8 8 8 6 . . 
            `, SpriteKind.Food)
        tiles.placeOnTile(flower, 值)
        tiles.setTileAt(值, assets.tile`transparency16`)
    }
}
function InitMapObj () {
    InitMonkey()
    InitCoin()
    InitFlower()
}
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.coral5, function (sprite, location) {
    game.over(false, effects.hearts)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Coin, function (sprite, otherSprite) {
    info.changeScoreBy(randint(50, 99))
    otherSprite.destroy(effects.fountain, 200)
})
function GenerateMap () {
    DestroyObj()
    if (Level == 1) {
        tiles.setTilemap(tilemap`级别1`)
    } else if (Level == 2) {
        tiles.setTilemap(tilemap`级别3`)
    } else if (Level == 3) {
        tiles.setTilemap(tilemap`级别4`)
    }
    InitMapObj()
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        mySprite.vy = -165
    }
})
function DestroyObj () {
    for (let 值2 of sprites.allOfKind(SpriteKind.Coin)) {
        值2.destroy()
    }
    for (let 值3 of sprites.allOfKind(SpriteKind.Food)) {
        值3.destroy()
    }
    for (let 值4 of sprites.allOfKind(SpriteKind.Enemy)) {
        值4.destroy()
    }
}
scene.onOverlapTile(SpriteKind.Player, sprites.builtin.coral4, function (sprite, location) {
    game.over(false, effects.hearts)
})
function InitMonkey () {
    for (let 值5 of tiles.getTilesByType(assets.tile`myTile1`)) {
        tiles.placeOnTile(mySprite, 值5)
        tiles.setTileAt(值5, assets.tile`transparency16`)
    }
}
function InitCoin () {
    for (let 值6 of tiles.getTilesByType(assets.tile`myTile2`)) {
        coins = sprites.create(img`
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 f 5 5 5 5 5 5 5 5 5 f 5 5 
            5 5 5 f 5 5 5 5 f f 5 5 5 f 5 5 
            5 5 f f f f 5 5 5 f 5 5 5 5 5 5 
            5 5 f 5 5 5 5 5 f f f 5 5 5 5 5 
            5 f f 5 f f 5 5 5 f 5 5 5 5 5 5 
            5 5 5 5 5 f 5 5 5 5 f f 5 5 5 5 
            5 5 5 5 f f f f f f f f 5 5 5 5 
            5 5 5 5 f 5 5 f 5 5 5 f 5 5 5 5 
            5 5 5 5 f 5 f f 5 5 5 f 5 5 5 5 
            5 5 5 5 f f 5 5 5 5 5 f f f 5 5 
            5 5 5 5 f f 5 f 5 f f f f 5 f 5 
            5 5 5 5 5 5 5 f f 5 5 5 f 5 f 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 f f 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            `, SpriteKind.Coin)
        animation.runImageAnimation(
        coins,
        [img`
            . . b b b b . . 
            . b 5 5 5 5 b . 
            b 5 d 3 3 d 5 b 
            b 5 3 5 5 1 5 b 
            c 5 3 5 5 1 d c 
            c d d 1 1 d d c 
            . f d d d d f . 
            . . f f f f . . 
            `,img`
            . . b b b . . . 
            . b 5 5 5 b . . 
            b 5 d 3 d 5 b . 
            b 5 3 5 1 5 b . 
            c 5 3 5 1 d c . 
            c 5 d 1 d d c . 
            . f d d d f . . 
            . . f f f . . . 
            `,img`
            . . . b b . . . 
            . . b 5 5 b . . 
            . b 5 d 1 5 b . 
            . b 5 3 1 5 b . 
            . c 5 3 1 d c . 
            . c 5 1 d d c . 
            . . f d d f . . 
            . . . f f . . . 
            `,img`
            . . . b b . . . 
            . . b 5 5 b . . 
            . . b 1 1 b . . 
            . . b 5 5 b . . 
            . . b d d b . . 
            . . c d d c . . 
            . . c 3 3 c . . 
            . . . f f . . . 
            `,img`
            . . . b b . . . 
            . . b 5 5 b . . 
            . b 5 1 d 5 b . 
            . b 5 1 3 5 b . 
            . c d 1 3 5 c . 
            . c d d 1 5 c . 
            . . f d d f . . 
            . . . f f . . . 
            `,img`
            . . . b b b . . 
            . . b 5 5 5 b . 
            . b 5 d 3 d 5 b 
            . b 5 1 5 3 5 b 
            . c d 1 5 3 5 c 
            . c d d 1 d 5 c 
            . . f d d d f . 
            . . . f f f . . 
            `],
        100,
        true
        )
        tiles.placeOnTile(coins, 值6)
        tiles.setTileAt(值6, assets.tile`transparency16`)
    }
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    otherSprite.destroy(effects.coolRadial, 500)
    bat = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Enemy)
    animation.runImageAnimation(
    bat,
    [img`
        . . f f f . . . . . . . . f f f 
        . f f c c . . . . . . f c b b c 
        f f c c . . . . . . f c b b c . 
        f c f c . . . . . . f b c c c . 
        f f f c c . c c . f c b b c c . 
        f f c 3 c c 3 c c f b c b b c . 
        f f b 3 b c 3 b c f b c c b c . 
        . c b b b b b b c b b c c c . . 
        . c 1 b b b 1 b b c c c c . . . 
        c b b b b b b b b b c c . . . . 
        c b c b b b c b b b b f . . . . 
        f b 1 f f f 1 b b b b f c . . . 
        f b b b b b b b b b b f c c . . 
        . f b b b b b b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        `,img`
        . . f f f . . . . . . . . . . . 
        f f f c c . . . . . . . . f f f 
        f f c c . . c c . . . f c b b c 
        f f c 3 c c 3 c c f f b b b c . 
        f f b 3 b c 3 b c f b b c c c . 
        . c b b b b b b c f b c b c c . 
        . c b b b b b b c b b c b b c . 
        c b 1 b b b 1 b b b c c c b c . 
        c b b b b b b b b c c c c c . . 
        f b c b b b c b b b b f c . . . 
        f b 1 f f f 1 b b b b f c c . . 
        . f b b b b b b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `,img`
        . . . . . . . . . . . . . . . . 
        . . c c . . c c . . . . . . . . 
        . . c 3 c c 3 c c c . . . . . . 
        . c b 3 b c 3 b c c c . . . . . 
        . c b b b b b b b b f f . . . . 
        c c b b b b b b b b f f . . . . 
        c b 1 b b b 1 b b c f f f . . . 
        c b b b b b b b b f f f f . . . 
        f b c b b b c b c c b b b . . . 
        f b 1 f f f 1 b f c c c c . . . 
        . f b b b b b b f b b c c . . . 
        c c f b b b b b c c b b c . . . 
        c c c f f f f f f c c b b c . . 
        . c c c . . . . . . c c c c c . 
        . . c c c . . . . . . . c c c c 
        . . . . . . . . . . . . . . . . 
        `,img`
        . f f f . . . . . . . . f f f . 
        f f c . . . . . . . f c b b c . 
        f c c . . . . . . f c b b c . . 
        c f . . . . . . . f b c c c . . 
        c f f . . . . . f f b b c c . . 
        f f f c c . c c f b c b b c . . 
        f f f c c c c c f b c c b c . . 
        . f c 3 c c 3 b c b c c c . . . 
        . c b 3 b c 3 b b c c c c . . . 
        c c b b b b b b b b c c . . . . 
        c b 1 b b b 1 b b b b f c . . . 
        f b b b b b b b b b b f c c . . 
        f b c b b b c b b b b f . . . . 
        . f 1 f f f 1 b b b c f . . . . 
        . . f b b b b b b c f . . . . . 
        . . . f f f f f f f . . . . . . 
        `],
    100,
    true
    )
    bat.setPosition(otherSprite.x + 80, otherSprite.y - 80)
    bat.follow(mySprite, 50)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy(effects.disintegrate, 500)
    if (sprite.vy > 0 && sprite.y <= otherSprite.y) {
        info.changeScoreBy(3)
    } else {
        info.changeLifeBy(-1)
    }
})
let bat: Sprite = null
let coins: Sprite = null
let flower: Sprite = null
let LevelCount = 0
let Level = 0
let mySprite: Sprite = null
scene.setBackgroundColor(0)
effects.blizzard.startScreenEffect()
mySprite = sprites.create(img`
    . . . . . . . f f f f f . . . . 
    . . . . . . f e e e e e f . . . 
    . . . . . f e e e d d d d f . . 
    . . . . f f e e d f d d f d c . 
    . . . f d d e e d f d d f d c . 
    . . . c d b e e d d d d e e d c 
    f f . c d b e e d d c d d d d c 
    f e f . c f e e d d d c c c c c 
    f e f . . f f e e d d d d d f . 
    f e f . f e e e e f f f f f . . 
    f e f f e e e e e e e f . . . . 
    . f f e e e e f e f f e f . . . 
    . . f e e e e f e f f e f . . . 
    . . . f e f f b d f b d f . . . 
    . . . f d b b d d c d d f . . . 
    . . . f f f f f f f f f . . . . 
    `, SpriteKind.Player)
animation.runImageAnimation(
mySprite,
assets.animation`villager1WalkRight`,
100,
true
)
controller.moveSprite(mySprite, 100, 0)
mySprite.ay = 400
scene.cameraFollowSprite(mySprite)
Level = 1
LevelCount = 3
info.setScore(0)
info.setLife(4)
GenerateMap()
