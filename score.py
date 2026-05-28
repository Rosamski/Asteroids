import pygame


class Score(pygame.sprite.Sprite):

    def __init__(self, starting_value) -> None:
        super().__init__(self.containers)
        self.starting_value = starting_value
        self.current_value = self.starting_value
        self.font = pygame.font.Font(None, 32)

    def draw(self, screen) -> None:
        score = self.font.render(f"Score: {self.current_value}", False, "white")
        screen.blit(score, (20,20))
        

    def update(self, dt: float) -> None:
        pass

    def plus_one(self) -> None:
        self.current_value += 1
        #print(self.current_value)
