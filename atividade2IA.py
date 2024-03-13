import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score  # r²
from sklearn.metrics import mean_squared_error  # mse

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([9, 10, 19, 21, 22, 25, 39, 40, 41, 47])

F = np.polyfit(x, y, 9)  # função que encontra o coeficiente de um polinomio

yy = np.polyval(F, x)  # saida da função como predição do modelo

plt.plot(x, y, '*', label='Real')  # plot dos dados reais
plt.plot(x, yy, 'g--', label='Predição')
plt.xlabel('x')
plt.ylabel('y')
plt.title('REGRESSÃO')
plt.show()

r2 = r2_score(y, yy)  # calculo do R²
print(r2)

mse = mean_squared_error(y, yy)  # calculo do erro quadratico médio
print(mse)
