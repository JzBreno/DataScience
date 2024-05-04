nome = {'Nome': 'Jose breno',
        'Idade': '24' ,
        'sexo' : 'Masculino'
}

lista = []

for i in range(10):
    lista.append(nome)

lista[1]['Nome'] = 'Breno'
lista[1]['Idade'] = '46'

print(lista[1])