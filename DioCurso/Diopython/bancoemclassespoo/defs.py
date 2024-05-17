import banco
def escreve(operacao, valor, saldo):
    with open('calculos.txt', 'a') as arquivo:
        arquivo.write (f'{operacao} : {valor}'+ '\n')
        arquivo.write( f'{'Saldo'} : {saldo}'+ '\n')

def ler():
    with open('calculos.txt', 'r') as arquivo:
        for valor in arquivo:
            print(valor)

def saldo_recebe():
    with open('calculos.txt', 'r') as arquivo:
        for valor in arquivo:
            banco.saldo = valor.strip()
def Saldo(saldo):
    print(saldo, f'Reais')

def Depositar(saldo):
    operacao = 'Depositou:'
    deposito = int(input("Digite o valor que irá Depositar: "))
    saldo += deposito
    valor = deposito
    escreve(operacao, valor, saldo)
    return saldo


def Extrato(extratosaque):
        print("Seu Extrato é: ")
        ler()

def Saque(saldo, limitesaque):
    operacao = 'Saque'
    print("Seu limite diario é 500 Reais")
    print(f'Seu limite de saques diarios atualmnete são', limitesaque)
    saque = int(input("Digite o valor que deseja sacar: "))
    if saque <= 500 and limitesaque > 0 and saldo > 0:
        limitesaque -= 1
        saldo -= saque
        print("Saque Feito com Sucesso!")
        valor = saque
        escreve(operacao, valor, saldo)
    else:
        if saldo == 0:
            print('Seu saldo está Zerado!')
        if limitesaque == 0:
            print('Seu milite de saques diarios está Zerado!')
        if saque > 500:
            print('Seu limite de saque diario é apenas de 500 Reais')
    return float(saldo), int(limitesaque)
