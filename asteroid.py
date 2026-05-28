import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self,) -> None:
        new_vector_1 = self.velocity.rotate(random.uniform(20, 50))
        new_vector_2 = self.velocity.rotate(-random.uniform(20,50))
        old_radius = self.radius
        current_position = self.position
        new_radius = old_radius - ASTEROID_MIN_RADIUS

        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        Asteroid(current_position.x, current_position.y, new_radius).velocity = new_vector_1 * 1.2
        Asteroid(current_position.x, current_position.y, new_radius).velocity = new_vector_2 * 1.2
        
