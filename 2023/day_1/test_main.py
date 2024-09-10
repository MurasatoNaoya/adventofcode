import pytest

from main import finds_first_digit, finds_last_digit, generate_sum_for_document


@pytest.mark.parametrize('line,res', [

    ('1asb4', '1'),
    ('2', '2'),
    ('1abd3', '1')

    ])

def test_finds_first_digit(line, res):
    assert finds_first_digit(line) == res



@pytest.mark.parametrize('line,res', [

    ('1asb4', '4'),
    ('2', '2'),
    ('1abd3', '3')

    ])

def test_finds_last_digit(line, res):
    assert finds_last_digit(line) == res




@pytest.mark.parametrize('document, res', [
    (['1abc2', 'pqr3stu8vwx',
        'a1b2c3d4e5f', 'treb7uchet'], 142)

])

def test_generate_sum_for_document(document, res):
    assert generate_sum_for_document(document) == res

