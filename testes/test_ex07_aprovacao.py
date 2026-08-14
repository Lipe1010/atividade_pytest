from ex07_aprovacao import verificar_aprovacao

def test_aprovado():
    assert verificar_aprovacao(7.5) == "Aprovado"

def test_recuperacao():
    assert verificar_aprovacao(6.0) == "Recuperação"

def test_reprovado():
    assert verificar_aprovacao(4.9) == "Reprovado"
