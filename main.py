@namespace
class SpriteKind:
    Coin = SpriteKind.create()

def on_overlap_tile(sprite, location):
    global Level
    Level += 1
    if Level <= LevelCount:
        GenerateMap()
    else:
        game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def InitFlower():
    global flower
    for 值 in tiles.get_tiles_by_type(assets.tile("""
        myTile3
    """)):
        flower = sprites.create(img("""
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
            """),
            SpriteKind.food)
        tiles.place_on_tile(flower, 值)
        tiles.set_tile_at(值, assets.tile("""
            transparency16
        """))
def InitMapObj():
    InitMonkey()
    InitCoin()
    InitFlower()

def on_overlap_tile2(sprite, location):
    game.over(False, effects.hearts)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.coral5, on_overlap_tile2)

def on_on_overlap(sprite, otherSprite):
    info.change_score_by(randint(50, 99))
    otherSprite.destroy(effects.fountain, 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap)

def GenerateMap():
    DestroyObj()
    if Level == 1:
        tiles.set_tilemap(tilemap("""
            级别1
        """))
    elif Level == 2:
        tiles.set_tilemap(tilemap("""
            级别3
        """))
    elif Level == 3:
        tiles.set_tilemap(tilemap("""
            级别4
        """))
    InitMapObj()

def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -165
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def DestroyObj():
    for 值2 in sprites.all_of_kind(SpriteKind.Coin):
        值2.destroy()
    for 值3 in sprites.all_of_kind(SpriteKind.food):
        值3.destroy()
    for 值4 in sprites.all_of_kind(SpriteKind.enemy):
        值4.destroy()

def on_overlap_tile3(sprite, location):
    game.over(False, effects.hearts)
scene.on_overlap_tile(SpriteKind.player, sprites.builtin.coral4, on_overlap_tile3)

def InitMonkey():
    for 值5 in tiles.get_tiles_by_type(assets.tile("""
        myTile1
    """)):
        tiles.place_on_tile(mySprite, 值5)
        tiles.set_tile_at(值5, assets.tile("""
            transparency16
        """))
def InitCoin():
    global coins
    for 值6 in tiles.get_tiles_by_type(assets.tile("""
        myTile2
    """)):
        coins = sprites.create(img("""
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
            """),
            SpriteKind.Coin)
        animation.run_image_animation(coins,
            [img("""
                    . . b b b b . . 
                                . b 5 5 5 5 b . 
                                b 5 d 3 3 d 5 b 
                                b 5 3 5 5 1 5 b 
                                c 5 3 5 5 1 d c 
                                c d d 1 1 d d c 
                                . f d d d d f . 
                                . . f f f f . .
                """),
                img("""
                    . . b b b . . . 
                                . b 5 5 5 b . . 
                                b 5 d 3 d 5 b . 
                                b 5 3 5 1 5 b . 
                                c 5 3 5 1 d c . 
                                c 5 d 1 d d c . 
                                . f d d d f . . 
                                . . f f f . . .
                """),
                img("""
                    . . . b b . . . 
                                . . b 5 5 b . . 
                                . b 5 d 1 5 b . 
                                . b 5 3 1 5 b . 
                                . c 5 3 1 d c . 
                                . c 5 1 d d c . 
                                . . f d d f . . 
                                . . . f f . . .
                """),
                img("""
                    . . . b b . . . 
                                . . b 5 5 b . . 
                                . . b 1 1 b . . 
                                . . b 5 5 b . . 
                                . . b d d b . . 
                                . . c d d c . . 
                                . . c 3 3 c . . 
                                . . . f f . . .
                """),
                img("""
                    . . . b b . . . 
                                . . b 5 5 b . . 
                                . b 5 1 d 5 b . 
                                . b 5 1 3 5 b . 
                                . c d 1 3 5 c . 
                                . c d d 1 5 c . 
                                . . f d d f . . 
                                . . . f f . . .
                """),
                img("""
                    . . . b b b . . 
                                . . b 5 5 5 b . 
                                . b 5 d 3 d 5 b 
                                . b 5 1 5 3 5 b 
                                . c d 1 5 3 5 c 
                                . c d d 1 d 5 c 
                                . . f d d d f . 
                                . . . f f f . .
                """)],
            100,
            True)
        tiles.place_on_tile(coins, 值6)
        tiles.set_tile_at(值6, assets.tile("""
            transparency16
        """))

def on_on_overlap2(sprite, otherSprite):
    global bat
    otherSprite.destroy(effects.cool_radial, 500)
    bat = sprites.create(img("""
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
        """),
        SpriteKind.enemy)
    animation.run_image_animation(bat,
        [img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """),
            img("""
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
            """)],
        100,
        True)
    bat.set_position(otherSprite.x + 80, otherSprite.y - 80)
    bat.follow(mySprite, 50)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    otherSprite.destroy(effects.disintegrate, 500)
    if sprite.vy > 0 and sprite.y <= otherSprite.y:
        info.change_score_by(3)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap3)

bat: Sprite = None
coins: Sprite = None
flower: Sprite = None
LevelCount = 0
Level = 0
mySprite: Sprite = None
scene.set_background_color(0)
effects.blizzard.start_screen_effect()
mySprite = sprites.create(img("""
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
    """),
    SpriteKind.player)
animation.run_image_animation(mySprite,
    assets.animation("""
        villager1WalkRight
    """),
    100,
    True)
controller.move_sprite(mySprite, 100, 0)
mySprite.ay = 400
scene.camera_follow_sprite(mySprite)
Level = 1
LevelCount = 3
info.set_score(0)
info.set_life(4)
GenerateMap()