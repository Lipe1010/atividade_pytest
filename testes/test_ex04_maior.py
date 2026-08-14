from ex04_maior import maior_numero

def test_maior_a():
    assert maior_numero(10, 5) == 10

def test_maior_b():
    assert maior_numero(2, 8) == 8

def test_maior_iguais():
    assert maior_numero(3, 3) == 3
