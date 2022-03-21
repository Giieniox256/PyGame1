import pygame
from Player import Player
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_UP
)

#initializing game
pygame.init()

#define constans
scr_width = 1024
scr_height = 600
screensize = (scr_width,scr_height)

# instantiate player
player = Player()

#center of screen for objects
center_screen = (
    scr_width/2,
    scr_height/2
)

#create screen object, size is determined by the constant scr-width
#and scr-height
screen = pygame.display.set_mode(screensize)

#variable to keep running loop
running = True

#main loop
while running:
    #looking for events in queue
    for event in pygame.event.get():
        #did player push the key?
        if event.type == KEYDOWN:
            #stop the loop
            if event.key == K_ESCAPE:
                running = False
                
        #did player hit the closebutton
        elif event.type == QUIT:
            running = False
    
    #get all keys pressed
    pressed_keys = pygame.key.get_pressed()
    
    #update player sprite
    player.updateKey(pressed_keys, screensize)
        
    #fill the screen with white
    colorBackground = (255,255,255)
    screen.fill(colorBackground)
    
    #Draw player
    screen.blit(player.surf,player.rect)    
    
        
    pygame.display.flip()