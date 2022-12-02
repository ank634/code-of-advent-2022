# Desc: Remove the new line at the end of line in a txt file
# Param: The contents of one line of text from a txt file
# Return: just the raw value of line as an int
def parse_file_contents(content: str):
    if len(content) > 1:
        content = int(content.replace('\n',''))
    return content

def main():
    INPUT_FILE = 'day-01-input.txt'
    file_contents = []
    fp = None

    try:
        fp = open(INPUT_FILE)
        
        # append the parsed file contents to a list
        for x in fp:
            file_contents.append(parse_file_contents(x))

    except IOError:
        print('File could not be open')

    finally:
        if fp != None:
            fp.close()


    max = 0
    current_val = 0

    for x in file_contents:
        if x != '\n':
            current_val += x

        else:
            if current_val > max:
                max = current_val
            current_val = 0

    print(max)
main()