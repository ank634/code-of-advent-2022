from typing import Final
import functools


class File:
    def __init__(self, name: str, size: int = 0) -> None:
        self.name: str = name
        self.size: int = size

    
    def __str__(self) -> str:
        return f'[name: {self.name}, size: {self.size}]'

    def __repr__(self) -> str:
        return f'File({self.name}, {self.size})'

    def __eq__(self, other: object) -> bool:
        if isinstance(other, File):
            return self.name == other.name
        return NotImplemented


def parse_file(split_command: list[str]) -> File:
    return File(split_command[1], int(split_command[0]))


def main() -> None:
    FILE_NAME: str = '/Users/emmanuelbastidas/Documents/Programming Projects/Python projects/code_of_advent_2022/Day07/input.txt'
    FILE_CONTENT: Final[list[str]] = utils.get_file_contents(FILE_NAME)
    LAST_FILES: list[File] = [] # holds only file directories 
    ALL_DIRECTORIES: list[File] =[]


    # builds file directory
    for content in FILE_CONTENT:
        
        split_command_line: list[str] = content.split()

        # parse the new file we have stepped into and save it on the file stack
        if split_command_line[1] == 'cd' and split_command_line[2] != '..':
            current_directory: File = File(split_command_line[2])
            LAST_FILES.append(current_directory)
            ALL_DIRECTORIES.append(current_directory)

        # if we go up in directory remove that directory from file stack
        elif split_command_line[1] == 'cd' and split_command_line[2] == '..':
            LAST_FILES.pop()
            
        # if the value command read is one showing a file NOT A DIRECTORY
        # propage value up directory tree
        elif split_command_line[0] != '$' and split_command_line[0] != 'dir':
            child: File = parse_file(split_command_line)
            for i in LAST_FILES:
                i.size += child.size


    # find the sum of all directories with a value less then 100000
    ValidFiles: list[File] = list(filter(lambda x: x.size < 100000, ALL_DIRECTORIES))

    total: int = 0
    for x in ValidFiles:
        total += x.size
    
    print(total)

    #Part2###############################
    TOTAL_SPACE: int = 70000000
    USED_SPACE: int = ALL_DIRECTORIES[0].size
    REQUIRED_SPACE: int = 30000000
    available_space: int = TOTAL_SPACE - USED_SPACE

    possible_values: list[int] = [] # list of directories that could be deleted

    for dir in ALL_DIRECTORIES:
        if dir.size >= (REQUIRED_SPACE - available_space):
            possible_values.append(dir.size)


    # find the smallest directory that could be deleted to fulfill requirement
    print(min(possible_values))
    
    
        



    



if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from helpers import utils
    else:
        from helpers import utils

    main()
