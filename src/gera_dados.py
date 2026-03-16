import pandas as pd
import random
from datetime import datetime, timedelta

print("Gerando dataset de e-commerce")

numero_linhas = 7500

produtos = [("Notebook", "Eletrônicos"),
            ("Mouse", "Acessórios"),
            ("Teclado", "Acessórios"),
            ("Monitor", "Eletrônicos"),
            ("Headset", "Áudio"),
            ("Cadeira Gamer", "Móveis"),
            ("Webcam", "Acessórios"),]

dados = []
data_inicial = datetime(2023, 1, 1)

for i in range(numero_linhas):
    produto = random.choice(produtos)
    linha = {"ID_Transacao": i + 1,
             "Data_Venda": data_inicial + timedelta(days = random.randint(0, 365)),
             "ID_Cliente": random.randint(1000, 5000),
             "Nome_Produto": produto[0],
             "Categoria_Produto": produto[1],
             "Valor_Unitario": round(random.uniform(50, 5000), 2),
             "Quantidade": random.randint(1, 5)}
    dados.append(linha)

df = pd.DataFrame(dados)
df.to_csv("data/raw/ecom_data.csv", index = False)
print("Dataset criado com sucesso em data/raw/ecom_data.csv")