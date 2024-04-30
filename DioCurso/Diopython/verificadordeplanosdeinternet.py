consumo = float(input("Digite seu consumo em GB: "))


def verificador_de_consumo(consumo):
    if consumo <= 10:
        print("Plano Essencial Fibra - 50Mbps")
    if consumo > 10 and consumo <= 20:
        print("Plano Prata Fibra - 100Mbps")
    elif consumo > 20:
        print("Plano Premium Fibra - 300Mbps")


verificador_de_consumo(consumo)
