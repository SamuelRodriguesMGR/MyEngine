
import curses
import time

class Loop:
    def __init__(self) -> None:
        self.FPS : int = 60
        self.HEIGHT : int = 10
        self.WIDTH : int = 20
        self.list_nodes : list = []
        self.tile_map : dict[list : str] = self._create_tile_map()
        self.stdscr : curses = curses.initscr()
        curses.noecho()
    
    def _create_tile_map(self) -> dict:
        new_dict : dict = {}
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                new_dict[(x, y)] = "."
        return new_dict
    
    def _create_matrix(self) -> None:
        for y in range(self.HEIGHT):
            new_line : str = ""
            for x in range(self.WIDTH):
                elem_tile_map : str = self.tile_map[(x, y)]
                

                for node in self.list_nodes:
                    if [x, y] == node.global_position:
                        if node.name == "Player":
                            new_line += f"[{elem_tile_map}]"
                        else:
                            new_line += f" {node.sprite} "
                        break   
                else:
                    new_line += f" {elem_tile_map} "                     
                
                
            self.stdscr.addstr(y, 0, new_line)

    def _update_map(self) -> None:
        time.sleep(1 / self.FPS)
        self.stdscr.refresh()

    def _process(self):
        self._create_matrix()
        self._update_map()
        for node in self.list_nodes:
            node._process()
    
    def add_node(self, node) -> None:
        node.engine = self
        self.list_nodes.append(node)