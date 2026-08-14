from ex03_par_impar import eh_par

def test_eh_par_verdadeiro():
    assert eh_par(4) is True

def test_eh_par_falso():
    assert eh_par(5) is False

def test_eh_par_zero():
    assert eh_par(0) is True
