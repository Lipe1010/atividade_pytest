from ex08_caracteres import contar_caracteres

def test_palavra_curta():
    assert contar_caracteres("Oi") == 2

def test_com_espacos():
    assert contar_caracteres("Olá mundo") == 9

def test_vazio():
    assert contar_caracteres("") == 0
