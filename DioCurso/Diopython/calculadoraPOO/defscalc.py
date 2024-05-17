import retorno_funcao
def escrever(valor):
    with open('calculos.txt', 'a') as arquivo:
        arquivo.write(str(valor) + '\n')

def calculadora(operacao):
    def somar(a,b,*args) :
        num = args
        valor = a+b
        escrever(valor)
        return a+b
    
    def diminui(a,b,*args):
        num = args
        valor = a-b
        escrever(valor)
        return a-b
    
    def multiplica(a,b, *args):
        num = args
        valor = a * b
        escrever(valor)
        return a*b
    
    def divide(a, b, *args):
        num = args
        valor = a/b
        print('dividiu')
        escrever(valor)
        return a/b

    if operacao in retorno_funcao.soma:
        return somar
    if operacao in retorno_funcao.subtrai:
        return diminui
    if operacao in retorno_funcao.multiplicar:
        return multiplica
    if operacao in retorno_funcao.dividir:
        return divide
    

    
    
    

