'''Advent of code, 2023 Day 3.'''
# 12R, 13G, 14B
import re


def extract_id_game(line:str) -> tuple:
    '''Reads from a game line and returning game id and turns.'''

    # RegEx pattern for isolating game id and turns into two groups.
    regex_pattern = r'Game (\d+): (.*)'

    # .search is used here to find the first game id match.
    match = re.search(regex_pattern, line)


    # Returning game id and the turns as a tuple.
    return (match.group(1), match.group(2))


def parse_game(turns:str) -> list[list[tuple[int, str]]]:
    '''Returns a formatted game list for a given turns string.'''
    game = []

    # Generalised for groups of a digit(s) a space then character(s).
    regex_pattern = r'(\d+) (\w+)'

    # Separating the turns string, to find individual turns.
    turns = turns.split(';')

    for turn in turns:
        # Unlike .search(), .findall() returns a list
        # containing ALL matching groups.
        match  = re.findall(regex_pattern, turn)
        game.append(match)
    return game





def check_valid_turn(turn:list[tuple[int, str]], actual: dict) -> bool:
    '''Returns bool for whether a given turn is valid, given starting list of cubes.'''

    for draw in turn:
        # print(draw)
        count, colour = draw
        # Count must be converted to an int,
        # as it if from a .txt file, which only
        # contains strings.
        if actual[colour] < int(count):
            return False
    return True



def check_valid_game(game:list[list[tuple[int, str]]], actual: dict) -> bool:
    '''Returns bool for whether a given game is valid, given starting list of cubes.'''

    for turn in game:
        if not check_valid_turn(turn, actual):
            return False
    return True


def count_id_id_sum(actual: dict):
    '''Reads from the input text file, and accumulates the id_sum of all game IDs.'''
    id_sum = 0
    with open('/Users/andrewnaoyamcwilliam/Desktop/adventofcode/2023/day_2/input.txt',
               'r', encoding='utf8') as f:
        for line in f:
            game_id, turns = extract_id_game(line)
            game = parse_game(turns)
            if check_valid_game(game, actual):
                id_sum += int(game_id)
    return id_sum



if __name__ == '__main__':

    actual_draw = {
        'red' : 12,
        'green' : 13,
        'blue' : 14

    }

    print(f'The sum of the IDs for all valid games is : {count_id_id_sum(actual_draw)}')
