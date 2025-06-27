import pygame
from pygame.locals import *
import sys
import random
import win
import lose

ancho = 650
alto = 500

color = (0, 0, 0)
pygame.init()
font = pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 15)

#imagenes que uso
pelea = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/battle.png')
benja = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/bemja.png')
pikachu = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/espalda.png')
blastoise = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulin.png')
ganar=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/ganar.png')
perder=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/derrotaaaaa.png')

#escalar las imágenes:
benja = pygame.transform.scale(benja, (130, 180))
blastoise = pygame.transform.scale(blastoise, (230, 260))
pikachu = pygame.transform.scale(pikachu, (200, 230))
ganar=pygame.transform.scale(ganar, (ancho, alto))
perder=pygame.transform.scale(perder, (ancho, alto))

#textos
lucha = "¡El entrenador misterioso te desafía!(E)"
eleccion = "¿Qué debe hacer Pikachu?" 
ataques = "Impactrueno(1)      Ataque Rápido(2)"  #nombre de los ataques que se pueden hacer
ataques2 = "Bola Voltio(3)     Cola de Hierro(4)"
pika = "Pikachu"  #nombre de 1 Pokémon
blasto = "Blastoise"  #nombre de 1 Pokémon
lv = "5"  #nivel de los Pokémones

#hacer una mini transición (fade) cuando cambia de pantalla
def hacer_transicion(pantalla):
    negro = pygame.Surface((ancho, alto))  # pantalla negra
    negro.fill((0, 0, 0))  # color negro
    for alpha in range(0, 255, 13):  # aumentamos la opacidad de a poco
        negro.set_alpha(alpha)
        pantalla.blit(negro, (0, 0))
        pygame.display.update()
        pygame.time.delay(30)

#mini transición blanca para los ataques
def transicion_blanca(pantalla):
    blanco = pygame.Surface((ancho, alto))  #pantalla blanca
    blanco.fill((255, 255, 255))
    for alpha in range(0, 150, 30):  #opacidad más rápida
        blanco.set_alpha(alpha)
        pantalla.blit(blanco, (0, 0))
        pygame.display.update()
        pygame.time.delay(20)

def main():
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("¡Batalla!")

    peleaa = pygame.transform.scale(pelea, (ancho, alto))

    hp = 100
    hpr = 100

    benjalugar = benja.get_rect()
    benjalugar.center = (450, 100)

    texto1lugar = [40, 380]
    textos = False
    combate_activo = True  #controla el estado de la batalla

    pasa = True
    while pasa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pasa = False

        tecla_p = pygame.key.get_pressed()

        screen.blit(peleaa, (0, 0))

        texto1 = font.render(lucha, True, color)
        texto2 = font.render(eleccion, True, color)
        texto3 = font.render(ataques, True, color)
        texto4 = font.render(ataques2, True, color)
        texto5 = font.render(lv, True, color)
        texto6 = font.render(lv, True, color)
        texto7 = font.render(f"{hpr}/100", True, color)
        texto8 = font.render(f"{hp}", True, color)
        texto9 = font.render("100", True, color)

        #dibujamos al personaje y el texto principal
        screen.blit(benja, benjalugar)
        screen.blit(texto1, texto1lugar)

        if tecla_p[pygame.K_e] and not textos: #esto es para que cuando se presiona la letra e y textos sea falso pasen cosas
            benjalugar.center = (600, 600)
            texto1lugar = (600, 600)
            textos = True
            hacer_transicion(screen)

        if textos:
            screen.blit(texto2, [40, 380])
            screen.blit(texto3, [40, 410])
            screen.blit(texto4, [40, 450])
            screen.blit(texto5, [250, 75])
            screen.blit(texto6, [580, 255])
            screen.blit(blastoise, [350, 5])
            screen.blit(pikachu, [40, 143])
            screen.blit(texto7, [50, 70])
            screen.blit(texto8, [505, 305])
            screen.blit(texto9, [565, 305])

            if combate_activo:
                ataque_realizado = False

                if tecla_p[K_1]: 
                    hpr -= random.randint(15,25)
                    ataque_realizado = True
                elif tecla_p[K_2]:
                    hpr -= random.randint(9,13)
                    ataque_realizado = True
                elif tecla_p[K_3]:
                    hpr -= random.randint(13,15)
                    ataque_realizado = True
                elif tecla_p[K_4]:
                    hpr -= random.randint(10,12)
                    ataque_realizado = True

                if ataque_realizado:
                    transicion_blanca(screen)
                    pygame.time.delay(300)
                    hpr = max(0, hpr)

                    if hpr > 0:
                        #ataque del bot
                        daño_bot = random.randint(15, 25)
                        hp -= daño_bot
                        transicion_blanca(screen)
                        pygame.time.delay(300)
                        hp = max(0, hp)

                #si alguno llega a 0, se termina el combate
                if hp <= 0 or hpr <= 0:
                    combate_activo = False
                    pygame.time.delay(500)

            else:
                if hp <= 0:
                    transicion_blanca(screen)
                    lose.main()
                elif hpr <= 0:
                    transicion_blanca(screen)
                    win.main()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
