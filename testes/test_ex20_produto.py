from ex20_produto import cadastrar_produto
def test_cadastro_mouse():
    esperado = "Produto: Mouse Gamer\nPreço: R$ 89.90\nEstoque: 15 unidades"
    assert cadastrar_produto("Mouse Gamer", 89.9, 15) == esperado

def test_cadastro_teclado():
    esperado = "Produto: Teclado\nPreço: R$ 120.00\nEstoque: 0 unidades"
    assert cadastrar_produto("Teclado", 120.0, 0) == esperado

def test_cadastro_monitor():
    esperado = "Produto: Monitor\nPreço: R$ 999.50\nEstoque: 2 unidades"
    assert cadastrar_produto("Monitor", 999.5, 2) == esperado
