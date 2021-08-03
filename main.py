@namespace
class SpriteKind:
    boost = SpriteKind.create()
    shield = SpriteKind.create()

def on_b_pressed():
    game.set_dialog_text_color(0)
    game.set_dialog_frame(img("""
        999999999999999999999999999999999999999999999999
                9999fff9999999999999fff9999999999999fff999999999
                99fffffff999ffff99fffffff999ffff99fffffff999fff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffff8fffffffffffffffffffffffffffff8fffffffff9
                9ffffff88ffffffffffffffffffffffffffff88ffffffff9
                9fffff88889fffffffffffffffffffffffff88889ffffff9
                9fffff888888ffffffffffffffffffffffff888888fffff9
                9ffffff88ffffffffffffffffffffffffffff88ffffffff9
                9ffffff8fffffffffffffffffffffffffffff8fffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ffffffffffffffffffffffffffffffffffffffffffffff9
                9ff6fffffffffffffffffffffffffffffffffffff6fffff9
                9ff6ffffffff6fffffffffffffffffffff6fffff66fffff9
                9ff66fffffff66ffffffffffffffffffff6ffffff6fff6f9
                9666ffffffff6ffffffffffffff6ffffff66ffff666ff6f9
                9f666ffffff666ffff6ffffffff6fffff66fffff66ff66f9
                9ff666ffffff6fffff6fffffff666fffff66fff6666ff6f9
                9666ffffff66666fff66ffffff66ffffff666fff66ff6669
                9f6666ffff6666fff6666ffff66666ff666ffff6666f66f9
                9f6666ffff6666ffff66ffffff66fffff666fff666666669
                96666ffff666666ff6666ffff66666ff6666f66666666669
                9f66ffff666666fff6666fff66666fff6666666666666669
                9666666ff666666666666666666666666666666666666669
                966666ff6666666666666666666666666666666666666669
                966666666666666666666666666666666666666666666669
                999999999999999999999999999999999999999999999999
    """))
    game.show_long_text("You are a survivor and are fighting your enemies! Defeat enemy ships to score points! Spaceships drop life boost, shield and 2x rewards sometimes...",
        DialogLayout.FULL)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_countdown_end():
    global shield_boost
    shield_boost = 0
info.on_countdown_end(on_countdown_end)

def on_on_zero(status):
    status.sprite_attached_to().destroy()
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_on_overlap(sprite, otherSprite):
    if statusbar.value < 100:
        otherSprite.destroy(effects.confetti, 100)
        info.change_life_by(1)
        statusbar.value += 34
    else:
        if statusbar.value == 100:
            otherSprite.destroy()
            Space.say("Life count max", 200)
sprites.on_overlap(SpriteKind.player, SpriteKind.boost, on_on_overlap)

def on_a_released():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        galgaDart0
    """), Space, 300, 0)
    animation.run_image_animation(projectile,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . 8 8 . . . . . . . . . . . 
                        . . . 8 6 8 . . 8 8 . . . . . . 
                        2 . . 8 6 6 8 . 8 6 8 . . . . . 
                        4 2 8 8 8 8 8 8 8 8 8 8 8 . . . 
                        5 2 8 6 6 6 6 6 6 8 4 4 8 8 8 8 
                        4 2 8 8 8 8 8 8 8 8 8 8 8 . . . 
                        2 . . 8 6 6 8 . 8 6 8 . . . . . 
                        . . . 8 6 8 . . 8 8 . . . . . . 
                        . . . 8 8 . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . 8 8 . . . . . . . . . . . 
                        . . . 8 6 8 . . 8 8 . . . . . . 
                        . . . 8 6 6 8 . 8 6 8 . . . . . 
                        . . 8 8 8 8 8 8 8 8 8 8 8 . . . 
                        . . 8 6 6 6 6 6 6 8 4 4 8 8 8 8 
                        . . 8 8 8 8 8 8 8 8 8 8 8 . . . 
                        . . . 8 6 6 8 . 8 6 8 . . . . . 
                        . . . 8 6 8 . . 8 8 . . . . . . 
                        . . . 8 8 . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        50,
        True)
    music.small_crash.play()
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

def on_on_overlap2(sprite, otherSprite):
    global shield_boost
    sprite.destroy(effects.fire, 100)
    scene.camera_shake(8, 500)
    music.beam_up.play()
    Space.say("Oh no!", 200)
    if shield_boost == 0:
        info.change_life_by(-1)
        statusbar.value += -34
        statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
    if shield_boost == 1:
        info.change_life_by(0)
        statusbar.value += 0
        shield_boost = 0
        info.stop_countdown()
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap2)

def on_on_overlap3(sprite, otherSprite):
    global shield_boost
    shield_boost += 1
    otherSprite.destroy()
    info.start_countdown(10)
sprites.on_overlap(SpriteKind.player, SpriteKind.shield, on_on_overlap3)

def on_on_overlap4(sprite, otherSprite):
    global boost2, shield2
    statusbars.get_status_bar_attached_to(StatusBarKind.enemy_health, otherSprite).value += -34
    sprite.destroy(effects.fire, 200)
    music.big_crash.play()
    info.change_score_by(1)
    if Math.percent_chance(15):
        boost2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . 1 1 1 1 1 . . 1 1 1 1 1 . . 
                            . 1 f f f f f 1 1 f f f f f 1 . 
                            1 f f 3 3 3 f f f f 3 3 3 f f 1 
                            1 f 3 2 2 2 2 f f 2 2 2 2 3 f 1 
                            1 f 3 2 2 2 2 2 2 2 1 1 2 3 f 1 
                            1 f 3 2 2 2 2 2 2 2 1 1 2 3 f 1 
                            1 f 3 2 2 2 2 2 2 2 2 2 2 3 f 1 
                            1 f f 3 2 2 2 2 2 2 2 2 2 f f 1 
                            . 1 f f 3 2 2 2 2 2 2 2 f f 1 . 
                            . . 1 f f 3 2 2 2 2 2 f f 1 . . 
                            . . . 1 f f 3 2 2 2 f f 1 . . . 
                            . . . . 1 f f 3 3 f f 1 . . . . 
                            . . . . . 1 f f f f 1 . . . . . 
                            . . . . . . 1 1 1 1 . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.boost)
        boost2.set_position(Space.x, Space.y)
    if Math.percent_chance(5):
        shield2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . 8 8 8 8 8 8 8 8 8 8 8 8 . . 
                            . . 8 6 6 6 6 6 6 6 6 6 6 8 . . 
                            . . 8 6 6 6 6 6 6 6 6 6 6 8 . . 
                            . . 8 6 6 9 9 9 9 9 9 6 6 8 . . 
                            . . 8 6 6 9 9 9 9 9 9 6 6 8 . . 
                            . . 8 6 6 9 9 1 1 9 9 6 6 8 . . 
                            . . 8 6 6 9 9 1 1 9 9 6 6 8 . . 
                            . . 8 6 6 9 9 1 1 9 9 6 6 8 . . 
                            . . 8 6 6 9 9 9 9 9 9 6 6 8 . . 
                            . . 8 6 6 6 9 9 9 9 6 6 6 8 . . 
                            . . . 8 6 6 6 6 6 6 6 6 8 . . . 
                            . . . . 8 6 6 6 6 6 6 8 . . . . 
                            . . . . . 8 8 8 8 8 8 . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.shield)
        shield2.set_position(Space.x, Space.y)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap4)

statusbar2: StatusBarSprite = None
life: Sprite = None
shield2: Sprite = None
boost2: Sprite = None
projectile: Sprite = None
shield_boost = 0
statusbar: StatusBarSprite = None
Space: Sprite = None
effects.star_field.start_screen_effect()
Space = sprites.create(assets.image("""
    RocketMan
"""), SpriteKind.player)
scene.set_background_image(img("""
    ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffff111ffffffffffffffffffffff111fffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffffffff1ffffffffffffffffffffffff1fffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff1ffffff1fff111fff1fffff1f1fff1ff1fff111fffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1fff11fffff1ff1fff1f1f1ffffff11ff1ff1ff1fff1ffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1111111fff111f1fff1f1ffffff1f1f1f1f111f1fff1ffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff11fffff1ff1fff1f1ffffff1f1ff11ff1ff1fff1ffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff1ffffff1fff111ff1ffffff1f1fff1ff1fff111fffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
"""))
controller.move_sprite(Space, 150, 150)
Space.set_stay_in_screen(True)
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.attach_to_sprite(Space)
statusbar.value = 100
statusbar.set_color(7, 2, 11)
statusbar.set_status_bar_flag(StatusBarFlag.SMOOTH_TRANSITION, True)
enemyspeed = -80
shield_boost = 0
info.set_life(3)
if shield_boost > 0:
    Space.set_image(img("""
        ....111.........111111......
                ...19991.......19999991.....
                ..19ccc91...1119ffffff91....
                ..19f6cc9111999fcc88ff91....
                ..19f66cc999fffccccff91.....
                ..19f866cccc88886668cc91....
                ..19f886cc8888888866b9c91...
                ..19cf8888888888888b999c91..
                .19c88c888888888b99999b8c91.
                19f88ccccccc888899999b888c91
                19fffffcc888c888888888888f91
                .199999f8888668888888888f91.
                ..1119f888866fc8888888ff91..
                ...19c888866ffffffffff991...
                ...19c8888cf999999999911....
                ...19ffffff91111111111......
                ....19999991................
                .....111111.................
                ............................
                ............................
    """))
elif shield_boost == 0:
    Space.set_image(img("""
        ............................
                ............................
                ....ccc.........ffffff......
                ....f6cc.......fcc88ff......
                ....f66cc...fffccccff.......
                ....f866cccc88886668cc......
                ....f886cc8888888866b9c.....
                ....cf8888888888888b999c....
                ...c88c888888888b99999b8c...
                ..f88ccccccc888899999b888c..
                ..fffffcc888c888888888888f..
                .......f8888668888888888f...
                ......f888866fc8888888ff....
                .....c888866ffffffffff......
                .....c8888cf................
                .....ffffff.................
                ............................
                ............................
                ............................
                ............................
    """))

def on_update_interval():
    global life, statusbar2, enemyspeed
    life = sprites.create(assets.image("""
        UFO
    """), SpriteKind.enemy)
    life.set_velocity(enemyspeed, 0)
    life.x = scene.screen_width()
    life.y = randint(10, scene.screen_height() - 10)
    life.set_flag(SpriteFlag.AUTO_DESTROY, True)
    statusbar2 = statusbars.create(20, 3, StatusBarKind.enemy_health)
    statusbar2.max = 100
    statusbar2.set_color(5, 12, 11)
    statusbar2.attach_to_sprite(life)
    if info.score() > 49:
        enemyspeed += -15
game.on_update_interval(1000, on_update_interval)
