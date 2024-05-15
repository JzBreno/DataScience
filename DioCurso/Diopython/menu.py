import DioCurso.Diopython.bancoemclassespoo.banco as banco
import DioCurso.Diopython.bancoemclassespoo.defs as defs
from time import sleep
import os

if banco.menu > 0 and 6 > banco.menu:
        match banco.menu:
            case 1:
                defs.Saldo(banco.saldo)
            case 2:
                saldo = defs.Depositar(banco.saldo)
            case 3:
                defs.Extrato(banco.extratosaque)
            case 4:
                saldo, limitesaques, extratosaque = defs.Saque(
                    banco.saldo, banco.limitesaques, banco.extratosaque)
            case 5:
                  continue

else:
    print("DIGITE UM NUMERO QUE TENHA FUNCIONALIDADE")
    time.sleep(3)
    os.system("cls")