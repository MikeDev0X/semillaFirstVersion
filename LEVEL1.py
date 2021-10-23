#18/10/2021--19/10/2021--20/10/2021
#Alejandro Hidalgo Badillo A01423412
#Miguel Jiménez Padilla A01423189
#Marco Antonio Gardida Cortés A01423221
#Jorge E. Turner Escalante A01423182
#Camila Turner Escalante A01423579
#Antonio Noguerón Bárcenas A01423759

import pygame
from pygame.event import Event
from sprites import *
from pygame import *
from config import *
import sys

pygame.display.set_caption("Son of Nature")
icon = pygame.image.load('assets_test\Icon\Icon\icono.png')
pygame.display.set_icon(icon)
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WITH,WIN_HEIGHT))

        #definimos nuestra pantalla
        self.clock = pygame.time.Clock()  #permite establecer la velocidad de fotogramas de nuestro juego, es la cantidad de veces que el juego se     actualiza por segundo
        self.font = pygame.font.Font('fonts/SpaceMono-Regular.ttf', 32)
        self.running = True
        self.level=2

        self.cazadorHitbox = pygame.Rect(0, 0, PLAYER_HITBOX[0], PLAYER_HITBOX[1])

    def createTilemap(self):
              
                    BackGround(self,0,0)
                    cazador(self,0,0)
                    for i, row in enumerate(tilemap):
                        print(i, row)
                        for j, column in enumerate(row):
                            #print(j,column)
                            if column == "B":
                              Block(self,j,i)
                              
                            if column == "P":  
                              Player(self,j,i) 
                            
                            #if column == "E":
                                #cazador(self,j,i)
                                #print("si hay  enemigo")

    def new(self):

                    #self.createTilemap()

                    # Inicia un nuevo juego

                    # util para saber si el jugador a muerto o si ha decidido abandonar el juego
                    self.all_sprites = pygame.sprite.LayeredUpdates() 
                    #contiene todos los sprites del juego
                    self.blocks = pygame.sprite.LayeredUpdates() 
                    ## contiene las paredes
                    self.enemies = pygame.sprite.LayeredUpdates() 
                    # contiene todos los enemigos de nuestro juego
                    self.attacks = pygame.sprite.LayeredUpdates()  
                    self.createTilemap()
                    #self.player = Player(self, 1, 2)  
                    #la clase de nuestro jugador / 1 y 2 es la posicion de aparicion en X/Y    
                    
                    
                
    def update(self):
        self.all_sprites.update()  # llama a updates que esta en sprites


    def events(self):
      for event in pygame.event.get():
        self.playing = False
        self.running = False
        if event.type == QUIT: 
          pygame.quit()
          sys.exit()
        
            

    def draw(self):

        self.screen.fill(WHITE)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)  # actualizamos 60 veces por segundo
        pygame.display.update()

    def main(self):
        while True:
            self.events()
            self.update()
            self.draw()
        self.running = False

        pass

    def intro_screen(self):
        pass


    def levelAustralia(self):


        pass
 
    def intro(self):
      click = False
      while True:
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font("SpaceMono-Regular.ttf", 50)
        text = font.render("Main Menu", True, (255, 255, 255))
        self.screen.blit(text, (10, 10))
        button_1 = pygame.Rect(50, 100, 200, 50)
        pygame.draw.rect(self.screen, (255, 0, 0), button_1)
        play_text = font.render("Play", True, (255, 255, 255))
        self.screen.blit(play_text, (50, 85))
        mx, my = pygame.mouse.get_pos()
        if button_1.collidepoint((mx, my)):
          if click:
            break
        for event in pygame.event.get():
          if event.type == QUIT:
            pygame.quit()
            sys.exit
          elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
              click = True
        pygame.display.update()

def main():
  init()
  screen = display.set_mode((1280,720))  
  myGame = Game()
  myGame.intro_screen()
  myGame.new()
  while myGame.running:
      myGame.main()
      myGame.game_over()
      #escenaMenu()
      

if __name__ == "__main__":
  main()
    
