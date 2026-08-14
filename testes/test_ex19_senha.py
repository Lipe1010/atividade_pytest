from ex19_senha import validar_senha
def test_senha_valida():
    assert validar_senha("senha1234") == "Senha válida"

def test_senha_curta():
    assert validar_senha("sn12") == "Senha inválida"

def test_senha_sem_numero():
    assert validar_senha("senhasemnumero") == "Senha inválida"
