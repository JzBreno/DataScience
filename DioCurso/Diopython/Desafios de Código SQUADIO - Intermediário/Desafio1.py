saldo = float
deposito = float(input())

if deposito > 0:
    saldo = deposito
    frase = """Deposito realizado com sucesso!
Saldo atual: R$ """
    print(f'{frase}{saldo:0.2f}')
elif deposito < 0:
    print("Valor invalido! Digite um valor maior que zero.")
else:
    print("Encerrando o programa...")