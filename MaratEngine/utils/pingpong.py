from MaratEngine.utils.node import *

class PingPong(Node2D):

    def _process(self) -> None:
        self._player_control()
        
    def _player_control(self) -> None:
        cur_pos = (self.global_position[0], self.global_position[1])

        if cur_pos[0] >= self.engine.WIDTH - 1:
            self.speed[0] = -1
        if cur_pos[1] >= self.engine.HEIGHT - 1:
            self.speed[1] = -1
        
        if cur_pos[0] <= 0:
            self.speed[0] = 1
        if cur_pos[1] <= 0:
            self.speed[1] = 1
        
        # if key == ord('p'):
        #     self.engine.tile_map[cur_pos] = "#"
        # if key == ord('o'):
        #     self.engine.tile_map[cur_pos] = "."

        self.global_position[0] += self.speed[0]
        self.global_position[1] += self.speed[1]