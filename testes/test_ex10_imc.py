from ex10_imc import calcular_imc

def test_imc_normal():
    assert round(calcular_imc(70, 1.75), 2) == 22.86

def test_imc_baixo():
    assert round(calcular_imc(50, 1.80), 2) == 15.43

def test_imc_alto():
    assert round(calcular_imc(100, 1.60), 2) == 39.06
