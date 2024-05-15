
class Estudante:
    escola = "DIO"
    def __init__(self, nome, matricula) -> None:
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    

aluno = Estudante("guilherme", 1)
print(aluno.__str__())