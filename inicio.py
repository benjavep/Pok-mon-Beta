import pygame
from pygame.locals import *
import sys
import reglas

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
color = (0, 0, 0)

pygame.init()
font = pygame.font.Font(None, 25)

#cargar la imagen del icono
icon_original = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/iconico.png')

def fade(screen,fondo): #esta definición la utilizamos para que haya una transicion para inciar el juego
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
    reglas.main()

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pokemon Juego")

    icon_escalada = pygame.transform.scale(icon_original, (SCREEN_WIDTH, SCREEN_HEIGHT))

    reloj = pygame.time.Clock()
    funcionar = True
    while funcionar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                funcionar = False

        teclas = pygame.key.get_pressed()
        screen.blit(icon_escalada, (0, 0))

        if teclas[pygame.K_e]:
            fade(screen,icon_escalada)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
