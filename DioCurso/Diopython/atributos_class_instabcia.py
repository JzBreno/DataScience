class PlanoTelefone:
    def __init__(self, nome, saldo):
        self._nome = nome
        self._saldo = saldo

    @property
    def nome(self):
        return self._nome

    @property
    def saldo(self):
        return self._saldo

    def verificar_saldo(self):
        if self._saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif self._saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    def mensagem_personalizada(self, nome_usuario):
        return f"Olá {nome_usuario}, seu saldo atual é {self._saldo}. {self.verificar_saldo()}"


class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self.nome = nome
        self.numero = numero
        self.plano = plano

    def __str__(self):
        return f"Usuário {self.nome} com número {self.numero} criado com sucesso."

    def verificar_saldo_plano(self):
        return self.plano.mensagem_personalizada(self.nome)


# Coletando informações do usuário
nome = input()
numero = input()
plano_nome = input()
saldo = int(input())

# Criando instâncias das classes
plano = PlanoTelefone(plano_nome, saldo)
usuario = UsuarioTelefone(nome, numero, plano)

# Exibindo informações
print(usuario)
print(usuario.verificar_saldo_plano())
