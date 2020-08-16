import sys
import numpy
from operator import add, sub


def noop(num, val):
    # does nothing
    return num


class Ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self._min_steps_to_pacman = None
    
    def set_min_steps_to_pacman(self, pac_x, pac_y):
        # this is the minimal (optimal) number of steps to reach pacman, as if there were no walls
        self._min_steps_to_pacman = abs(pac_x - self.x) + abs(pac_y - self.y)
    
    @staticmethod
    def calculate_next_coord(ghost_coord: int, pac_coord: int):
        if pac_coord != ghost_coord:
            # we should try to get closer on the x axis
            if pac_coord > ghost_coord:
                operator = add
            else:
                # pac_coord < ghost_coord
                operator = sub
            ideal_next_coord = operator(ghost_coord, 1)
            return ideal_next_coord
        return None


def main(board):
    # would hash coordinates
    walls = []
    ghosts = []
    pacman: tuple = None
    for x, col in enumerate(board):
        for y, cell in enumerate(col):
            if cell == 1:
                walls.append((x, y))
            elif cell == 2:
                ghost = Ghost(x, y)
                ghosts.append(ghost)
                if pacman:
                    # spare
                    ghost.set_min_steps_to_pacman(*pacman)
            elif cell == 3:
                if pacman:
                    raise ValueError(f"More than one pacman found in board. First at {pacman}, second at {(x, y)}. Must have exactly one.")
                pacman = (x, y)
                for ghost in ghosts:
                    # all ghosts found until this moment couldn't calculate steps to pacman
                    ghost.set_min_steps_to_pacman(*pacman)
    if not pacman:
        raise ValueError(f"No pacman found in board. Board must contain exactly one")
    
    for ghost in ghosts:
        # all ghosts have already set min steps to pacman
        # decide U/R/D/L
        
        pac_x, pac_y = pacman
        ideal_next_x = ghost.calculate_next_coord(ghost.x, pac_x)
        idea_next_y = ghost.y
        
        # TODO:
        #  if next point has no walls and other ghosts, move towards it
        #  if it does, call ghost.calculate_next_coord again with y
        #  if that's impossible as well, see which of the  


if __name__ == '__main__':
    # TODO: --board 'file.npy' with OptParse
    board = [[]]
    
    main(board)
