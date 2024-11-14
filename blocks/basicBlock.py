from abc import ABC, abstractmethod

class BasicBlock(ABC):
    def __init__(self) -> None:
        self.blockType = 'o'
        self.color = (255, 255, 255)

    # Render the block on the screen.
    @abstractmethod
    def Render(self, screen):
        pass

    # Update the block.
    @abstractmethod
    def Update(self):
        pass

    # Rotate the block.
    @abstractmethod
    def Rotate(self, direction):
        pass

    