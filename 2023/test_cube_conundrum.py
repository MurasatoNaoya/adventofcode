import pytest

from cube_conundrum import finds_max_cubes_for_game

@pytest.mark.parametrize('max_cubes,res' [
    ['(3 blue, 4 red), (1 red, 2 green, 6 blue), (2 green)', 48]
                                                                    
                                           
])

def test_finds_max_cubes_for_game(max_cubes, res):

    assert finds_max_cubes_for_game(max_cubes) == res