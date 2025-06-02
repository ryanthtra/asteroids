import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS, PLAYER_SHOOT_SPEED

class Shot(CircleShape):

    containers = tuple()

    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SHOOT_SPEED * dt

    def does_collide(self, circ):
        #print("Testing for shot collision...")
        distance = self.position.distance_to(circ.position)
        if distance < self.radius + circ.radius:
            return True
        return False