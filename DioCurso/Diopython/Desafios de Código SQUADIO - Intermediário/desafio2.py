##lista = ['nome','breno', 'savio', 'fagner', '1', '0']
#lista.sort()

#for nome in lista:
    #print(nome)

ativos = []
quantidadeAtivos = int(input())
codigoAtivo = ''

for _ in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

ativos.sort()

for i in ativos:
    print(i)