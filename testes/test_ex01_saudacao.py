from ex01_saudacao import saudacao

def test_saudacao_normal():
    assert saudacao("João") == "Olá, João! Seja bem-vindo."

def test_saudacao_maria():
    assert saudacao("Maria") == "Olá, Maria! Seja bem-vindo."

def test_saudacao_vazio():
    assert saudacao("") == "Olá, ! Seja bem-vindo."
