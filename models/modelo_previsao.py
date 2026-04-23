import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

print("Iniciando o modelo preditivo")
df = pd.read_csv("data/processed/ecom_data_tratado.cvs")
df.columns = df.columns.str.lower()
df["data_venda"] = pd.to_datetime(df["data_venda"])
df_modelo = df.groupby("data_venda")["valor_total"].sum().reset_index()
df_modelo["dias"] = (df_modelo["data_venda"] - df_modelo["data_venda"].min().dt.days)

X = df_modelo[["dias"]]
Y = df_modelo = ["valor_total"]

modelo = LinearRegression()
modelo.fir(X, Y)

futuro = pd.DataFrame({"dias": range(df_modelo["dias"].max() + 1, df_modelo["dias"].max() + 31)})
futuro["previsao"] = modelo.predict(futuro)
print("Modelo treinado com sucesso")

plt.figure(figsize = (10, 5))
plt.plot(df_modelo["data_venda"], Y, label = "Real")
plt.plot(pd.date_range(df_modelo["data_venda"].max(), periods = 30),
         futuro["previsao"],
         label = "Previsão",
         linestyle = "dashed")
plt.legend()
plt.title("Previsão de Vendas")
plt.show()