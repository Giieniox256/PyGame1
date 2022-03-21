import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)

class Player(pygame.sprite.Sprite):
    def __init__(self):
       super(Player,self).__init__()
       self.surf = pygame.Surface((75,25))
       self.surf.fill((69,46,183))
       self.rect = self.surf.get_rect()
    
    def updateKey(self, presKey, screensize):
        if presKey[K_UP]:
            self.rect.move_ip(0,-5)
        if presKey[K_DOWN]:
            self.rect.move_ip(0,5)
        if presKey[K_LEFT]:
            self.rect.move_ip(-5,0)
        if presKey[K_RIGHT]:
            self.rect.move_ip(5,0)
        #keep player in screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > screensize[0]:
            self.rect.right = screensize[0]
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= screensize[1]:
            self.rect.bottom = screensize[1]