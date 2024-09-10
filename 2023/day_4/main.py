

def count_matches(winning_numbers:list, numbers:list) -> int:
    '''Returns the number matches across winning and player numbers.'''
    count = 0

    for number in numbers:
        if number in winning_numbers:
            count +=1
    return count


def generate_card_score(count:int) -> int:
    '''Returns card score, for a given number of matches.'''
    # print(count)
    if count > 0:
        return 2**(count-1)
    return 0


def generate_score_for_pile(card_pile:list[list[list]]) -> int:
    pile_score = 0
    print(card_pile)
    for card in card_pile:
        card_match = count_matches(card[0], card[1])
        card_score = generate_card_score(card_match)
        pile_score += card_score
    return pile_score


def load_txt_file(filepath:str) -> list[str]:
    with open(filepath, 'r', encoding='utf8') as f:
        rows = f.readlines()

        return rows 


def parse_text(text:list[str]) -> list[list[list]]:
    new_list = []
    for row in text:
        numbers = row.split(': ')[-1]

        winning_numbers, actual_numbers = numbers.split(' | ')

        new_list.append([winning_numbers.split(), actual_numbers.split()])
    return new_list
    


if __name__ == '__main__':
    card_data = load_txt_file('/Users/andrewnaoyamcwilliam/Desktop/adventofcode/2023/day_5/input.txt')
    parsed_card_data = parse_text(card_data)
    print(generate_score_for_pile(parsed_card_data))

