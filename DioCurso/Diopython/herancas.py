class veiculo:
    def __init__(self, cor, placa, num_rodas ):
        self.cor = cor
        self.placa = placa
        self.num_rodas = num_rodas
    
    def ligar(self):
        print("ok!gonna staring...")
        print("3,2,1...")
        print("vrumm")

    def desligar(self):
        print("ok!gonna stop...")
        print("3,2,1...")
        print("puff")

    def acelerar(self):
        print("ok!gonna run more...")
        print("vrummVRUUUUUUUUUUUUUUUUUUUUUUUUUUUUUM")
    
    def freiar(self):
        msg = """
            68,
            67,
            66,
            40...
            """
        print("ok! more slow ....")
        print(msg)

c = veiculo('preto', '234-9876', 4)
c.ligar()
c.acelerar()
c.freiar()
c.desligar()