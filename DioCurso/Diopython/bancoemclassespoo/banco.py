import defs
import os
from time import sleep
 
extratosaque = []
limitesaques = 3
saldo = float()
limitediario = 500
deposito = float()
saque = float()

print("Bem vindo ao banco")



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
                defs.Saldo(saldo)
            case 2:
                saldo = defs.Depositar(saldo)
            case 3:
                defs.Extrato(extratosaque)
            case 4:
                saldo, limitesaques = defs.Saque(saldo, limitesaques)
            case 5:
                break

    else:
        print("DIGITE UM NUMERO QUE TENHA FUNCIONALIDADE")
    sleep(3)
    os.system("cls")
