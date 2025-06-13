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

lolo = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/reglass.png')

def fade(screen, fondo, pk, playlugarx, playlugary): #esta definición la utilizamos para que haya una transicion para inciar el juego
    fade_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    fade_surface.fill((0, 0, 0))

    #fundido a negro
    for alpha in range(0, 255, 10):
        fade_surface.set_alpha(alpha)
        screen.blit(fondo, (0, 0))
        screen.blit(fade_surface, (0, 0))
        pygame.display.flip()
        pygame.time.delay(30)

    #cambiar a la siguiente escena
    pokemonbenja.main(pk, playlugarx, playlugary)



def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Introducción")

    lolol = pygame.transform.scale(lolo, (SCREEN_WIDTH, SCREEN_HEIGHT)) #transformamos la escala de la imagen

    reloj = pygame.time.Clock()
    lol = True
    while lol:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lol = False

        tecla_p = pygame.key.get_pressed()
        screen.blit(lolol, (0, 0))

        if tecla_p[pygame.K_e]:
            fade(screen, lolol, pk, playlugarx, playlugary)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()


