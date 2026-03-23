import pandas as pd

print("Iniciando a análise dos dados.\n")

df = pd.read_csv("data/processed/ecom_data_tratado.csv")

print("Estatísticas descritivas: ")
print(df.describe())

faturamento_total = df["Valor_Total"].sum()
print(f"Faturamento total: R${faturamento_total:,.2f}\n")

produtos_vendidos = df.groupby("Nome_Produto")["Quantidade"].sum().sort_values(ascending = False)
print("Produtos mais vendidos:\n")
print(produtos_vendidos.head())
print("\n")

vendas_categoria = df.groupby("Categoria_Produto")["Valor_Total"].sum()
print("Vendas por categoria:\n")
print(vendas_categoria)
print("\n")

print("Análise de possíveis outliers (Valor_Total):")
print(df["Valor_Total"].describe())
print("\n")

print("Correlação entre variáveis numéricas:")
print(df.corr(numeric_only = True))
print("\n")

print("Segmentação de clientes (RFM simplificado):")
df["Data_Venda"] = pd.to_datetime(df["Data_Venda"])

rfm = df.groupby("ID_Cliente").agg({
    "Data_Venda": "max",
    "ID_Transacao": "count",
    "Valor_Total": "sum"
})
rfm.columns = ["Recência", "Frequência", "Monetário"]
print(rfm.head())
print("\n")
print("Fim da análise.")
