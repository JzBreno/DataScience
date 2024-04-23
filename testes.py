quantidade_passos = int(input(""))

if quantidade_passos != 0:
    for i in range(quantidade_passos):
        x = i+1
        if x != 1:
            print('Explorador: {} passos'.format(x))
        else:
            print('Explorador: {} passo'.format(x))
else:
    print('Nenhum passo dado na floresta.')
