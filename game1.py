import pygame
from Enemy import *
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

#create groups to hold sprrites
# - enemies for collisoions
# - all sprites for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

#center of screen for objects
center_screen = (
    scr_width/2,
    scr_height/2
)

#create screen object, size is determined by the constant scr-width
#and scr-height
screen = pygame.display.set_mode(screensize)

#create custom event for adding new enemy
addenemy = pygame.USEREVENT + 1
pygame.time.set_timer(addenemy, 550)


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
    
        #add new enemy
        elif event.type == addenemy:
            #create enemy and add to group
            new_enemy = Enemy(screensize)
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)           
    
    #get all keys pressed
    pressed_keys = pygame.key.get_pressed()
    
    #update player sprite
    player.updateKey(pressed_keys, screensize)
    
    #update position of enemy
    enemies.update()
    
    #fill the screen with white
    colorBackground = (255,255,255)
    screen.fill(colorBackground)
    
    #Draw player
    for entity in all_sprites:
        screen.blit(entity.surf,entity.rect)    
    
    
        
    pygame.display.flip()