import pygame
from pygame.locals import *
import sys
import time
import pokemonbenja

ancho = 500
alto = 500

pygame.init()

#colores
blanco = (255, 255, 255)

#Imágenes
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
oak=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/oak2.png')
oaks=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/oak.png')
pokeball=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/pokebalf.png')
pi=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/pikachu.png')
mision2=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/misiones.png')
talkk=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/talk.png')
vaporeon=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/vaporeon.png')
vaporeon2=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/vaporeon2.png')

#Escalar imágenes
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
oak=pygame.transform.scale(oak, (60, 56))
oaks=pygame.transform.scale(oaks, (300, 180))
pokeball=pygame.transform.scale(pokeball, (27, 27))
pi=pygame.transform.scale(pi, (150, 190))
mision2=pygame.transform.scale(mision2, (ancho/1.5, alto/1.5))
talkk=pygame.transform.scale(talkk, (35, 35))
vaporeon=pygame.transform.scale(vaporeon, (380, 270))
vaporeon2=pygame.transform.scale(vaporeon2, (380, 270))

#Animaciones
anim1 = [play2, play3]
anim2 = [play4, play5]
anim3 = [play6, play7]
anim4 = [play8, play9]

#Textos
misi= "Presiona 'M' para ver las misiones"
lol="Hola! Soy Oak el profesor Pokémon! Oí que "
lol2= "iniciaras tu viaje, por lo que en aquella mesa "
lol3="deje un amiguito que te ayudara en tu travesia."
bl="¡Obtuviste un Pikachu nivel 5!"
talk= "Manten presionado ¨R¨ para hablar"
chau0= "¡Ese Pikachu se nota que te quiere!"
chau="Hay un chico allá afuera que quiere una batalla."
chau2="Ve y demuestrale de que estas hecho/a!"
talk2="Mirar las noticias (E)"
noticia="Que noticia tan curiosa-"
noticia2="Bue, no pasaba nada bueno"

pk = 0
playlugarx=340
playlugary=365
            
misionlugar=mision2.get_rect()
misionlugar.center=(250,250)

#En este código no voy a decir que hace cada cosa porque ya lo explique en pokemonbenja.py, solo explicare lo nuevo
            
def main(pk):
    screen = pygame.display.set_mode((ancho, alto))
    pygame.display.set_caption("Laboratorio ;)")

    fondo = pygame.transform.scale(fondo_original, (ancho, alto))
    clock = pygame.time.Clock()
    font = pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 13)
    font2 = pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 9)

    fram = 0
    
    hablando=True

    #Posiciones iniciales
    playlugar = play.get_rect()
    playlugar.center = (250, 420)

    dialog = dialogo.get_rect()
    dialog.topleft = (0, alto - 100)

    oak2=oak.get_rect()
    oak2.center=(250,250)
    
    ball=pokeball.get_rect()
    ball.center=(350,190)
    
    pika=pi.get_rect()
    pika.center=(250,250)
    
    talkl=talkk.get_rect()
    talkl.center=(230,210)
    
    #Obstáculos
    obstaculos = [
        pygame.Rect(70, 151, 60, 40),   # capsula rara .
        pygame.Rect(310, 165, 80, 20),  # mesa de pokebola
        pygame.Rect(300, 290, 205, 30),# libros1
        pygame.Rect(0, 290, 200, 30),  # libros2
        pygame.Rect(450, 430, 119, 50), # planta1
        pygame.Rect(-30, 430, 85, 70),# planta2
        pygame.Rect(0, 20, 500, 50),     # pared arriba
        pygame.Rect(20, 0, 20, 500),     # pared izquierda
        pygame.Rect(460, 0, 20, 500),   # pared derecha
        pygame.Rect(0, 480, 500, 20),   #pared abajo
        pygame.Rect(245, 230, 9, 9),   #oak
        
    ]

    salida= pygame.Rect(220, 470, 60, 35) #salida
    
    pc= pygame.Rect(105, 55, 10, 25) #posición de la computadora 
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        tecla_p = pygame.key.get_pressed()
        play_actual = play
        anterior = playlugar.copy()
        
        # Movimiento con animación
        if tecla_p[pygame.K_w]:
            play_actual = anim4[(fram // 10) % 2]
            playlugar.y -= 4
        if tecla_p[pygame.K_s]:
            play_actual = anim1[(fram // 10) % 2]
            playlugar.y += 4
        if tecla_p[pygame.K_a]:
            play_actual = anim2[(fram // 10) % 2]
            playlugar.x -= 4
            
        if tecla_p[pygame.K_d]:
            play_actual = anim3[(fram // 10) % 2]
            playlugar.x += 4
        
            
        #Verificar colisiones con área reducida
        collision_rect = pygame.Rect(playlugar.x + 8, playlugar.y + 28, 14, 8)
        for obstaculo in obstaculos:
            if playlugar.colliderect(obstaculo):
                playlugar = anterior  # volver a la posición anterior
                break
            
        mision = font.render(misi, True, ( 255, 255, 255))
        # Dibujar elementos
        screen.blit(fondo, (0, 0))
        screen.blit(mision,(10,0))   
        screen.blit(oak,oak2)
        screen.blit(play_actual, playlugar)
        
        if hablando:
            screen.blit(talkk,talkl)
        
        if pk==0:
            screen.blit(pokeball,ball)
        else:
            ball.x, ball.y = 500, 500
            
        
        if playlugar.colliderect(oak2):
            screen.blit(dialogo, dialog)
            text1 = font.render(talk, True, (0, 0, 0))
            screen.blit(text1, (dialog.x + 38, dialog.y + 30))
            if tecla_p[pygame.K_r]:
                hablando=False
                texto=font2.render(lol3, True, (0, 0, 0))
                text4=(font2.render(lol, True, (0, 0, 0)))
                text5=(font2.render(lol2, True, (0, 0, 0))) 
                screen.blit(dialogo, dialog)
                screen.blit(oaks,(100,150))
                screen.blit(text4,(dialog.x + 38, dialog.y + 30))
                screen.blit(text5,(dialog.x + 38, dialog.y + 50))
                screen.blit(texto,(dialog.x + 38, dialog.y + 70))

        if playlugar.colliderect(pc):
            screen.blit(dialogo, dialog)
            text1 = font.render(talk2, True, (0, 0, 0))
            text2 = font.render(noticia, True, (0, 0, 0))
            text3 = font.render(noticia2, True, (0, 0, 0))
            screen.blit(text1, (dialog.x + 38, dialog.y + 30))
            if pk==0:
                if tecla_p[pygame.K_e]:
                    screen.blit(vaporeon,[70,70])
                    screen.blit(dialogo, dialog)
                    screen.blit(text2,(dialog.x + 38, dialog.y + 30) )
            else:
                if tecla_p[pygame.K_e]:
                    screen.blit(dialogo, dialog)
                    screen.blit(text3,(dialog.x + 38, dialog.y + 30))
                    screen.blit(vaporeon2,[70,70])
                    
        if playlugar.colliderect(ball):
            screen.blit(dialogo, dialog)
            pok = font.render(bl, True, (0, 0, 0))
            screen.blit(pok, (dialog.x + 38, dialog.y + 30))
            screen.blit(pi,pika)
            pygame.display.update() #dibuja en la pantalla
            pygame.event.pump() #procesa los eventos pendientes, obligando a pygame a actualizar lo visual
            time.sleep(1.5)
            pk=pk+1 #esta variable sirve para contar cuantos pokemones  
            hablando=True #esto sirve para mostrar o no el icono arriba de los npc
            
        if pk==1:
            if playlugar.colliderect(oak2):
                screen.blit(dialogo, dialog)
                text1 = font.render(talk, True, (0, 0, 0))
                screen.blit(text1, (dialog.x + 38, dialog.y + 30))
                if tecla_p[pygame.K_r]:
                    hablando=False
                    text=font2.render(chau2, True, (0, 0, 0))
                    textoo=(font2.render(chau0, True, (0, 0, 0)))
                    textoo0=(font2.render(chau, True, (0, 0, 0))) 
                    
                    screen.blit(oaks,(100,150))
                    screen.blit(dialogo,dialog)
                    screen.blit(dialogo, dialog)
                    screen.blit(textoo,(dialog.x + 38, dialog.y + 30))
                    screen.blit(textoo0,(dialog.x + 38, dialog.y + 50))
                    screen.blit(text,(dialog.x + 38, dialog.y + 70))
            
        if tecla_p[pygame.K_m]:
            screen.blit(mision2,misionlugar)
            
        #for obstaculo in obstaculos:
            #pygame.draw.rect(screen, (255, 0, 0), obstaculo, 2)
            
        if playlugar.colliderect(salida):
            pokemonbenja.main(pk, playlugarx,playlugary)
            
        pygame.display.flip()
        clock.tick(25)
        fram += 1
        
if __name__ == "__main__":
    main(pk)
