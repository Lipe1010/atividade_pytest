from ex13_contagem import contagem_regressiva
def test_contagem_cinco():
    assert contagem_regressiva(5) == [5, 4, 3, 2, 1, 0]

def test_contagem_zero():
    assert contagem_regressiva(0) == [0]

def test_contagem_tres():
    assert contagem_regressiva(3) == [3, 2, 1, 0]
