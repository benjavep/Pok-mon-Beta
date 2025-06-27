import pygame
from pygame.locals import *
import sys

ancho = 500
alto = 500

pygame.init()


ganar = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/ganar.png')
ganar = pygame.transform.scale(ganar, (ancho, alto)) 

def main():
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("¡GANASTE!")

    reloj = pygame.time.Clock()
    pasa = True

    while pasa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pasa = False

        
        screen.blit(ganar, (0, 0))


        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_e]:
            pasa = False  #salir del bucle

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
