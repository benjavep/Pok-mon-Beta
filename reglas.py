import pygame
from pygame.locals import *
import sys
import pokemonbenja

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
color = (0, 0, 0)
pygame.init()
pk = 0
playlugarx = 130
playlugary = 200

fondo = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/reglass.png')


def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Introducción")

    fondolu = pygame.transform.scale(fondo, (SCREEN_WIDTH, SCREEN_HEIGHT))

    reloj = pygame.time.Clock()
    funcionar = True
    while funcionar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionar = False

        tecla_p = pygame.key.get_pressed()
        screen.blit(fondolu, (0, 0))

        if tecla_p[pygame.K_e]:
            pokemonbenja.main(pk, playlugarx, playlugary)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


