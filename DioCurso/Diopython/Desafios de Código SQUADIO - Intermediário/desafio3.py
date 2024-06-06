import re

def validar_senha(senha):
    # Critérios de segurança
    comprimento_minimo = 8
    contem_maiuscula = re.search(r'[A-Z]', senha)
    contem_minuscula = re.search(r'[a-z]', senha)
    contem_numero = re.search(r'[0-9]', senha)
    contem_caractere_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)
    
    # Verificações
    if len(senha) < comprimento_minimo:
        return "Sua senha e muito curta. Recomenda-se no minimo 8 caracteres."
    if not contem_maiuscula:
        return "Sua senha nao atende aos requisitos de seguranca."
    if not contem_minuscula:
        return "Sua senha nao atende aos requisitos de seguranca."
    if not contem_numero:
        return "Sua senha nao atende aos requisitos de seguranca."
    if not contem_caractere_especial:
        return "Sua senha nao atende aos requisitos de seguranca."
    
    return "Sua senha atende aos requisitos de seguranca. Parabens!"

# Exemplo de uso
senha = input()
resultado = validar_senha(senha)
print(resultado)
