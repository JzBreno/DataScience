class cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("AUAU")

    def dormir(self):
        return print("Zzzzz...")


hercules = cachorro('hercules', 'preto', False)
print(hercules.acordado)
print(hercules.dormir())
