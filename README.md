Implementação do Algoritmo k-Nearest Neighbors (kNN) em Dados do Instagram
Descrição do Projeto
Este projeto implementa e avalia o desempenho do algoritmo k-Nearest Neighbors (kNN) em uma base de dados reais relacionada a influenciadores do Instagram. O objetivo é explorar as relações entre as variáveis ​​e criar um modelo preditivo para analisar tendências e métricas de engajamento.

Descrição da Base de Dados
A base de dados utilizada contém informações sobre influenciadores do Instagram, com as seguintes colunas principais:

rank : Posição no ranking dos influenciadores.
channel_info : Informações do canal do influenciador.
influence_score : Pontuação de influência.
postagens : Quantidade de postagens realizadas.
seguidores : Número de seguidores.
avg_likes : Média de curtidas por postagem.
60_day_eng_rate : Taxa de engajamento nos últimos 60 dias.
new_post_avg_like : Média de curtidas em novas postagens.
total_likes : Total de curtidas no canal.
país : País de origem do influenciador.
Transformação de Dados:

A coluna countryfoi convertida em valores numéricos baseados em continentes:
América do Sul: 1-9
América do Norte: 20-29
Europa: 40-49
Outras regiões, como Ásia, Oceania e África, foram comprovadas separadamente.
Instruções para replicar o projeto
Pré-requisitos

Python 3.7 ou superior.
Bibliotecas com permissão: pandas, numpy, matplotlib, seaborn, scikit-learn.
Clonar o Repositório

Clone este repositório para sua máquina local:
bater

Copiar código
git clone https://github.com/seuusuario/kNN-Instagram-Analysis.git
cd kNN-Instagram-Analysis
Instalar as Dependências

Use ou pippara instalar as bibliotecas possíveis:
bater

Copiar código
pip install -r requirements.txt
Executar o Código

O código principal não está no arquivo main.py. Executar-o:
bater

Copiar código
python main.py
Gerar o Relatório

O relatório técnico será salvo automaticamente como um arquivo PDF na pasta /docs.
Resultados
Principais Descobertas
Relação Seguidores vs Média Curtidas: Observamos uma manifestação positiva moderadamente entre o número de seguidores e a mídia de curtidas.
Impacto da Taxa de Engajamento em 60 Dias: Uma maior taxa de engajamento nos últimos 60 dias mostrou-se diretamente relacionada à classificação de influência.
Métricas de Desempenho
MSE (Erro Quadrático Médio): XX
RMSE (Raiz do Erro Quadrático Médio): XX
Melhor valor de k encontrado: X
Visualizações
Gráficos detalhados, incluindo:
Dispersão entre seguidores e avg_likes .
Comparação de classificação e influencia_score .
Estrutura do Repositório
texto simples

Copiar código
├── data/                # Base de dados
├── docs/                # Relatórios técnicos
├── src/                 # Código-fonte
├── README.md            # Este arquivo
├── requirements.txt     # Dependências do projeto
├── main.py              # Arquivo principal
