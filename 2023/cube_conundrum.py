# 12R, 13G, 14B
import re


def extract_id_game(line:str) -> tuple:
    '''Reads from a game line and returns game ID and rounds.'''

    # RegEx pattern for isolating game ID and rounds into two groups.
    regex_pattern = r'Game (\d+): (.*)'

    # .search is used here to find the first valid match.
    match = re.search(regex_pattern, line)


    # Returning game ID and the rounds as a tuple.
    return (match.group(1), match.group(2))


def parse_game(rounds:str) -> list[list[tuple[int, str]]]:
    '''Returns a formatted game list for a given rounds string.'''
    game = []

    # Generalised for groups of a digit(s) a space then character(s). 
    regex_pattern = r'(\d+) (\w+)'
    
    # Separating the rounds string, to find individual rounds.
    rounds = rounds.split(';')

    for round in rounds:
        # Unlike .search(), .findall() returns a list 
        # containing ALL matching groups.
        match  = re.findall(regex_pattern, round)
        game.append(match)
    return game




    
def check_valid_round(turn:list[tuple[int, str]], actual: list[tuple[int, str]]) -> bool:
    '''Returns bool for whether a given round is valid, given starting list of cubes.'''

    ... 


def check_valid_game(game:list[list[tuple[int, str]]], actual: list[tuple[int, str]]) -> bool:
    '''Returns bool for whether a given game is valid, given starting list of cubes.'''

    ... 


def count_valid_games(games:list[list[list[tuple[int, str]]]]) -> int:
    '''Returns number of valid games, for a given games array.'''

    ... 


if __name__ == '__main__':
    id, rounds = extract_id_game("Game 1: 7 blue, 6 green, 3 red; 3 red, 5 green, 1 blue; 1 red, 5 green, 8 blue; 3 red, 1 green, 5 blue")
    print(parse_game(rounds))