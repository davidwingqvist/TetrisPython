import math
import globals
from engine.screenSquare import ScreenSquare

class ScreenHandler:
    def __init__(self):
        self.squares: list[ScreenSquare] = []

        xBlocks = math.floor(globals.SCREEN_WIDTH / globals.BLOCKS_PER_WIDTH)
        yBlocks = math.floor(globals.SCREEN_HEIGHT / globals.BLOCKS_PER_HEIGHT)



        x = 0
        y = 0
        for i in range(globals.SCREEN_HEIGHT // yBlocks):
            x = 0
            y += yBlocks

            for i in range(globals.SCREEN_WIDTH // xBlocks):
                x += xBlocks
                square = ScreenSquare(x, y)
                self.squares.append(square)




