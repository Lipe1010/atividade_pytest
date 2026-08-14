from ex14_desconto import calcular_desconto
def test_desconto_dez_porcento():
    assert calcular_desconto(100, 10) == 90

def test_desconto_zero():
    assert calcular_desconto(50, 0) == 50

def test_desconto_total():
    assert calcular_desconto(200, 100) == 0
