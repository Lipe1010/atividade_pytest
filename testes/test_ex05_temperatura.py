from ex05_temperatura import celsius_para_fahrenheit

def test_zero_graus():
    assert celsius_para_fahrenheit(0) == 32

def test_cem_graus():
    assert celsius_para_fahrenheit(100) == 212

def test_negativo():
    assert celsius_para_fahrenheit(-40) == -40
