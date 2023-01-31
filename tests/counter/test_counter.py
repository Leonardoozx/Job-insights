from src.pre_built.counter import count_ocurrences
import pytest


def test_counter():
    python_word_ocurrences = count_ocurrences("data/jobs.csv", "Python")
    js_word_ocurrences = count_ocurrences("data/jobs.csv", "Javascript")
    assert python_word_ocurrences == 1639
    assert js_word_ocurrences == 122
    with pytest.raises(TypeError):
        count_ocurrences('data/jobs.csv')
    with pytest.raises(TypeError):
        count_ocurrences('Javascript')
    with pytest.raises(TypeError):
        count_ocurrences()
