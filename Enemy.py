from random import *
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self,screensize):
        super(Enemy,self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((86,236,18))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(screensize[0]+20,screensize[0]+100),
                random.randint(0,screensize[1])
            )
        )
        self.speed = random.randint(5,20)
        
    def update_enemy(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
        