import pygame
from random import randint
pygame.init()

x = 550  #max 700     min 400 (400<x<700)
y = 150
velocidade = 9
x_amb = 550
y_amb = 1500
vel_amb = randint(6, 8)
x_pol = 400
y_pol = randint(800, 1700)
vel_pol = randint(6, 9)
x_taxi = 700
y_taxi = randint(800, 1700)
vel_taxi = randint(7, 9)
y_grama1 = 0
y_grama2 = 188
y_grama3 = 376
y_grama4 = 564
y_grama5 = 730
vel_pista = 6
fundo = pygame.image.load('pista.png')
carro = pygame.image.load('carro_menor.png')
policia = pygame.image.load('policia.png')
ambulancia = pygame.image.load('ambulancia.png')
taxi = pygame.image.load('taxi.png')
faixa = pygame.image.load('faixa.png')
grama = pygame.image.load('grama.png')
explosão = pygame.image.load('explosão.png')
fonte = pygame.font.SysFont('arial black', 30)
fonte2 = pygame.font.SysFont('arial black', 120)
game_over = fonte2.render('GAME OVER', True, (255, 0, 0), (0, 0, 0))

timer = 0
tempo_segundo = 0
a = 0
c = 0
vivo = 0                    #Quando vivo for igual a 1, é porque o jogador perdeu
texto = fonte.render('Tempo: ', True, (255, 255, 255), (0, 0, 255))
pos_texto = texto.get_rect()
pos_texto.center = (600, 30)

janela = pygame.display.set_mode((1200, 700))

pygame.display.set_caption('Jogo')
janela_aberta = True


while janela_aberta:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

        comandos = pygame.key.get_pressed()

    if comandos[pygame.K_d] and x <= 710 and vivo == 0:
        x += velocidade
    if comandos[pygame.K_a] and x >= 390 and vivo == 0:
        x -= velocidade

    if y_amb <= -169:
        y_amb = randint(1000, 1700)
    if y_pol <= -200:
        y_pol = randint(1200, 1800)
    if y_taxi <= -200:
        y_taxi = randint(1500, 2300)
    if y_amb < 1000:
        if y_taxi > 700:                                                #para que os três não apareçam juntos
            if y_pol - y_amb < 300 and y_taxi - y_amb < 200:
                y_taxi = randint(1500, 2300)

    if y_grama1 >= 794:
        y_grama1 = -94
    if y_grama2 >= 794:
        y_grama2 = -94
    if y_grama3 >= 794:
        y_grama3 = -94
    if y_grama4 >= 794:
        y_grama4 = -94
    if y_grama5 >= 794:
        y_grama5 = -94

    if a > 0:
        if x + 80 > x_taxi and y + 170 > y_taxi >= 0:             #colisão com o táxi
            vivo = 1
            vel_pista = 0
        if x - 80 < x_pol and y + 170 > y_pol >= 0:               #colisão com o carro da polícia
            vivo = 1
            vel_pista = 0
        if x > x_amb:
            if x - 70 < x_amb and y + 170 > y_amb >= 0:   #colisão com a ambulância pela esquerda ou por trás
                vivo = 1
                vel_pista = 0
        elif x < x_amb:
            if x + 80 > x_amb and y + 170 > y_amb >= 0:   #colisão com a ambulância pela esquerda
                vivo = 1
                vel_pista = 0

    if x != 550:
        a += 1
    if a > 0:
        if vivo == 0:
            timer += 1
    tempo_segundo = timer/37
    texto = fonte.render(f'Tempo: {tempo_segundo :.0f}', True, (255, 255, 255), (0, 0, 255))

    y_pol -= vel_pol
    y_amb -= vel_amb
    y_taxi -= vel_taxi
    y_grama1 += vel_pista
    y_grama2 += vel_pista
    y_grama3 += vel_pista
    y_grama4 += vel_pista
    y_grama5 += vel_pista

    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(ambulancia, (x_amb, y_amb))
    janela.blit(policia, (x_pol, y_pol))
    janela.blit(taxi, (x_taxi, y_taxi))
    janela.blit(texto, pos_texto)

    janela.blit(grama, (0, y_grama1))
    janela.blit(grama, (0, y_grama2))
    janela.blit(grama, (0, y_grama3))
    janela.blit(grama, (0, y_grama4))
    janela.blit(grama, (0, y_grama5))
    janela.blit(grama, (932, y_grama1))
    janela.blit(grama, (932, y_grama2))
    janela.blit(grama, (932, y_grama3))
    janela.blit(grama, (932, y_grama4))
    janela.blit(grama, (932, y_grama5))
    janela.blit(grama, (907, y_grama1))
    janela.blit(grama, (907, y_grama2))
    janela.blit(grama, (907, y_grama3))
    janela.blit(grama, (907, y_grama4))
    janela.blit(grama, (907, y_grama5))
    janela.blit(faixa, (511, y_grama1))
    janela.blit(faixa, (511, y_grama2))
    janela.blit(faixa, (511, y_grama3))
    janela.blit(faixa, (511, y_grama4))
    janela.blit(faixa, (511, y_grama5))
    janela.blit(faixa, (660, y_grama1))
    janela.blit(faixa, (660, y_grama2))
    janela.blit(faixa, (660, y_grama3))
    janela.blit(faixa, (660, y_grama4))
    janela.blit(faixa, (660, y_grama5))
    janela.blit(carro, (x, y))
    janela.blit(texto, pos_texto)

    if vivo == 1:                                        #Mostrar que o jogador perdeu
        pos_texto2 = texto.get_rect()
        pos_texto2.center = (280, 0)
        janela.blit(game_over, pos_texto2)
        tempo_final = fonte.render(f'Seu tempo: {tempo_segundo:.1f} segundos', True, (255, 0, 0), (0, 0, 0))
        janela.blit(tempo_final, (400, 390))
        janela.blit(explosão, (x, y))
        c += 1

    pygame.display.update()

pygame.quit()
