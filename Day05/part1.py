from typing import Final
import re

# O(n)
def parse_command(line_content: str) -> list[int]:
    '''Parses data from the form 'move 1 from 2 to 6'
       To a integer list in the form [1, 2, 6] and returns a copy of its values
    '''
    split_string: list[str] = re.split(r'\D+', line_content) # Isolates the integers from the commands and puts in list
    output= list[int](map(int, filter(lambda x: x.isnumeric(), split_string))) # previous instruction left trailing space for some reason this creates new list without trailing space 
    
    return output.copy()

# O(m) where n is the amount of values that are moved
def rearrange_stacks(parsed_command: list[int], stacks: list[list[str]]) -> None:
    ''' moves x amount of values from original location to destination stack
        This is also removes values moved from original location
        mutates stacks 2d list
    '''
    move_amount: int = parsed_command[0]
    move_from: int = parsed_command[1] - 1
    move_to: int = parsed_command[2] - 1

    # gets the n last elements from the move from list and appends those values to move to list in the same order
    values_moved: list[str] = stacks[move_from][-move_amount:]
    stacks[move_to].extend(values_moved)

    # delete moved values from the moved from list
    for i in range(move_amount):
       stacks[move_from].pop()
    
    
def solution(file_contents_input: list[str],  stack_orientation: list[list[str]]) -> str:
    top_stack_values: str = '' #this is the solution is the list of top of crates
    parsed_commands: list[list[int]] = [] # list holding all parsed commands in the form [move x amount, from, to]

    # parses file contents to list of list of ints in order to make it easier to implement commands
    for contents in file_contents_input:
        parsed_commands.append(parse_command(contents))


    # rearrange stack given a command
    for parsed_command in parsed_commands:
        rearrange_stacks(parsed_command, stack_orientation)

    #  get the top values of stacks
    for stacks in stack_orientation:
        top_stack_values += stacks.pop()
            
    return top_stack_values          



def main() -> None:
    FILE_NAME: str = '/Users/emmanuelbastidas/Documents/Programming Projects/Python projects/code_of_advent_2022/Day05/input.txt'
    FILE_CONTENTS: Final[list[str]] = utils.get_file_contents(FILE_NAME)

    stack_one: list[str]   = ['R' , 'S', 'L', 'F', 'Q'] 
    stack_two: list[str]   = ['N', 'Z', 'Q', 'G ', 'P', 'T']
    stack_three: list[str] = ['s', 'm', 'q' , 'b']
    stack_four: list[str]  = ['t', 'g', 'z', 'j', 'h', 'c', 'b', 'q']
    stack_five: list[str]  = ['p', 'h', 'm', 'b', 'n', 'f', 's']
    stack_six: list[str]   = ['p', 'c', 'q', 'n' , 's', 'l', 'v', 'g']
    stack_seven: list[str] = ['w', 'c', 'f']
    stack_eight: list[str] = ['q', 'h', 'g', 'z', 'w', 'v', 'p', 'm']
    stack_nine: list[str]  = ['g', 'z', 'd', 'l', 'c', 'n', 'r']

    stacks: list[list[str]] = [stack_one, stack_two, stack_three, stack_four, stack_five, stack_six, stack_seven, stack_eight, stack_nine]
    print(solution(FILE_CONTENTS, stacks))



if __name__ == '__main__':
    ''' Need to research this more but without this
        I can't import functions from my personal packages
    '''
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from helpers import utils
    else:
        from helpers import utils

    main()