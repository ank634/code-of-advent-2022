# Desc: Remove the new line at the end of line in a txt file
# Param: The contents of one line of text from a txt file
# Return: just the raw value of line as an int
def parse_file_contents(content: str) -> str:
    if len(content) > 1:
        content = int(content.replace('\n',''))
    return content

# Desc: Parses the whole file and returns each line as an element in a list
def parse_file(FILE: str) -> list[str]:
    file_contents: list[str] = []
    fp = None

    try:
        fp = open(FILE)
        
        # append the parsed file contents to a list
        for x in fp:
            file_contents.append(parse_file_contents(x))

    except IOError:
        print('File could not be open')

    finally:
        if fp != None:
            fp.close()

    return file_contents

def main():
    INPUT_FILE = 'input.txt'
    
    # get cleaned up file content in the form of a list
    FILE_CONTENT = parse_file(INPUT_FILE)


    max = 0
    current_val = 0

    for x in FILE_CONTENT:
        if x != '\n':
            current_val += x

        else:
            if current_val > max:
                max = current_val
            current_val = 0

    print(max)

if __name__ == '__main__':
    main()