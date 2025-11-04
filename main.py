@namespace
class SpriteKind:
    LeftPaddle = SpriteKind.create()
    RightPaddle = SpriteKind.create()
def create_right_paddle():
    global right_paddle
    right_paddle = sprites.create(img("""
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            """),
        SpriteKind.RightPaddle)
    controller.player2.move_sprite(right_paddle, 0, 150)
    right_paddle.right = 160
    right_paddle.set_stay_in_screen(True)

def on_on_overlap(sprite, otherSprite):
    sprite.vx = sprite.vx * -1
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.LeftPaddle, on_on_overlap)

def create_left_paddle():
    global left_paddle
    left_paddle = sprites.create(img("""
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . a . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            . . . . . . . 8 . . . . . . . .
            """),
        SpriteKind.LeftPaddle)
    controller.move_sprite(left_paddle, 0, 150)
    left_paddle.left = 0
    left_paddle.set_stay_in_screen(True)
def create_ball():
    global ball
    ball = sprites.create(img("""
            . . . . . . . e e e e . . . . .
            . . . . . e e 4 5 5 5 e e . . .
            . . . . e 4 5 6 2 2 7 6 6 e . .
            . . . e 5 6 6 7 2 2 6 4 4 4 e .
            . . e 5 2 2 7 6 6 4 5 5 5 5 4 .
            . e 5 6 2 2 8 8 5 5 5 5 5 4 5 4
            . e 5 6 7 7 8 5 4 5 4 5 5 5 5 4
            e 4 5 8 6 6 5 5 5 5 5 5 4 5 5 4
            e 5 c e 8 5 5 5 4 5 5 5 5 5 5 4
            e 5 c c e 5 4 5 5 5 4 5 5 5 e .
            e 5 c c 5 5 5 5 5 5 5 5 4 e . .
            e 5 e c 5 4 5 4 5 5 5 e e . . .
            e 5 e e 5 5 5 5 5 4 e . . . . .
            4 5 4 e 5 5 5 5 e e . . . . . .
            . 4 5 4 5 5 4 e . . . . . . . .
            . . 4 4 e e e . . . . . . . . .
            """),
        SpriteKind.player)
    ball.set_velocity(100, 100)
    ball.set_bounce_on_wall(True)
    ball.y = randint(0, 120)
ball: Sprite = None
left_paddle: Sprite = None
right_paddle: Sprite = None
create_ball()
create_left_paddle()
create_right_paddle()