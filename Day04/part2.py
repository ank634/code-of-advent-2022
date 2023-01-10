from typing import Final, TextIO


def get_file_contents(file_name: str) -> list[str]:
    FILE_POINTER: Final[TextIO] = open(file_name)
    FILE_CONTENTS: Final[list[str]] = FILE_POINTER.readlines()
    FILE_POINTER.close()

    # newlines at end of strings messes with data comparision so they are removed
    return list[str](map(lambda x: x.rstrip(), FILE_CONTENTS))


def parse_set(unparsed_set_representation: str) -> set[int]:
    '''recieve a string in the form '[x-y]' which repesents a set with values x through y inclusive'''
    unparsed_set_boundaries: Final[list[str]] = unparsed_set_representation.split('-')
    lower_bound: int = (int)(unparsed_set_boundaries[0])
    upper_bound: int = (int)(unparsed_set_boundaries[1])
    parsed_set: set[int] = set()

    for i in range(lower_bound, upper_bound + 1):
        parsed_set.add(i)
    
    return parsed_set


def main() -> None:
    FILE_NAME: Final[str] = 'input.txt'
    FILE_CONTENTS: Final[list[str]] = get_file_contents(FILE_NAME)

    total_intersection_sets: int = 0

    for file_content in FILE_CONTENTS:
        '''data in form of a-b,x-y which repesents a group of 2 sets
           splits it up into the two sets'''
        pre_parsed_sets: list[str] = file_content.split(',')


        left_set: set[int] = parse_set(pre_parsed_sets[0])
        right_set: set[int] = parse_set(pre_parsed_sets[1])

        intersection_set: set[int] = left_set.intersection(right_set)
        print(intersection_set)
    
        if len(intersection_set) > 0:
            total_intersection_sets += 1
            

    print(total_intersection_sets)


if __name__ == '__main__':
    main()