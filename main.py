import pygame
from player import Player
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            item.draw(screen)
            dt = clock.tick(60)/1000
            item.update(dt)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()

