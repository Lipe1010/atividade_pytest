from ex06_media import calcular_media

def test_media_exata():
    assert calcular_media(7, 7, 7) == 7

def test_media_quebrada():
    assert round(calcular_media(5, 6, 8), 2) == 6.33

def test_media_zero():
    assert calcular_media(0, 0, 0) == 0
