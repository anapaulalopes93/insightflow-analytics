import pandas as pd

print("Pipeline de ingestão de dados iniciando")

caminho = "data/raw/ecom_data.csv"

try:
    df = pd.read_csv(caminho)
    print("Dados carregados com sucesso!")
    
    print("Primeiras linhas do dataset:")
    print(df.head())
    print("Informações do dataset:")
    print(df.info())

except FileNotFoundError:
    print("Arquivo não encontrado. Tente executar primeiramente o script gera_dados.py")
