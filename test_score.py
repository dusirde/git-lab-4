import pytest
from score_to_ects import score_to_ects

def test_score_100_returns_a():
    assert score_to_ects(100) == 'A'

def test_score_90_returns_a():
    assert score_to_ects(90) == 'A'

def test_score_89_returns_b():
    assert score_to_ects(89) == 'B'

def test_score_75_returns_c():
    assert score_to_ects(75) == 'C'

def test_score_65_returns_d():
    assert score_to_ects(65) == 'D'

def test_score_60_returns_e():
    assert score_to_ects(60) == 'E'

def test_score_59_returns_f():
    assert score_to_ects(59) == 'F'

def test_score_minus_1_raises_error():
    with pytest.raises(ValueError):
        score_to_ects(-1)

def test_score_101_raises_error():
    with pytest.raises(ValueError):
        score_to_ects(101)

def test_score_string_raises_error():
    with pytest.raises(ValueError):
        score_to_ects("текст")