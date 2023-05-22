import pytest
import random


@pytest.fixture
def rnd_gen():
    a = random.Random(123456)
    return a
    # return random.Random(123456)

@pytest.fixture
def rnd(rnd_gen):
    b = rnd_gen.random()
    return b
    # return rnd_gen.random()


def test_a():
    assert 1 != 2


class TestB:
    def test_b(self):
        assert 'a'.upper() == 'A'

    def test_c(self):
        with pytest.raises(ZeroDivisionError):
            1/0


def test_d(rnd):    
    assert rnd < 1