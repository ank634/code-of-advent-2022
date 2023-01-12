from typing import TextIO


def solution(file_content: str, length_substring: int) -> int:
    '''Desc: Find a substring of length n in string that has no repeating values
       returns the location of last character in substring + 1
    '''
    left_index: int = 0
    right_index: int = length_substring - 1

    while right_index <= len(file_content):
        # create a set with current substring
        # contains duplicates if length of set < length_substring
        if len(set(file_content[left_index:right_index+1])) != length_substring:
            left_index+=1
            right_index+=1

        else:
            break

    
    return right_index + 1

def main() -> None:
    FILE_NAME: str = '/Users/emmanuelbastidas/Documents/Programming Projects/Python projects/code_of_advent_2022/Day06/input.txt'
    FP: TextIO = open(FILE_NAME)
    FILE_CONTENT: str = FP.readline()
    FP.close()


    substring_length: int = 4
    print(solution(FILE_CONTENT, substring_length))



if __name__ == '__main__':
    main()