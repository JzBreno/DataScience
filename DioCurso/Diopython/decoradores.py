#inner Functions
def pai():
    print("Escrevendo da pai() Função")

    def filho1():
        print("Escrevendo da filho1() Função")
    
    def filho2():
        print("Escrevendo da filho2() Função")

    #filho1()
    #filho2()

#pai()
#saida:
"""
Escrevendo da pia() Função
Escrevendo da filho1() Função
Escrevendo da filho2() Função
"""
#retornando funções de funções


def calcular(operacao):
    def somar(a,b):
        return a + b
    
    def subtrair(a,b):
        return a- b
    
    if operacao == "+":
        return somar
    else:
        return subtrair
    
resultado = calcular("-")(1,3)
print(resultado)