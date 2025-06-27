import pygame
from pygame.locals import *
import sys
import batalla

ancho = 500
alto = 500

pygame.init()

perder = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/derrotaaaaa.png')
perder = pygame.transform.scale(perder, (ancho, alto))  # Escalar al tamaño de la ventana

def main():
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Pantalla de Victoria")

    reloj = pygame.time.Clock()
    pasa = True

    while pasa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pasa = False

        screen.blit(perder, (0, 0))

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_e]:
            pasa = False  

        if teclas[pygame.K_q]: #reintentar
            batalla.main()
            
        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
