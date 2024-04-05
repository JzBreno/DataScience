import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Função para calcular a distância de Manhattan entre dois pontos
def manhattan_distance(x1, x2):
    return np.sum(np.abs(x1 - x2))

# Implementação do algoritmo KNN
class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):
        self.X_train = X
        self.y_train = y

    def predict(self, X):
        predictions = [self._predict(x) for x in X]
        return np.array(predictions)

    def _predict(self, x):
        # Calcula as distâncias de Manhattan entre x e todos os exemplos no conjunto de treinamento
        distances = [manhattan_distance(x, x_train) for x_train in self.X_train]
        # Ordena as distâncias e retorna os índices dos primeiros k vizinhos
        k_indices = np.argsort(distances)[:self.k]
        # Identifica as classes dos k vizinhos
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        # Retorna a classe mais comum entre os k vizinhos
        most_common = max(set(k_nearest_labels), key=k_nearest_labels.count)
        return most_common

# Dados de entrada para a porta XOR
X = np.random.randint(0, 2, (100, 4))  # 100 amostras de 4 entradas binárias
# Rótulos de saída para a porta XOR
y = np.logical_xor(X[:, 0], X[:, 1]).astype(int)

# Divisão dos dados em conjunto de treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Inicializa o modelo KNN
knn = KNN()

# Treinamento do modelo
knn.fit(X_train, y_train)

# Teste do modelo
predictions = knn.predict(X_test)

# Calcula a acurácia do modelo
accuracy = accuracy_score(y_test, predictions)
print("Acurácia do modelo KNN:", accuracy)