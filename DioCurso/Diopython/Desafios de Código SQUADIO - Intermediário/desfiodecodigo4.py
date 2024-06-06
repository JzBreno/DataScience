class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


class PlanoUsuario:
    def __init__(self, nome, saldo):
        self.nome = nome
        self.saldo = saldo

    def VerificarSaldo(self, saldo):
        if self.saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self.saldo > 10 and self.saldo < 50:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
        else:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."


nome = input()
numero = input()
plano_nome = input()
saldo = int(input())
plano = PlanoUsuario(plano_nome, saldo)
usuario = UsuarioTelefone(nome, numero, plano)
print(plano.VerificarSaldo(saldo))
