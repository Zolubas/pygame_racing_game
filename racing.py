import pygame
pygame.init()
pygame.mixer.music.load('tokyodrift8bit.mp3')
pygame.mixer.music.play(-1)
x = 400
y = 300
velocidade = 10 # 10 pixels
#fundo = pygame.image.load('estrada.png')
fundo = pygame.image.load('racecity.png')

carw = pygame.image.load('carw.png')
card = pygame.image.load('card.png')
cars = pygame.image.load('cars.png')
cara = pygame.image.load('cara.png')
carwd = pygame.image.load('carwd.png')
cards = pygame.image.load('cards.png')
carsa = pygame.image.load('carsa.png')
caraw = pygame.image.load('caraw.png')

car = carw

janela = pygame.display.set_mode((1040,750))
pygame.display.set_caption("Tokyo Drift - Possani Turbo Society")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        car = carw
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        car = cars
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        car = card
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        car = cara
        x-= velocidade
        #=======================
    #if comandos[pygame.K_KP9]:
    #    car = carwd
    #    y-= velocidade*0.7
    #    x+= velocidade*0.7
    #if comandos[pygame.K_KP3]:
    #    car = cards
    #    y+= velocidade*0.7
    #    x+= velocidade*0.7
    #if comandos[pygame.K_KP1]:
    #    car = carsa
    #    x-= velocidade*0.7
    #    y+= velocidade*0.7
    #if comandos[pygame.K_KP7]:
    #    car = caraw
    #    x-= velocidade*0.7
    #    y-= velocidade*0.7


    janela.blit(fundo, (0,0))
    janela.blit(car, (x,y))
    #pygame.draw.circle(janela, (0,10,90),(x,y),50)
    pygame.display.update()
