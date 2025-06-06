import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 650
SCREEN_HEIGHT = 500

color=(0,0,0)
pygame.init()
font=pygame.font.Font("/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/viejito/viejito2.ttf", 15)



#imagenes
pelea=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/battle.png')
benja=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/bemja.png')
pikachu=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/espalda.png')
blastoise=pygame.image.load('/home/quinto/Escritorio/Benjamin Vega 5B 2025/prog/juegopokemon/azulin.png')

#escalar las imagenes:
benja=pygame.transform.scale(benja, (130, 180))

#textos
lucha="¡El entrenador misterioso te desafia!"
eleccion="¿Qué debe hacer Pikachu?" 
ataques="Impactrueno(1)      Ataque Rapido(2)" #nombre de los ataques que se pueden hacer
ataques2="Bola Voltio(3)     Cola de hierro(4)"
pika="Pikachu" #nombre de 1 pokemon
blasto="Blastoise" #nombre de 1 pokemon
lv= "5" #nivel de los pokemones

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) #creamos la pantalla
    pygame.display.set_caption("¡Batalla!") #nombre de la pantalla/ventana
    
    peleaa = pygame.transform.scale(pelea, (SCREEN_WIDTH, SCREEN_HEIGHT)) #fondo de la pelea
    
    hp=100 #vida de tu pokémon
    hpr=100 #vida del pokémon rival
    
    benjalugar = benja.get_rect() #lugar del rival
    benjalugar.center = (450, 100)
    
    texto1lugar = [40, 380]  #lo pongo como lista para poder modificarlo
    
    pasa = True
    while pasa:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pasa = False 
        
        tecla_p = pygame.key.get_pressed()
        
        texto1 = font.render(lucha, True, color)
        texto2=font.render(eleccion, True, color)
        

        screen.blit(peleaa, (0, 0))
        screen.blit(benja, benjalugar)
        screen.blit(texto1, texto1lugar)
        
        if tecla_p[pygame.K_e]:
            benjalugar.center = (600, 600) #cambiar la posición usando el rect
            texto1lugar = (600, 600)
        
            
        screen.blit(benja, benjalugar)
        screen.blit(texto1, texto1lugar)
        
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e: 
                texto1lugar = (600, 600) 
        
            screen.blit(texto2, [40, 380])
                
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()

    
if __name__ == "__main__":
    main()