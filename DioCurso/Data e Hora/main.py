from datetime import date
from datetime import datetime, timedelta
from datetime import time
data = date(2024,7,30)
hora = time(20,57)
horaagr = datetime.today()
data_hora =datetime(2024,7,30,20,57)


#contando tempo 

tipo_Carro = 'P' #p,m,g
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()
print(datetime.now())
if tipo_Carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(data_estimada)
elif tipo_Carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(data_estimada)
else:
   data_estimada = data_atual + timedelta(minutes=tempo_grande)
   print(data_estimada)

