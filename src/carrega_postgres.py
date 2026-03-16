import pandas as pd
from sqlalchemy import create_engine

print("Enviando dados para o PostgreSQL.")
df = pd.read_csv("data/processed/ecom_data_tratado.csv")

engine = create_engine("postgresql://postgres:postgres@localhost:5432/insightflow")
df.to_sql("vendas",
          engine,
          if_exists = "replace",
          index = False)
print("Dados enviados com sucesso!")