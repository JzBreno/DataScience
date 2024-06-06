# Classe PlanoTelefone
class PlanoTelefone:
    def __init__(self, nome, saldo):
        self.__nome = nome
        self.__saldo = saldo

    # Método para verificar o saldo
    def verificar_saldo(self):
        return self.__saldo

    # Método para gerar mensagem personalizada
    def mensagem_personalizada(self):
        saldo = self.__saldo
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

    def custo_chamada(self, duracao):
        valor = 0.10
        return (valor * duracao)

    def deduzir_saldo(self, gasto,saldo, numero_telefone_destinatario ):
        sald = saldo
        if gasto > sald:
            return 'Saldo insuficiente para fazer a chamada.'
        else:
            return f'Chamada para {numero_telefone_destinatario} realizada com sucesso. Saldo: ${"%.2f" % (sald-gasto) }'

# Classe UsuarioTelefone


class UsuarioTelefone:
    def __init__(self, nome, plano):
        self.nome = nome
        self.plano = plano
        self.destinatario = destinatario
        self.duracao = duracao

    # Método para verificar o saldo do usuário e gerar uma mensagem personalizada
    def verificar_saldo(self):
        saldo = self.plano.verificar_saldo()
        mensagem = self.plano.mensagem_personalizada()
        return saldo, mensagem


class Chamada_telefone:
    def __init__(self, plano, nome_usuario, numero_telefone, saldo_inicial, numero_destinatario, duracao) -> None:
        self.plano = plano
        self.nome_usuario = nome_usuario
        self.numero_telefone = numero_telefone
        self.saldo_inicial = saldo_inicial
        self.numero_destinatario = numero_destinatario
        self.duracao = duracao

    def fazer_chamada(self):
        nome_usuario = self.nome_usuario
        numero_telefone_usuario = self.numero_telefone
        saldo = self.saldo_inicial
        numero_telefone_destinatario = self.numero_destinatario
        dur = self.duracao

        gasto = self.plano.custo_chamada(dur)
        dedu_saldo = self.plano.deduzir_saldo(gasto, saldo, numero_telefone_destinatario)
        return gasto, dedu_saldo


# Recebendo as entradas do usuário (nome, plano, saldo)
nome_usuario = 'Breno'
nome_plano = 'premium'

nome = input()
numero1 = input()
saldo_inicial = float(input())
numero2 = input()
tempo = int(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial)
usuario = Chamada_telefone(plano_usuario, nome,
                           numero1, saldo_inicial, numero2, tempo)

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do pla
gasto_chamada, deducao_saldo = usuario.fazer_chamada()
print(deducao_saldo)
