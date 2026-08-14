from ex17_fatorial import fatorial
def test_fatorial_cinco():
    assert fatorial(5) == 120

def test_fatorial_zero():
    assert fatorial(0) == 1

def test_fatorial_tres():
    assert fatorial(3) == 6
