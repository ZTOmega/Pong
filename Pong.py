# Pong game by Eclizanto
# utilizando a biblioteca/modulo turtle

import turtle
import winsound
import time

wn = turtle.Screen()
wn.title("Pong by Eclizanto")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Função Element "Um elemento do jogo"
def element(widht, length, xLoc, yLoc):
    element = turtle.Turtle()
    element.speed(0)
    element.shape("square")
    element.color("white")
    element.shapesize(stretch_wid=widht, stretch_len=length)
    element.penup()
    element.goto(xLoc, yLoc)
    return element

# Paddle A
paddleA = element(5, 1, -350, 0)

# Paddle B
paddleB = element(5, 1, 350, 0)

# Ball
ball = element(1, 1, 0, 0)
ballSpeedX = -3
ballSpeedY = 3

# Rede
web = element(28, 0.1, 0, 0)

# Parede de Cima
wallUp = element(1, 40, 0, 280)

# Parede de Baixo
wallDown = element(1, 40, 0, -280)

# Score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 180)

# Pontuação inicial
scoreA = 0
scoreB = 0

# Função pontuação Atualizada
def scoreUpdate(scoreA, scoreB):
    score.clear()
    score.write("{}        {}".format(scoreA, scoreB), align="center", font=("Arial", 40, "bold"))

# Exibir pontuação inicial
scoreUpdate(scoreA, scoreB)

# Função Som
def soundPaddle():
    winsound.PlaySound("bounce", winsound.SND_ASYNC)

def soundBorder():
    winsound.PlaySound("8-bit-bounce", winsound.SND_ASYNC)

def soundExit():
    winsound.PlaySound("jumping", winsound.SND_ASYNC)

def soundPoint():
    winsound.PlaySound("8-bit-powerup", winsound.SND_ASYNC)


# Função Mover Paddle para Cima e limite das Bordas
def paddleUp(paddle):
    if paddle.ycor() < 220 and paddle.ycor() >= -220:
        y = paddle.ycor()
        y += 20
        paddle.sety(y)

# Função Mover Paddle para Baixo e limite das Bordas
def paddleDown(paddle):
    if paddle.ycor() <= 220 and paddle.ycor() > -220:
        y = paddle.ycor()
        y -= 20
        paddle.sety(y)


# Imputs do teclado
wn.listen()

# Player 1
# Cima
wn.onkeypress(lambda p=paddleA: paddleUp(p), "w"), wn.onkeypress(lambda p=paddleA: paddleUp(p), "W")
# Baixo
wn.onkeypress(lambda p=paddleA: paddleDown(p), "s"), wn.onkeypress(lambda p=paddleA: paddleDown(p), "S")

# Player 2
# Cima
wn.onkeypress(lambda p=paddleB: paddleUp(p), "Up")
# Baixo
wn.onkeypress(lambda p=paddleB: paddleDown(p), "Down")


# Main game loop
while True:
    wn.update()

    # Move a bola
    ball.setx(ball.xcor() + ballSpeedX)
    ball.sety(ball.ycor() + ballSpeedY)

    #C olisão bola e Borbas
    if ball.ycor() > 260:
        ball.sety(260)
        ballSpeedY *= -1
        soundBorder()

    if ball.ycor() < -260:
        ball.sety(-260)
        ballSpeedY *= -1
        soundBorder()


    # Bola Sai e pontua
    # Saida Direita
    if ball.xcor() > 420:
        soundExit()
        for sec in range(1):
            time.sleep(1)
            if sec == 0:
                soundPoint()
                scoreA += 1
                scoreUpdate(scoreA, scoreB)
                ball.goto(0, 0)
                ballSpeedX *= -1

    # Saida Esquerda
    if ball.xcor() < -420:
        soundExit()
        for sec in range(1):
            time.sleep(1)
            if sec == 0:
                soundPoint()
                scoreB += 1
                scoreUpdate(scoreA, scoreB)
                ball.goto(0, 0)
                ballSpeedX *= -1

    # Colisão bola e Raquetes
    if (ball.xcor() < -335 and ball.xcor() > -340) and (ball.ycor() < paddleA.ycor() + 60 and ball.ycor() > paddleA.ycor() - 60):
        ballSpeedX *= -1
        soundPaddle()

    if (ball.xcor() > 335 and ball.xcor() < 340) and (ball.ycor() < paddleB.ycor() + 60 and ball.ycor() > paddleB.ycor() - 60):
        ballSpeedX *= -1
        soundPaddle()