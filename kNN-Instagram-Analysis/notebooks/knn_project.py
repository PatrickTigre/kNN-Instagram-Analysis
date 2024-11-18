# Importação das bibliotecas necessárias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Definindo o caminho do arquivo CSV (lembre-se de usar o caminho completo)
df = pd.read_csv(r"C:\Users\Patrick Tigre\Downloads\archive\top_insta_influencers_data.csv")

# Exibindo as primeiras linhas do dataframe para verificar a leitura correta
print("Visualizando as primeiras linhas do dataset:")
print(df.head())
print("\nInformações gerais sobre o dataset:")
print(df.info())

# Tratamento de dados ausentes (se necessário)
print("\nVerificando dados ausentes:")
print(df.isnull().sum())

# Removendo colunas desnecessárias (ajuste conforme o seu dataset)
df = df.dropna()  # Removendo linhas com valores nulos (se houver)

# Selecionando as colunas para features (X) e rótulo (y)
# Aqui estou assumindo que a coluna 'categoria' é o alvo. Altere conforme necessário.
# Ajuste as colunas de acordo com seu dataset
X = df[['followers', 'engagement_rate', 'total_posts']]  # Exemplo de features
y = df['category']  # Exemplo de rótulo (categoria)

# Dividindo o dataset em treino e teste (70% treino, 30% teste)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Criação e treino do modelo KNN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# Previsão com o modelo treinado
y_pred = knn.predict(X_test)

# Avaliação do modelo
print("\nMatriz de Confusão:")
print(confusion_matrix(y_test, y_pred))
print("\nRelatório de Classificação:")
print(classification_report(y_test, y_pred))
print("\nAcurácia do modelo:")
print(f"Acurácia: {accuracy_score(y_test, y_pred):.2f}")

# Plotando a matriz de confusão usando Seaborn para visualização
plt.figure(figsize=(8, 6))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues')
plt.title('Matriz de Confusão')
plt.xlabel('Previsto')
plt.ylabel('Verdadeiro')
plt.show()

# Visualizando a acurácia para diferentes valores de K
k_values = range(1, 21)
accuracies = []

for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred_k = knn.predict(X_test)
    accuracies.append(accuracy_score(y_test, y_pred_k))

# Plotando o gráfico da acurácia para diferentes valores de K
plt.figure(figsize=(10, 5))
plt.plot(k_values, accuracies, marker='o', linestyle='-', color='b')
plt.title('Acurácia para diferentes valores de K')
plt.xlabel('Número de Vizinhos (K)')
plt.ylabel('Acurácia')
plt.grid(True)
plt.show()
