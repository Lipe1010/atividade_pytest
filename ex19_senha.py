def validar_senha(senha):
    if len(senha) < 8:
        return "Senha inválida"
    
    tem_letra = False
    tem_numero = False
    
    for char in senha:
        if char.isalpha():
            tem_letra = True
        if char.isdigit():
            tem_numero = True
            
    if tem_letra and tem_numero:
        return "Senha válida"
    else:
        return "Senha inválida"
