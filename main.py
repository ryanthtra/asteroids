# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0; # delta time

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Initialize player
    my_player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    asteroid_field = AsteroidField()

    # Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))

        updatable.update(dt)
        asteroids.update(dt)
        shots.update(dt)
        for sprite in drawable:
            sprite.draw(screen)
        for asteroid in asteroids:
            #asteroid.draw(screen)
            for shot in shots:
                if shot.does_collide(asteroid):
                    print("shot hits asteroid!")
                    pygame.sprite.Sprite.kill(asteroid)
                    pygame.sprite.Sprite.kill(shot)
            if asteroid.does_collide(my_player):
                print("Game over!")
                return 0
            

        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()