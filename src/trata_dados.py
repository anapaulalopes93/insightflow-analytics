import pandas as pd

print("Iniciando transformação dos dados.")

df = pd.read_csv("data/raw/ecom_data.csv")

df.columns = df.columns.str.replace(" ", "_")

df = df.dropna()
df = df.drop_duplicates()

df["Valor_Total"] = df["Valor_Unitario"] * df["Quantidade"]
print("A coluna Valor_Total foi criada!")

df["Data_Venda"] = pd.to_datetime(df["Data_Venda"])
df["Valor_Unitario"] = df["Valor_Unitario"].astype(float)
df["Valor_Total"] = df["Valor_Total"].astype(float)

df.to_csv("data/processed/ecom_data_tratado.csv", index = False)
print("Dataset tratado salvo em data/processed")