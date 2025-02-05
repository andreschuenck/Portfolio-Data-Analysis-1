import pandas as pd
import random
from datetime import datetime, timedelta

# Função para gerar dados sintéticos de produção
def gerar_dados_producao(num_linhas):
    dados = []
    for i in range(num_linhas):
        id_produto = f"P{i+1:04d}"
        data_producao = datetime(2024, 1, 1) + timedelta(days=random.randint(0, 30))
        tempo_producao = random.randint(30, 240)  # Tempo de produção entre 30 a 240 minutos
        tempo_setup = random.randint(10, 60)  # Tempo de setup entre 10 a 60 minutos
        quantidade_produzida = random.randint(10, 100)  # Quantidade produzida entre 10 e 100 unidades
        
        dados.append([id_produto, data_producao.strftime('%Y-%m-%d'), tempo_producao, tempo_setup, quantidade_produzida])
    
    # Criando um DataFrame com os dados
    df = pd.DataFrame(dados, columns=["ID_Produto", "Data_Producao", "Tempo_Producao", "Tempo_Setup", "Quantidade_Produzida"])

    # Salvando os dados em um arquivo CSV
    df.to_csv('data/dados_producao.csv', index=False)
    print("Dados gerados e salvos em 'data/dados_producao.csv'")

# Gerar 100 linhas de dados
gerar_dados_producao(10000)

# Explicação do Código:
# 
# Importação de Bibliotecas:
# - import pandas as pd: Importa o Pandas para manipulação de dados e criação de DataFrames.
# - import random: Para gerar valores aleatórios.
# - from datetime import datetime, timedelta: Para manipular datas de produção.
# 
# Função gerar_dados_producao():
# 
# - Gera 'num_linhas' de dados sintéticos com as colunas:
#   - ID_Produto: Gera um identificador único para o produto.
#   - Data_Producao: Gera uma data aleatória para a produção entre 1º de janeiro e 30 dias à frente.
#   - Tempo_Producao: Gera um valor aleatório entre 30 e 240 minutos.
#   - Tempo_Setup: Gera um valor aleatório entre 10 e 60 minutos.
#   - Quantidade_Produzida: Gera um valor aleatório entre 10 e 100 unidades.
# 
# Criando o DataFrame e Salvando em CSV:
# - O código usa o pandas.DataFrame para criar a tabela com os dados.
# - Em seguida, usa df.to_csv() para salvar o DataFrame como um arquivo CSV na pasta 'data/dados_producao.csv'.
# 
# Execução da Função:
# - A função gerar_dados_producao(100) gera 100 linhas de dados e salva o arquivo CSV.
