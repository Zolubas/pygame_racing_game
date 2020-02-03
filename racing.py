import pygame
pygame.init()
pygame.mixer.music.load('tokyodrift8bit.mp3')
pygame.mixer.music.play(-1)
x = 400
y = 300
velocidade = 10 # 10 pixels
fundo = pygame.image.load('estrada.png')
carro = pygame.image.load('carro.png')

janela = pygame.display.set_mode((640,700))
pygame.display.set_caption("Car game")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))
    #pygame.draw.circle(janela, (0,10,90),(x,y),50)
    pygame.display.update()
