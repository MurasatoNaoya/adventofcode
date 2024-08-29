import pytest
from i_was_told_there_would_be_no_math import generate_faces_sum_and_min

@pytest.mark.parametrize('data, expected_faces_sums, expected_smallest_faces', [
    # What's being parameterised has to be in an iterable,
    #  I've used tuples here, but lists are fine too.
    (['2x2x2'], [12], [4]),
    (['1x2x3'], [11], [2]),  
    (['2x2x2', '1x2x3'], [12, 11], [4, 2]), 
])
def test_generate_faces_sum_and_min(data, expected_faces_sums, expected_smallest_faces):

    faces_sums, smallest_faces = generate_faces_sum_and_min(data)

    assert faces_sums == expected_faces_sums
    assert smallest_faces == expected_smallest_faces


@pytest.mark.parametrize('expected_faces_sums, expected_smallest_faces', [
    ([12])








]
)