import pygame
from pygame.locals import *
import sys
import labo
import batalla

ancho = 500 
alto = 500

pygame.init()

#colores
blanco = (255, 255, 255)

#imágenes
fondo_original = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/pueblopaleta.png')
play = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulfrente2.png')
blastoise = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/blastoisef.png')
ben = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/benjaf.png')
play2 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulfrente3.png')
play3 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulfrente4.png')
play4 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulizquierda.png')
play5 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulizquierda2.png')
play6 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulderecha.png')
play7 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulderecha2.png')
play8 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azularriba.png')
play9 = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azularriba2.png')
dialogo = pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/dialogo.png')
puerta= pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/puerta.png')
icon=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/iconico.png')
mision2=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/misiones.png')

#escalar imágenes
play = pygame.transform.scale(play, (30, 36))
play2 = pygame.transform.scale(play2, (30, 36))
play3 = pygame.transform.scale(play3, (30, 36))
play4 = pygame.transform.scale(play4, (30, 36))
play5 = pygame.transform.scale(play5, (30, 36))
play6 = pygame.transform.scale(play6, (30, 36))
play7 = pygame.transform.scale(play7, (30, 36))
play8 = pygame.transform.scale(play8, (30, 36))
play9 = pygame.transform.scale(play9, (30, 36))
blastoise = pygame.transform.scale(blastoise, (50, 50))
ben = pygame.transform.scale(ben, (45, 45))
dialogo = pygame.transform.scale(dialogo, (ancho, 100))
puerta=pygame.transform.scale(puerta, (45, 45))
mision2=pygame.transform.scale(mision2, (ancho/1.5, alto/1.5))

#animaciones
anim1 = [play2, play3]
anim2 = [play4, play5]
anim3 = [play6, play7]
anim4 = [play8, play9]

#textos
hablar = "Manten presionado ¨R¨ para hablar"
hablar2 = "¿En serio quieres una batalla? NO TIENES POKÉMONES"
misi= "Presiona 'M' para ver las misiones"


#icono
pygame.display.set_icon(icon)

pk = 0 #esta variable sirve para saber si ya tienes 1 pokemon
playlugarx=130 #esta variable es la posición x inicial del jugador
playlugary=200 #esta variable es la posición y inicial del jugador

misionlugar=mision2.get_rect()
misionlugar.center=(250,250)
        
def main(pk, playlugarx,playlugary):
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Pokemon Juego")

    fondo = pygame.transform.scale(fondo_original, (ancho, alto))
    clock = pygame.time.Clock()
    font = pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 13)
    font2 = pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 8)

    fram = 0
    

    #posiciones iniciales
    playlugar = play.get_rect()
    playlugar.center = (playlugarx, playlugary)

    blastoiselu = blastoise.get_rect()
    blastoiselu.center = (100, 450)

    benfinal = ben.get_rect()
    benfinal.center = (70, 450)

    dialog = dialogo.get_rect()
    dialog.topleft = (0, alto - 100)
    


    #obstáculos/colisiones
    obstaculos = [
        pygame.Rect(100, 90, 110, 80),   #casa jugador
        pygame.Rect(285, 90, 110, 80),  #casa rival
        pygame.Rect(270, 240, 145, 80),#laboratorio
        pygame.Rect(100, 275, 110, 5),  #valla1
        pygame.Rect(270, 400, 119, 5), #valla2
        pygame.Rect(145, 430, 85, 70),#agua
        pygame.Rect(85, 170, 20, 20),   #correo
        pygame.Rect(110, 350, 10, 10),  #cartel 
        pygame.Rect(0, 20, 500, 20),     #arboles arriba
        pygame.Rect(20, 0, 20, 500),     #arboles izquierda
        pygame.Rect(460, 0, 20, 500),   #arboles derecha
        pygame.Rect(0, 480, 500, 20), #arboles abajo
    ]

    entrar=pygame.Rect(340, 280, 15, 50) #puerta del lab
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tecla_p = pygame.key.get_pressed()
        play_actual = play
        anterior = playlugar.copy() #esto lo usaremos para que el jugador no traspase las colisiones
        
        #movimiento con animación
        if tecla_p[pygame.K_w]:
            play_actual = anim4[(fram // 10) % 2]
            playlugar.y -= 3
        if tecla_p[pygame.K_s]:
            play_actual = anim1[(fram // 10) % 2]
            playlugar.y += 3
        if tecla_p[pygame.K_a]:
            play_actual = anim2[(fram // 10) % 2]
            playlugar.x -= 3
        if tecla_p[pygame.K_d]:
            play_actual = anim3[(fram // 10) % 2]
            playlugar.x += 3
            
        #colisiones:
        collision_rect = pygame.Rect(playlugar.x + 8, playlugar.y + 28, 14, 8)
        for obstaculo in obstaculos:
            if playlugar.colliderect(obstaculo):
                playlugar = anterior  #volver a la posición anterior
                break
            
        mision = font.render(misi, True, ( 0, 50, 0 ))
        
        #dibujar elementos
        
        screen.blit(fondo, (0, 0))
        screen.blit(blastoise, blastoiselu)
        screen.blit(ben, benfinal)
        screen.blit(play_actual, playlugar)
        screen.blit(mision,(10,10))
        
        #hablar con npcs
        if playlugar.colliderect(benfinal):
            screen.blit(dialogo, dialog)
            text1 = font.render(hablar, True, (0, 0, 0))
            screen.blit(text1, (dialog.x + 38, dialog.y + 30))
            if tecla_p[pygame.K_r]:
                if pk == 0:
                    text2 = font2.render(hablar2, True, (0, 0, 0))
                    screen.blit(dialogo, dialog)
                    screen.blit(text2, (dialog.x + 38, dialog.y + 30))
                else: 
                    batalla.main()
       
        if tecla_p[pygame.K_m]: #ver misiones
            screen.blit(mision2,misionlugar)

        
        if playlugar.colliderect(entrar): #entrar al laboratorio
            labo.main(pk) #para que se mantenga el valor de pk a la hora de entrar al laboratorio
            
            
        pygame.display.flip()
        clock.tick(25)
        fram += 1

if __name__ == "__main__":
    main(pk, playlugarx,playlugary) 
