class bicicleta():
    def __init__(self, cor, modelo, ano, valor):
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.cor = cor
    
    def buzinar(self):
        print("Biiiiiiiiiiiiii!")

    def parar(self):
        print("Parando! ooooooooooooooh ")

    def correr(self):
        print("Correndo! Vrummmmmmmmmmmmmmm")

    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave } = {valor}'for chave, valor in self.__dict__.items()]}"
#
garethbike = bicicleta("preta", "speed","2021", 2300)

print(garethbike)