from MaratEngine.engine import * 
from MaratEngine.utils.node import *
from MaratEngine.utils.character import *
from MaratEngine.utils.pingpong import *


# It is standart Program
class Program(Loop):
    def __init__(self) -> None:
        super().__init__()
        
        player : Node2D = Character("Player", "")
        player.global_position = [4, 4]
        self.add_node(player)

        ping : Node2D = PingPong("ping", "@")
        ping.speed = [1, 1]
        ping.global_position = [2, 2]
        self.add_node(ping)

                
    def _process(self) -> None: 
        while True:
            super()._process()
            

      

program = Program()
program._process()