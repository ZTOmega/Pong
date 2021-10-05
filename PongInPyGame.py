# Pong em PyGame By Eclizanto

import pygame, sys, random, winsound, pygame.freetype

# Animações
def ballAnimation():
    global ballSpeedX, ballSpeedY, scoreAI, scoreP, opponentSpeed
    # Movimento da bola
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Colisão Bordas
    if ball.top <= 15 or ball.bottom >= screenHeight - 15:
        ballSpeedY *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)
    # Ball Exit - Pontuação
    if ball.right <= 0:
        scoreP +=1
        scorePoint(scoreAI, scoreP)
        opponentSpeed = 21
        ballRestart()
        winsound.PlaySound("8-bit-powerup", winsound.SND_ASYNC)
    if ball.left >= screenWidth:
        scoreAI +=1
        scorePoint(scoreAI, scoreP)
        opponentSpeed = 7
        ballRestart()
        winsound.PlaySound("8-bit-powerup", winsound.SND_ASYNC)
    # Colisão Padles
    if ball.colliderect(player) or ball.colliderect(opponent):
        ballSpeedX *= -1
        winsound.PlaySound("bounce", winsound.SND_ASYNC)

def playerAnimation():
    player.y += playerSpeed
    if player.top <= 15:
        player.top = 15
    if player.bottom >= screenHeight - 15:
        player.bottom = screenHeight - 15

def opponentAI():
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponentSpeed
    if opponent.top <= 15:
        opponent.top = 15
    if opponent.bottom >= screenHeight - 15:
        opponent.bottom = screenHeight - 15

def ballRestart():
    global ballSpeedX, ballSpeedY
    ball.center = (screenWidth/2, screenHeight/2)
    ballSpeedY *= random.choice((1,-1))
    ballSpeedX *= random.choice((1,-1))

def scorePoint(scoreAI, scoreP):
    gameFont.render_to(screen, (315, 40), "{}      {}".format(scoreAI, scoreP), paddleColor)

# Cor Gradiente
def gradient(screen, topColor, bottomColor, gradientScale):
    gradientSurf = pygame.Surface((2,2)) # 2x2 BitMap
    pygame.draw.line(gradientSurf, topColor, (0, 0), (1, 0)) # Cor da linha Esquerda
    pygame.draw.line(gradientSurf, bottomColor, (0, 1), (1, 1)) # Cor da linha Direita
    gradientSurf = pygame.transform.smoothscale(gradientSurf, (gradientScale.width, gradientScale.height)) # Aumenta a Escala
    screen.blit(gradientSurf, gradientScale) #  Posiciona/Desenha
    return gradientSurf

scoreAI = 0
scoreP = 0

# Setup Geral
pygame.init()
clock = pygame.time.Clock()

# Tela
screenWidth = 880
screenHeight = 660
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pong by Eclizanto")
gameFont = pygame.freetype.Font("Aldrich-Regular.ttf", 80)

# Retangulos
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30, 30)
player = pygame.Rect(screenWidth-20, screenHeight/2-70, 15, 140)
opponent = pygame.Rect(20, screenHeight/2-70, 15, 140)
wallTop = pygame.Rect(0, 0, 880, 15)
wallBotton = pygame.Rect(0, 645, 880, 15)
screenRect = pygame.Rect(0,0, 880,660)
#score = pygame.Surface((100,100))

# Cores
bgColor = pygame.Color(0,35,0)
paddleColor = pygame.Color(180, 255, 200)
paddleColor2 = pygame.Color(20, 200, 150)
ballColor = pygame.Color(255, 255, 180)
screenRectColorTop = (0,35,0)
screenRectColorBottom = (0,70,0)

# Velocidade
ballSpeedX = 7 * random.choice((1,-1))
ballSpeedY = 7 * random.choice((1,-1))
playerSpeed = 0
opponentSpeed = 7

# Game Update
while True:
    # imputs do Usuario
    for event in pygame.event.get():
        # Sair do Jogo
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Imputs do Teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7
            if event.key == pygame.K_UP:
                playerSpeed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7

    ballAnimation()
    playerAnimation()
    opponentAI()

    # Draw Visual
    #screen.fill(bgColor)
    gradient(screen, screenRectColorTop, screenRectColorBottom, screenRect)
    pygame.draw.rect(screen, paddleColor, player, 6, 10)
    pygame.draw.rect(screen, paddleColor, opponent, 6, 10)
    pygame.draw.ellipse(screen, ballColor, ball, 10)
    pygame.draw.aaline(screen, paddleColor,(screenWidth/2,0), (screenWidth/2,screenHeight))
    pygame.draw.rect(screen, paddleColor, wallTop)
    pygame.draw.rect(screen, paddleColor, wallBotton)
    scorePoint(scoreAI,scoreP)
    #score, rect = gameFont.render("0  0000000", (255, 255, 255))
    #screen.blit(score,(screenWidth/2 - 50, screenHeight/2 - 50))
    #gradient(screen, paddleColor, paddleColor2, player)


    # Atualização da Tela
    pygame.display.flip()
    clock.tick(60)