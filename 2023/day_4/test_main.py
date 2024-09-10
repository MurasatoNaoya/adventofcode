import pytest

from main import count_matches, generate_card_score


def test_count_matches():
    assert count_matches([41, 48, 83, 86, 17], [83, 86, 6, 31, 17, 9, 48, 53]) == 4


def test_generate_card_score():
    assert generate_card_score(4) == 8


def test_generates_card_score_zero():
    assert generate_card_score(0) == 0



