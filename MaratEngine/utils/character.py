from MaratEngine.utils.node import *

class Character(Node2D):

    def _process(self) -> None:
        self._control()
        
    def _control(self) -> None:
        key = self.engine.stdscr.getch()  # Ждем нажатия клавиши
        cur_pos = (self.global_position[0], self.global_position[1])
        self.speed = [0, 0]

        if key == ord('a'):
            self.speed[0] += -1
        if key == ord('w'):
            self.speed[1] += -1
        
        if key == ord('d'):
            self.speed[0] += 1
        if key == ord('s'):
            self.speed[1] += 1
        
        if key == ord('p'):
            self.engine.tile_map[cur_pos] = "#"
        if key == ord('o'):
            self.engine.tile_map[cur_pos] = "."

        self.global_position[0] += self.speed[0]
        self.global_position[1] += self.speed[1]

        
