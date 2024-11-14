import pygame
import globals
from engine.gameLogic import GameHandler

class GameEngine:
    def __init__(self) -> None:
        pygame.init()

        self.run = True
        self.screen = pygame.display.set_mode((globals.SCREEN_WIDTH, globals.SCREEN_HEIGHT))
        self.gameLogic = GameHandler(self.screen)
        self.gameLogic.UpdateScoreDisplay()

    def Loop(self):

        while self.run:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

            self.gameLogic.Update()
            self.gameLogic.Render()
    
            pygame.display.update()

        pygame.quit()