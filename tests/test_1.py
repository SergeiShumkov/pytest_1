import pytest


@pytest.yield_fixture
def open_file():
    f = None
    def opener(filename):
        nonlocal f
        assert f is None
        f = open(filename)
        return f
    yield opener
    if f is not None:
        f.close()

def test_a(open_file):
    assert open_file("file_a.txt").read() == "Content A"

def test_b(open_file):
    assert open_file("file_b.txt").read() == "Content B"

"""@pytest.yield_fixture
def opened_file():
    f = open("filename.txt")
    try:
        yield f
    finally:f.close()

def test_c(opened_file):
    assert opened_file.read() == "file content"
    """



"""@pytest.fixture(scope='function')
def rnd_gen():
    a = random.Random()    
    return a
    # return random.Random(123456)


@pytest.fixture
def fixture_a(rnd_gen):    
    print(rnd_gen)

@pytest.fixture
def fixture_b(rnd_gen):
    print(rnd_gen)

def test_a(rnd_gen):
    print(rnd_gen)

def test_b(rnd_gen):
    print(rnd_gen)"""


"""def test_e(fixture_a, fixture_b):
    # print(fixture_a)
    # print(fixture_b)
    assert fixture_a == fixture_b"""