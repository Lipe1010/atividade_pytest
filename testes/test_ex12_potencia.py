from ex12_potencia import potencia
def test_potencia_quadrado():
    assert potencia(2, 2) == 4

def test_potencia_cubo():
    assert potencia(3, 3) == 27

def test_potencia_zero():
    assert potencia(5, 0) == 1
