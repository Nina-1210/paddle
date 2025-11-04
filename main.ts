namespace SpriteKind {
    export const LeftPaddle = SpriteKind.create()
    export const RightPaddle = SpriteKind.create()
}

function create_right_paddle() {
    
    right_paddle = sprites.create(img`
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
            `, SpriteKind.RightPaddle)
    controller.player2.moveSprite(right_paddle, 0, 150)
    right_paddle.right = 160
    right_paddle.setStayInScreen(true)
}

sprites.onOverlap(SpriteKind.Player, SpriteKind.LeftPaddle, function on_on_overlap(sprite: Sprite, otherSprite: Sprite) {
    sprite.vx = sprite.vx * -1
    info.changeScoreBy(1)
})
function create_left_paddle() {
    
    left_paddle = sprites.create(img`
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
            `, SpriteKind.LeftPaddle)
    controller.moveSprite(left_paddle, 0, 150)
    left_paddle.left = 0
    left_paddle.setStayInScreen(true)
}

function create_ball() {
    
    ball = sprites.create(img`
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
            `, SpriteKind.Player)
    ball.setVelocity(100, 100)
    ball.setBounceOnWall(true)
    ball.y = randint(0, 120)
}

let ball : Sprite = null
let left_paddle : Sprite = null
let right_paddle : Sprite = null
create_ball()
create_left_paddle()
create_right_paddle()
