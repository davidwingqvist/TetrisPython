import pygame
from blocks.basicBlock import BasicBlock
from engine.screenHandler import ScreenHandler

class GameHandler:
    def __init__(self, screen) -> None:
        self.score = 0
        self.blocks: list[BasicBlock] = []
        self.screen = screen
        self.screenHandler = ScreenHandler()


    def AddScore(self, score):
        self.score + score
        self.UpdateScoreDisplay()

    def UpdateScoreDisplay(self):
        pygame.display.set_caption(f"***Tetris*** score: {self.score}")

    def Update(self):
        for block in self.blocks:
            block.Update()

    def Render(self):
        for block in self.blocks:
            block.Update()