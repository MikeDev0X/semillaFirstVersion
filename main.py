import pygame
from pygame import *
import sys, random
import sys, time
import LEVEL1
escena = 0

def multilineText(screen, tipo, texto, width, x, y, R,G,B):
    while len(texto)>0:
        linea = ""
        lin = tipo.render(linea, True, (250,250,250))
        i=0
        espacio = -1
        while lin.get_width()<width and i<len(texto):
            linea = linea + texto[i]
            if texto[i]==" ": espacio = i
            i+=1
            lin = tipo.render(linea, True, (250,250,250))
        if i==len(texto): espacio = i
        lin = tipo.render(linea[:espacio+1], True, (R,G,B))
        texto = texto[espacio+1:]
        screen.blit(lin, (x, y))
        y = y + 50 # espacio entre líneas
        
def pintar_boton(boton,fontB,textoBoton,R,G,B):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (255, 123,0), boton, 0)
    else:
        draw.rect(screen, (19, 191,62), boton, 0)
    texto = fontB.render(textoBoton, True, (R,G,B))    
    screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
                        boton.y+(boton.height-texto.get_height())/2))

def escenaMenu(screen):
    fondo = image.load('fondos/Menu.png')
    fondo = transform.scale(fondo, (720,480))
    instrucciones = image.load('fondos/instrucciones.png')
    instrucciones = transform.scale(instrucciones, (720,480))
    myFont = font.Font("Gratise.ttf", 25)
    boton = Rect(270,220,160,100)
    instruccion = False
    while True:
            for e in event.get():
                if e.type == QUIT: sys.exit()
                if e.type == MOUSEBUTTONDOWN and e.button == 1 and instruccion == False:
                    if boton.collidepoint(mouse.get_pos()):
                        fondo = instrucciones
                        instruccion = True
                        boton = Rect(100,390,110,60)
                if e.type == MOUSEBUTTONDOWN and e.button == 1 and instruccion == True:
                    if boton.collidepoint(mouse.get_pos()):
                          
                        return 1
            screen.blit(fondo, (0,0))
            pintar_boton(boton,myFont,"Jugar",255,255,255)
            display.flip()
init()
screen = display.set_mode((720,480))
mixer.init()
music = mixer.Sound("sonidos/adventure.wav")
music.set_volume(0.07)
music.play(-1)

while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    if escena == 0:
        escena = escenaMenu(screen)
    if escena == 1:
        LEVEL1.main()
        

