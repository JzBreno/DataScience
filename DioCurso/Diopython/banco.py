import os
from time import sleep
extratosaque = []
limitesaques = 3
saldo = float()
limitediario = 500
deposito = float()
saque = float()

print("Bem vindo ao banco")


def Saldo(saldo):
    print(saldo, f'Reais')


def Depositar(saldo):
    deposito = int(input("Digite o valor que irá Depositar: "))
    saldo += deposito
    return saldo


def Extrato(extratosaque):
    if len(extratosaque) == 0:
        print("Sem Saques feitos")
    else:
        print("Seu Extrato é: ")
        for i in extratosaque:
            print(i, f'Reais')


def Saque(saldo, limitesaque, extratosaques):
    print("Seu limite diario é 500 Reais")
    print(f'Seu limite de saques diarios atualmnete são', limitesaque)
    saque = int(input("Digite o valor que deseja sacar: "))
    if saque <= 500 and limitesaque > 0 and saldo > 0:
        limitesaques -= 1
        extratosaque.append(saque)
        saldo -= saque
        print("Saque Feito com Sucesso!")
    else:
        if saldo == 0:
            print('Seu saldo está Zerado!')
        if limitesaque == 0:
            print('Seu milite de saques diarios está Zerado!')
        if saque > 500:
            print('Seu limite de saque diario é apenas de 500 Reais')
        return saldo, limitesaque, extratosaques


while True:
    menu = int(input("""
[1] - Saldo
[2] - Depósitar
[3] - Extrato
[4] - Sacar
[5] - Sair
"""))

    if menu > 0 and 6 > menu:
        match menu:
            case 1:
                Saldo(saldo)
            case 2:
                saldo = Depositar(saldo)
            case 3:
                Extrato(extratosaque)
            case 4:
                saldo, limitesaques, extratosaque = Saque(
                    saldo, limitesaques, extratosaque)
            case 5:
                break

    else:
        print("DIGITE UM NUMERO QUE TENHA FUNCIONALIDADE")
    sleep(3)
    os.system("cls")
