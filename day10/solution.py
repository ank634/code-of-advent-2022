from typing import Final


def is_critical_cycle(cycle_count: int) -> bool:
    '''Check to see if current cycle is a significant cycle'''
    return (cycle_count - 20) % 40 == 0

def update_register_value(command: str) -> int:
    '''Parse command and return the value that X register should be incremented by'''
    if command.split()[0] == 'addx':
        return int(command.split()[1])
    return 0

def update_clock(command: str) -> int:
    '''Parse command and return the value that clock should be incremented by'''
    if command.split()[0] == 'addx':
        return 2
    return 1

def calculate_signal_strength(cycle_count: int, register_val: int) -> int:
    return cycle_count * register_val

def print_bit_map(bit_map: str) -> None:
    '''Print the bitmap that is 40 columns wide'''
    for i in range(0, len(bit_map), 40):
        print(bit_map[i: i+40])

def update_bit_map(register_val: int, crt_location: int, bit_map: str) -> str:
    '''Draw appropriate value onto bitmap'''
    if register_val == crt_location or register_val + 1 == crt_location or register_val - 1 == crt_location:
        bit_map+='#'
    else:
        bit_map+='.'

    return bit_map   


def main() -> None:
    FILE_NAME: Final[str] = '/Users/emmanuelbastidas/Documents/Programming Projects/Python projects/code_of_advent_2022/day10/input.txt'
    FILE_CONTENTS: Final[list[str]] = utils.get_file_contents(FILE_NAME)
    
    register_value: int = 1
    cycle_count: int = 1
    signal_strength: int = 0
    bit_map: str = ''
    crt_location = 0 # this can only be a value from 0-39

    for command in FILE_CONTENTS:
        clock_cyles_per_command = update_clock(command)

        for num_clock_cycles in range(clock_cyles_per_command):
            bit_map = update_bit_map(register_value, crt_location, bit_map)  

            if is_critical_cycle(cycle_count):
                signal_strength += calculate_signal_strength(cycle_count, register_value)
            # update the value of register on the last clock cycle of its command
            if clock_cyles_per_command - num_clock_cycles == 1:
                register_value += update_register_value(command)
                
            crt_location = (cycle_count % 40)
            cycle_count += 1
            
    print(signal_strength) # PART ONE SOLUTION
    print_bit_map(bit_map) # PART TWO SOLUTION


if __name__ == '__main__':
    if __package__ is None:
        import sys
        from os import path
        sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
        from helpers import utils
    else:
        from helpers import utils

    main()

 