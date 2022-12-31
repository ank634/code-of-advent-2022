import solution_part_1

def main() -> None:
    INPUT_FILE = 'input.txt'
    FILE_CONTENT = solution_part_1.parse_file(INPUT_FILE)

    all_calories = [] # list of all categories, each element is calories one elf has
    current_val = 0   

    for x in FILE_CONTENT:
        if x != '\n':
            current_val += x

        else:
            all_calories.append(current_val)
            current_val = 0

    sorted_calories = sorted(all_calories)
    
    print(sum(sorted_calories[-3:])) # print the sum of the last three values of the sorted list

if __name__ == '__main__':
    main()