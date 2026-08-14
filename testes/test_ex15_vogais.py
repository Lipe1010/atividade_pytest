from ex15_vogais import contar_vogais
def test_vogais_simples():
    assert contar_vogais("casa") == 2

def test_sem_vogais():
    assert contar_vogais("brr") == 0

def test_vogais_maiusculas():
    assert contar_vogais("AEROPORTO") == 5
