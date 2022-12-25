from typing import Final, TextIO


def main() -> None:
    WIN_POINTS: Final[int]  = 6 
    DRAW_POINTS: Final[int] = 3
    ROCK_POINTS: Final[int] = 1
    PAPER_POINTS: Final[int] = 2
    SCISSORS_POINTS: Final[int] = 3
    FILE_NAME: Final[str] = 'input.txt'
    score: int = 0

    # look up table for all the values
    possible_scenarios: Final[dict[str, int]] = {
                                                'A X': 3, 
                                                'A Y': 4, 
                                                'A Z': 8, 
                                                'B X': 1, 
                                                'B Y': 5, 
                                                'B Z': 9, 
                                                'C X': 2, 
                                                'C Y': 6, 
                                                'C Z': 7,
                                                'A X\n': 3, 
                                                'A Y\n': 4, 
                                                'A Z\n': 8, 
                                                'B X\n': 1, 
                                                'B Y\n': 5, 
                                                'B Z\n': 9, 
                                                'C X\n': 2, 
                                                'C Y\n': 6, 
                                                'C Z\n': 7
                                                }
    file_contents: list[str] = []

    # get all file content
    fp: TextIO = open(FILE_NAME)
    file_contents = fp.readlines()
    fp.close()

    # calculate final score
    for content in file_contents:
        score += possible_scenarios[content]

    print(score)



if __name__ == '__main__':
    main()