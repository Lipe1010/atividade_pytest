from ex18_moedas import converter_dolar
def test_conversao_simples():
    assert converter_dolar(10.0, 5.0) == 2.0

def test_conversao_quebrada():
    assert round(converter_dolar(15.0, 4.8), 2) == 3.12

def test_conversao_zero():
    assert converter_dolar(0, 5.0) == 0
