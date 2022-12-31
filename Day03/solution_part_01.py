from typing import Final, TextIO


def get_file_input(file_name: str) -> list[str]:
    file_pointer: TextIO = open(file_name)
    file_contents: list[str] = file_pointer.readlines()
    file_pointer.close()

    return list[str](map(lambda x: x.rstrip('\n'), file_contents))

def main() -> None:
    FILE_NAME: Final[str] = 'input.txt'
    file_contents: list[str] = get_file_input(FILE_NAME)
    look_up_table: Final[dict[str, int]] = {
                                            'a' : 1,
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
                                            'Z' : 52,
                                            }
    
    
    left_str: str
    right_str: str
    left_str_set: set[str]
    right_str_set: set[str] 
    duplicate_str_set: set[str]
    duplicate_str: str
    score: int = 0

    for content in file_contents:
        left_str = content[:len(content) // 2]
        right_str = content[len(content) // 2: len(content)]
        left_str_set = set()
        right_str_set = set()
        
        for char in left_str:
            left_str_set.add(char)

        for char in right_str:
            right_str_set.add(char)

        duplicate_str_set = right_str_set.intersection(left_str_set)
        
        for values in duplicate_str_set:
            duplicate_str = values
            score += look_up_table[duplicate_str]
    
        
    print(score)


if __name__ == '__main__':
    main()