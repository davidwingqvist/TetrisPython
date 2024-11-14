import pygame

class GameEngine:
    def __init__(self) -> None:
        pygame.init()

        self.SCREEN_WIDTH = 1280
        self.SCREEN_HEIGHT = 800
        self.run = True

        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        pygame.display.set_caption("Python Game")

    def Loop(self):


        while self.run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
    
            pygame.display.update()

        pygame.quit()