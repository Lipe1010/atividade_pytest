from ex02_area import calcular_area

def test_area_quadrado():
    assert calcular_area(2, 2) == 4

def test_area_retangulo():
    assert calcular_area(5, 10) == 50

def test_area_zero():
    assert calcular_area(0, 10) == 0
