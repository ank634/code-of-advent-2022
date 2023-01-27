from typing import Final
from dataclasses import dataclass

@dataclass
class Knot:
    x_location = 0
    y_location = 0

    def move(self, direction: str) -> None:
        if direction == 'R':
            self.move_right()

        elif direction == 'U':
            self.move_up()

        elif direction == 'L':
            self.move_left()

        elif direction == 'D':
            self.move_down()

    def move_right(self) -> None:
        self.x_location += 1

    def move_left(self) -> None:
        self.x_location -= 1
        
    def move_up(self) -> None:
        self.y_location += 1

    def move_down(self) -> None:
        self.y_location -= 1

    def is_adjacent(self, other: 'Knot') -> bool:
        '''Checks to see if other Knot is adjacent with current Knot'''
        if self.x_location == other.x_location and self.y_location == other.y_location:
            return True

        elif ((self.x_location - other.x_location) == 1 or (self.x_location - other.x_location) == -1) and self.y_location == other.y_location:
            return True

        elif ((self.y_location - other.y_location) == 1 or (self.y_location - other.y_location) == -1) and self.x_location == other.x_location:
            return True

        elif ((self.x_location - other.x_location) == 1 or (self.x_location - other.x_location) == -1) and ((self.y_location - other.y_location) == 1 or (self.y_location - other.y_location) == -1):
            return True
        
        return False


def solution(command: str, visited_locations: set[tuple[int, int]], rope: list[Knot]) -> None:
    split_command: list[str] = command.split()
    direction: str = split_command[0]
    amount: int = int(split_command[1])
    
    # move head knot x amount of times
    for x in range(amount):
        rope[0].move(direction)      # move head to new direction
        for y in range(len(rope)-1): # iterate through the rest of the rope and move all the remaining knots
            if not rope[y].is_adjacent(rope[y+1]):

                if (rope[y+1].x_location == rope[y].x_location and rope[y+1].y_location != rope[y].y_location):
                    # you can't just move the previous not the same direction even if in same column or row
                    # since every knot other then the head can move diagnally.        
                    if (rope[y+1].y_location + 1) - rope[y].y_location == -1:
                        rope[y+1].move_up()
                    else:
                        rope[y+1].move_down()
        
                elif rope[y+1].x_location != rope[y].x_location and rope[y+1].y_location == rope[y].y_location:
                    # you can't just move the previous not the same direction even if in same column or row
                    # since every knot other then the head can move diagnally.
                    if (rope[y+1].x_location + 1) - rope[y].x_location == -1:
                        rope[y+1].move_right()
                    else:
                        rope[y+1].move_left()
                    
                # if knots aren't in same column or row we must move the following not diagnally in the appropriate direction
                else:
                    if rope[y+1].x_location > rope[y].x_location and rope[y+1].y_location < rope[y].y_location:
                        rope[y+1].move_up()
                        rope[y+1].move_left()

                    elif rope[y+1].x_location < rope[y].x_location and rope[y+1].y_location < rope[y].y_location:
                        rope[y+1].move_up()
                        rope[y+1].move_right()

                    elif rope[y+1].x_location < rope[y].x_location and rope[y+1].y_location > rope[y].y_location:
                        rope[y+1].move_down()
                        rope[y+1].move_right()

                    elif rope[y+1].x_location > rope[y].x_location and rope[y+1].y_location > rope[y].y_location:
                        rope[y+1].move_down()
                        rope[y+1].move_left()

        visited_locations.add((rope[-1].x_location, rope[-1].y_location))    


def main() -> None:
    FILE_NAME: Final[str] = '/Users/emmanuelbastidas/Documents/Programming Projects/Python projects/code_of_advent_2022/day09/input.txt'
    FILE_CONTENTS: Final[list[str]] = utils.get_file_contents(FILE_NAME)
    ROPE_LENGTH: Final[int] = 10
    ROPE: Final[list[Knot]] = list()
    VISITED_LOCATIONS: Final[set[tuple[int, int]]] = set()
    
    for i in range(ROPE_LENGTH):
        ROPE.append(Knot())
    
    for content in FILE_CONTENTS:
        solution(content, VISITED_LOCATIONS, ROPE)

    print(len(VISITED_LOCATIONS))


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from helpers import utils
    else:
        from helpers import utils

    main()