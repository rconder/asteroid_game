import pygame
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        for item in drawable:
            item.draw(screen)
        for item in updatable:
            dt = clock.tick(60)/1000
            item.update(dt)
        for item in asteroids:
            if not player.is_collide(item):
                print("Game Over") 
                raise SystemExit("You Lose")
            for shot in shots:
                if not shot.is_collide(item):
                    item.kill()
        pygame.display.flip()

if __name__ == "__main__":
    main()

