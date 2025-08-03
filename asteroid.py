from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius / 2)
            new_asteroid1.velocity = pygame.math.Vector2.rotate(self.velocity, angle)*1.2
            new_asteroid2.velocity = pygame.math.Vector2.rotate(self.velocity, -angle)*1.2