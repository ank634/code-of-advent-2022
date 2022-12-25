from typing import TextIO
from typing import Final


def main()->None:
    # A for Rock, B for Paper, and C for Scissors.
    
    # The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors.


    WIN_POINTS: Final[int]  = 6 
    LOSS_POINTS: Final[int] = 0
    DRAW_POINTS: Final[int] = 3
    ROCK_POINTS: Final[int] = 1
    PAPER_POINTS: Final[int] = 2
    SCISSORS_POINTS: Final[int] = 3
    FILE_NAME: Final[str] = 'input.txt'
    
    score: int = 0
    file_contents: list[str] = []

    # get all file content
    fp: TextIO = open(FILE_NAME)
    file_contents = fp.readlines()
    fp.close()

    # clean the file contents up
    file_contents = list[str](map(lambda x: x.strip('\n').replace(' ', ''), file_contents))


    # calculate score based off your input and oponents
    for content in file_contents:
        if content[1] == 'X':
            score += ROCK_POINTS

            if content[0] == 'C':
                score += WIN_POINTS

            elif content[0] == 'A':
                score += DRAW_POINTS
        
        elif content[1] == 'Y':
            score += PAPER_POINTS
            
            if content[0] == 'A':
                score += WIN_POINTS

            elif content[0] == 'B':
                score += DRAW_POINTS

        else:
            score += SCISSORS_POINTS
            if content[0] == 'B':
                score += WIN_POINTS

            elif content[0] == 'C':
                score += DRAW_POINTS

    print(score)
 

if __name__ == '__main__':
    main()