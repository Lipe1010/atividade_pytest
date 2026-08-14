from ex09_calculadora import somar, multiplicar, dividir, subtrair

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(10, 4) == 6

def test_multiplicar():
    assert multiplicar(3, 4) == 12

def test_dividir():
    assert dividir(10, 2) == 5.0
    assert dividir(10, 0) == "Erro: divisão por zero"
