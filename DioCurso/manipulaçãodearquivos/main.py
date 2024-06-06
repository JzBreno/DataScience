import csv 
from pathlib import Path
name = 'Breno'
idade = 18

with open('DioCurso\manipulaçãodearquivos\Leste.txt', 'a') as arquivo:
    arquivo.write(name + '\n')
    arquivo.write(f'{idade}{'\n'}')

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', encoding= 'utf-8') as arquivo:
        #escritor = csv.writer(arquivo)
        leitor = csv.reader(arquivo)
        #escritor.writerow(['id','nome'])
        for row in leitor:
            print(row)
except IOError as exc :
    print(f'Erro ao Criar o Arquivo. {exc}')





