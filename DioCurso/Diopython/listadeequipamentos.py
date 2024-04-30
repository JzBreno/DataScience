listaequipamnetos = []

for i in range(3):
    listaequipamnetos.append(input())

mensagem = """
Lista de Equipamentos:"""
print(mensagem)
for i in listaequipamnetos:
    print(f'- ', i)
