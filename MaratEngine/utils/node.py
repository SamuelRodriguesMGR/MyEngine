
from MaratEngine.engine import *

class Node2D:

    def __init__(self, name : str = "", sprite : str = "@") -> None:
        self.engine : Loop
        self.name : str = name
        self.global_position : list[int, int] = [0, 0]
        self.sprite : str = sprite
        self.speed = [0, 0]
    
    def _process(self) -> None:
        pass
    
    