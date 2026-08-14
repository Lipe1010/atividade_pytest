from ex16_tabuada import tabuada
def test_tabuada_do_dois():
    resultado = tabuada(2)
    assert resultado[0] == "2 x 1 = 2"
    assert resultado[9] == "2 x 10 = 20"

def test_tamanho_tabuada():
    assert len(tabuada(5)) == 10

def test_tabuada_zero():
    assert tabuada(0)[4] == "0 x 5 = 0"
