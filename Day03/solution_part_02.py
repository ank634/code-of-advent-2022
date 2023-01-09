from typing import Final, TextIO


def get_file_contents(file_name: str) -> list[str]:
    FILE_POINTER: Final[TextIO] = open(file_name)
    FILE_CONTENTS: Final[list[str]] = FILE_POINTER.readlines()
    FILE_POINTER.close()

    return list[str](map(lambda x: x.rstrip(), FILE_CONTENTS))

def main() -> None:
    FILE_CONTENTS: Final[list[str]] = get_file_contents('input.txt')
    LOOK_UP_TABLE: Final[dict[str, int]] = {                                            'a' : 1,
                                            'b' : 2,
                                            'c' : 3,
                                            'd' : 4,
                                            'e' : 5,
                                            'f' : 6,
                                            'g' : 7,
                                            'h' : 8,
                                            'i' : 9,
                                            'j' : 10,
                                            'k' : 11,
                                            'l' : 12,
                                            'm' : 13,
                                            'n' : 14,
                                            'o' : 15,
                                            'p' : 16,
                                            'q' : 17,
                                            'r' : 18,
                                            's' : 19,
                                            't' : 20,
                                            'u' : 21,
                                            'v' : 22,
                                            'w' : 23,
                                            'x' : 24,
                                            'y' : 25,
                                            'z' : 26,
                                            'A' : 27,
                                            'B' : 28,
                                            'C' : 29,
                                            'D' : 30,
                                            'E' : 31,
                                            'F' : 32,
                                            'G' : 33,
                                            'H' : 34,
                                            'I' : 35,
                                            'J' : 36,
                                            'K' : 37,
                                            'L' : 38,
                                            'M' : 39,
                                            'N' : 40,
                                            'O' : 41,
                                            'P' : 42,
                                            'Q' : 43,
                                            'R' : 44,
                                            'S' : 45,
                                            'T' : 46,
                                            'U' : 47,
                                            'V' : 48,
                                            'W' : 49,
                                            'X' : 50,
                                            'Y' : 51,
                                            'Z' : 52
                                            }

    total_score: int = 0
    member_one: set[str] = set()
    member_two: set[str] = set()
    member_three: set[str] = set()

    print(FILE_CONTENTS[0])

    for i in range(0, len(FILE_CONTENTS)-2, 3):
        member_one.update(FILE_CONTENTS[i])
        member_two.update(FILE_CONTENTS[i+1])
        member_three.update(FILE_CONTENTS[i+2])
        intersection_set: set[str] = member_one.intersection(member_two, member_three)

        for k in intersection_set:
            total_score += LOOK_UP_TABLE[k]

        
        intersection_set = set()
        member_one = set()
        member_two = set()
        member_three = set()
    
    print(total_score)

if __name__ == '__main__':
    main()
