import pygame
from pygame.locals import *
import sys
import time
import pokemonbenja


ancho = 500
alto = 500

pygame.init()  


blanco = (255, 255, 255)

fondo_original = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/laboratorio.png')
play = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulfrente2.png')
play2 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulfrente3.png')
play3 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulfrente4.png')
play4 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulizquierda.png')
play5 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulizquierda2.png')
play6 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulderecha.png')
play7 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulderecha2.png')
play8 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azularriba.png')
play9 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azularriba2.png')
dialogo = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/dialogo.png')
oaks = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/oak.png')
pi = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/pikachu.png')
mision2 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/misiones.png')
talkk = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/talk.png')
vaporeon = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/vaporeon.png')
vaporeon2 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/vaporeon2.png')


play = pygame.transform.scale(play, (40, 46))
play2 = pygame.transform.scale(play2, (40, 46))
play3 = pygame.transform.scale(play3, (40, 46))
play4 = pygame.transform.scale(play4, (40, 46))
play5 = pygame.transform.scale(play5, (40, 46))
play6 = pygame.transform.scale(play6, (40, 46))
play7 = pygame.transform.scale(play7, (40, 46))
play8 = pygame.transform.scale(play8, (40, 46))
play9 = pygame.transform.scale(play9, (40, 46))
dialogo = pygame.transform.scale(dialogo, (ancho, 100))  
oaks = pygame.transform.scale(oaks, (300, 180))
pi = pygame.transform.scale(pi, (150, 190))
mision2 = pygame.transform.scale(mision2, (ancho / 1.5, alto / 1.5))
talkk = pygame.transform.scale(talkk, (35, 35))
vaporeon = pygame.transform.scale(vaporeon, (380, 270))
vaporeon2 = pygame.transform.scale(vaporeon2, (380, 270))


anim1 = [play2, play3]  #para abajo
anim2 = [play4, play5]  #para izquierda
anim3 = [play6, play7]  #para derecha
anim4 = [play8, play9]  #para arriba


misi = "Presiona 'M' para ver las misiones"
lol = "Hola! Soy Oak el profesor Pokémon! Oí que "
lol2 = "iniciaras tu viaje, por lo que en aquella mesa "
lol3 = "deje un amiguito que te ayudara en tu travesia."
bl = "¡Obtuviste un Pikachu nivel 5!"
talk = "Manten presionado ¨R¨ para hablar"
chau0 = "¡Ese Pikachu se nota que te quiere!"
chau = "Hay un chico allá afuera que quiere una batalla."
chau2 = "Ve y demuestrale de que estas hecho/a!"
talk2 = "Mirar las noticias (E)"
noticia = "Que noticia tan curiosa-"
noticia2 = "Bue, no pasaba nada bueno"

#clase para el profesor Oak, con su sprite y un método para mostrar su diálogo de inicio
class ProfesorOak:
    def __init__(self):
        # Cargamos la imagen del profe y la ajustamos
        self.sprite = pygame.transform.scale(pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/oak2.png'), (60, 56))
        self.sprite_hablando = oaks  #imagen cuando está hablando
        self.rect = self.sprite.get_rect()
        self.rect.center = (250, 250)  #su posición

    def dibujar(self, pantalla):
        pantalla.blit(self.sprite, self.rect)  #lo mostramos en la pantalla

    def mostrar_dialogo_inicio(self, pantalla, dialogo_img, fuente, fuente_peque, t1, t2, t3):
        #mostramos un cuadro de diálogo abajo con las frases que queremos y la imagen del profe hablando
        dialog = dialogo_img.get_rect()
        dialog.topleft = (0, alto - 100)  #lo posicionamos abajo
        pantalla.blit(dialogo_img, dialog)
        pantalla.blit(self.sprite_hablando, (100, 150))
        pantalla.blit(fuente_peque.render(t1, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))
        pantalla.blit(fuente_peque.render(t2, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 50))
        pantalla.blit(fuente_peque.render(t3, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 70))

#clase para la Pokeball, con sprite, posición y visibilidad
class Pokeball:
    def __init__(self):
        self.sprite = pygame.transform.scale(pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/pokebalf.png'), (27, 27))
        self.rect = self.sprite.get_rect()
        self.rect.center = (350, 190)
        self.visible = True  #si está visible o no

    def dibujar(self, pantalla):
        if self.visible:
            pantalla.blit(self.sprite, self.rect)  #si está visible la mostramos

    def ocultar(self):
        self.visible = False  #ocultamos la Pokeball cuando la agarrás


def main(pk):
    screen = pygame.display.set_mode((ancho, alto))  
    pygame.display.set_caption("Laboratorio ;)")  

    fondo = pygame.transform.scale(fondo_original, (ancho, alto)) 
    clock = pygame.time.Clock()  # Reloj para controlar fps
    font = pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 13) 
    font2 = pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 9)  

    oak_obj = ProfesorOak()  #creamos al profe Oak
    ball_obj = Pokeball()    #creamos la Pokeball

    pika = pi.get_rect()
    pika.center = (250, 250)  #posición de Pikachu
    talkl = talkk.get_rect()
    talkl.center = (230, 210)  #posición del icono para hablar
    misionlugar = mision2.get_rect()
    misionlugar.center = (250, 250)  #lugar para mostrar misiones
    
    playlugar = play.get_rect()
    playlugar.center = (250, 420)  #posición del jugador

    salida = pygame.Rect(220, 470, 60, 35)  #zona para salir del laboratorio
    pc = pygame.Rect(105, 55, 10, 25)       #zona del PC (computadora)

    #obstaculos (paredes, muebles, etc)
    obstaculos = [pygame.Rect(70, 151, 60, 40), 
                  pygame.Rect(310, 165, 80, 20), 
                  pygame.Rect(300, 290, 205, 30),
                  pygame.Rect(0, 290, 200, 30), 
                  pygame.Rect(450, 430, 119, 50), 
                  pygame.Rect(-30, 430, 85, 70),
                  pygame.Rect(0, 20, 500, 50), 
                  pygame.Rect(20, 0, 20, 500), 
                  pygame.Rect(460, 0, 20, 500),
                  pygame.Rect(0, 480, 500, 20), 
                  pygame.Rect(245, 230, 9, 9)]

    dialog = dialogo.get_rect()
    dialog.topleft = (0, alto - 100)  #posición del cuadro de diálogo abajo

    hablando = True  #variable para saber si estamos hablando con alguien
    fram = 0  #frame para animaciones


    while True:
        for event in pygame.event.get():  
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tecla_p = pygame.key.get_pressed()  
        play_actual = play  #sprite actual del jugador, empieza con el normal
        anterior = playlugar.copy()  #guardamos la posición anterior para controlar choques

        #movimiento con WASD y animación del sprite según la dirección
        if tecla_p[K_w]:
            play_actual = anim4[(fram // 10) % 2]  #animación para arriba
            playlugar.y -= 4
        if tecla_p[K_s]:
            play_actual = anim1[(fram // 10) % 2]  #animación para abajo
            playlugar.y += 4
        if tecla_p[K_a]:
            play_actual = anim2[(fram // 10) % 2]  #animación para izquierda
            playlugar.x -= 4
        if tecla_p[K_d]:
            play_actual = anim3[(fram // 10) % 2]  #animación para derecha
            playlugar.x += 4

        #se ve si chocamos con algo, y si si, volvemos a la posición anterior (no pasar)
        for obs in obstaculos:
            if playlugar.colliderect(obs):
                playlugar = anterior
                break

        #dibujamos todo: fondo, texto, personaje, profesor, etc
        screen.blit(fondo, (0, 0))
        screen.blit(font.render(misi, True, blanco), (10, 0))
        oak_obj.dibujar(screen)
        screen.blit(play_actual, playlugar)
        if hablando:
            screen.blit(talkk, talkl)
        ball_obj.dibujar(screen)

        #si estás cerca de Oak y estás hablando
        if playlugar.colliderect(oak_obj.rect):
            screen.blit(dialogo, dialog)
            screen.blit(font.render(talk, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))
            if tecla_p[K_r] and pk == 0:  #si presionás R y no tenés Pikachu
                hablando = False
                oak_obj.mostrar_dialogo_inicio(screen, dialogo, font, font2, lol, lol2, lol3)

        #si estás cerca de la pokeball y está visible
        if playlugar.colliderect(ball_obj.rect) and ball_obj.visible:
            screen.blit(dialogo, dialog)
            screen.blit(font.render(bl, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))
            screen.blit(pi, pika)
            pygame.display.update()
            pygame.event.pump()
            time.sleep(1.5)  #pausa para que veas la imagen
            pk += 1
            ball_obj.ocultar()
            hablando = True

        #si ya tenés el Pikachu y estás cerca de Oak
        if pk == 1 and playlugar.colliderect(oak_obj.rect):
            screen.blit(dialogo, dialog)
            screen.blit(font.render(talk, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))
            if tecla_p[K_r]:
                hablando = False
                screen.blit(oaks, (100, 150))
                screen.blit(dialogo, dialog)
                screen.blit(font2.render(chau0, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))
                screen.blit(font2.render(chau, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 50))
                screen.blit(font2.render(chau2, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 70))

        #si estás cerca de la PC
        if playlugar.colliderect(pc):
            screen.blit(dialogo, dialog)
            screen.blit(font.render(talk2, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))
            if tecla_p[K_e]:
                if pk == 0:
                    screen.blit(vaporeon, [70, 70])
                    screen.blit(dialogo, dialog)
                    screen.blit(font.render(noticia, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))
                else:
                    screen.blit(vaporeon2, [70, 70])
                    screen.blit(dialogo, dialog)
                    screen.blit(font.render(noticia2, True, (0, 0, 0)), (dialog.x + 38, dialog.y + 30))

        #si presionas M, se muestran las misiones
        if tecla_p[K_m]:
            screen.blit(mision2, misionlugar)

        #si estás en la salida, te manda afuera (siguiente parte del juego)
        if playlugar.colliderect(salida):
            pokemonbenja.main(pk, 340, 365)

        pygame.display.flip()  
        clock.tick(25)  #FPS a 25
        fram += 1  #contador de frames para las animaciones


if __name__ == "__main__":
    main(0)

