import pytest
import random


@pytest.fixture
def rnd_gen():
    a = random.Random(123456)    
    return a
    # return random.Random(123456)

@pytest.fixture
def rnd(rnd_gen):
    # b = rnd_gen.random()
    # return b
    return rnd_gen.random()

@pytest.fixture
def make_rnd(rnd_gen):
    def maker():
        b = rnd_gen.random()
        print(b)
        return b
        # return rnd_gen.random()
    return maker


@pytest.fixture
def fixture_a(make_rnd):    
    return make_rnd

@pytest.fixture
def fixture_b(make_rnd):
    return make_rnd


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


def test_e(fixture_a, fixture_b):
    # print(fixture_a)
    # print(fixture_b)
    assert fixture_a == fixture_b