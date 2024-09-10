

def finds_first_digit(line:str) -> str: # O(n), O(1)
    '''
    Traverses a given line, 
    and returns the first number
    '''
    for char in line:
        if char.isdigit():
            return char
    return ''



def finds_last_digit(line:str) -> str:
    '''
    Traverses a given line, and 
    returns the last number as a string
    '''

    # Traversing the string backwards.
    for i in range(len(line) - 1, -1, -1):
        if line[i].isdigit():
            return line[i]
    return ''



def generate_sum_for_document(document:list[str]) -> int:
    '''Returns sum of a given line, as an integer.'''
    document_sum = 0

    for line in document:
        first = finds_first_digit(line) # first as a string. 
        last = finds_last_digit(line) # last as a string.
        
        line_sum = int(first + last) # line sum as an integer.

        document_sum += line_sum
    return document_sum



def parse_txt_file(filepath:str) -> list[str]:
    '''Reads from txt file, and converts it into a list of strings.'''
    document = []

    with open(filepath, 'r', encoding='utf8') as f:
        all_lines = f.readlines()

        for line in all_lines:
            document.append(line)
    return document


if __name__ == '__main__':
    elf_document = parse_txt_file('/Users/andrewnaoyamcwilliam/Documents/technical_interviews/input_data.txt')
    total_sum = generate_sum_for_document(elf_document)

    print(total_sum)