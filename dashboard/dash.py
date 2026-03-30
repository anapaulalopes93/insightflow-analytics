import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title = "InsightFlow Analytics",
                   layout = "wide")

st.title("InsightFlow Analytics")
st.caption("Dashboard de Vendas de E-commerce")

engine = create_engine("postgresql://postgres:postgres@localhost:5432/insightflow")
df = pd.read_sql("SELECT * FROM vendas", engine)
df.columns =df.columns.str.lower()
df["data_venda"] = pd.to_datetime(df["data_venda"])

st.sidebar.header("Filtros")
categoria = st.sidebar.multiselect("Categoria",
                                   df["categoria_produto"].unique())

data_inicio = st.sidebar.date_input("Data inicial", df["data_venda"].min())
data_fim = st.sidebar.date_input("Data final", df["data_venda"].max())

df = df[(df["data_venda"] >= pd.to_datetime(data_inicio)) &
        (df["data_venda"] <= pd.to_datetime(data_fim))]
if categoria:
    df = df[df["categoria_produto"].isin(categoria)]

col1, col2, col3, col4 = st.columns(4)
faturamento = df["valor_total"].sum()
vendas = df.shape[0]
produtos = df["quantidade"].sum()
ticket = faturamento / vendas if vendas > 0 else 0

col1.metric("Faturamento", f"R$ {faturamento:,.0f}")
col2.metric("Vendas", vendas)
col3.metric("Produtos vendidos", produtos)
col4.metric("Ticket médio", f"R$ {ticket:,.2f}")

st.divider()

col1, col2 = st.columns(2)

cat = df.groupby("categoria_produto")["valor_total"].sum().reset_index()
figura1 = px.bar(cat,
                 x = "categoria_produto",
                 y = "valor_total",
                 color = "categoria_produto",
                 title = "Vendas por Categoria")
col1.plotly_chart(figura1, use_container_width = True)

produtos = df.groupby("nome_produto")["quantidade"].sum().reset_index()
figura2 = px.bar(produtos.sort_values("quantidade", ascending = False),
                 x = "nome_produto",
                 y = "quantidade",
                 color = "nome_produto",
                 title = "Produtos Mais Vendidos")
col2.plotly_chart(figura2, use_container_width = True)

vendas_data = df.groupby("data_venda")["valor_total"].sum().reset_index()
figura_data = px.line(vendas_data,
                      x = "data_venda",
                      y = "valor_total",
                      title = "Evolução das Vendas ao Longo do Tempo")
st.plotly_chart(figura_data, use_container_width = True)


# if categoria:
#     df = df[df["categoria_produto"].isin(categoria)]

# # ------- LINHA DO TEMPO ------

# df = pd.read_csv("data/processed/ecom_data_tratado.csv")

# faturamento_total = df["Valor_Total"].sum()
# st.metric("Faturamento Total", f"R${faturamento_total:,.2f}")

# categoria = st.selectbox("Filtrar por categoria", ["Todas"] + list(df["Categoria_Produto"].unique()))

# if categoria != "Todas":
#     df = df[df["Categoria_Produto"] == categoria]

# vendas_categoria = df.groupby("Categoria_Produto")["Valor_Total"].sum().reset_index()
# figura_categoria = px.bar(vendas_categoria,
#                           x = "Categoria_Produto",
#                           y = "Valor_Total",
#                           title = "Vendas Por Categoria")
# st.plotly_chart(figura_categoria)

# produtos_vendidos = df.groupby("Nome_Produto")["Quantidade"].sum().reset_index()
# figura_produtos = px.bar(produtos_vendidos.sort_values("Quantidade", ascending = False),
#                          x = "Nome_Produto",
#                          y = "Quantidade",
#                          title = "Produtos Mais Vendidos")
# st.plotly_chart(figura_produtos)
