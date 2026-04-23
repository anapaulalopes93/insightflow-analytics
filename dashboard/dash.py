import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title = "InsightFlow Analytics",
                   layout = "wide")

st.markdown(""" <style>
            .stApp{ background-color: #0F172A;}
            h1, h2, h3 { color: #E2E8F0; }
            [data-testid = "metric-container"] {
            background: linear-gradient(135deg, #1E293B, #0F172A);
            border: 1px solid #334155;
            border-radius: 12px;
            padding: 20px;
            box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.3); }
            section[data-testid="stSidebar"] {
            background-color: #020617; }
            label {
            color: #CBD5F5 !important; }
            </style> """, unsafe_allow_html = True)

st.markdown("""# InsightFlow Analytics""")
st.caption("Plataforma de Inteligência de Vendas")

@st.cache_data
def analise_dados():
    df = pd.read_csv("data/processed/ecom_data_tratado.csv")
    df.columns = df.columns.str.lower()
    df["data_venda"] = pd.to_datetime(df["data_venda"])
    df["data_formatada"] = df["data_venda"].dt.strftime("%d/%m/%Y")
    return df
df = analise_dados()

st.sidebar.header("Filtros")

categoria = st.sidebar.multiselect("Categoria",
                                   df["categoria_produto"].unique())

data_inicio = st.sidebar.date_input("Data inicial (dd/mm/aaaa)",
                                    df["data_venda"].min())
data_fim = st.sidebar.date_input("Data final (dd/mm/aaaa)",
                                 df["data_venda"].max())
st.sidebar.caption("Formato: dia/mês/ano")

df = df[(df["data_venda"] >= pd.to_datetime(data_inicio)) &
        (df["data_venda"] <= pd.to_datetime(data_fim))]

if categoria:
    df = df[df["categoria_produto"].isin(categoria)]

df["mes"] = df["data_venda"].dt.to_period("M")
df["ano"] = df["data_venda"].dt.year
st.subheader("Indicadores")
faturamento_total = df["valor_total"].sum()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Faturamento", f"R${faturamento_total:,.0f}")
col2.metric("Vendas", df.shape[0])
col3.metric("Produtos", int(df["quantidade"].sum()))
col4.metric("Ticket Médio", f"R${(faturamento_total / df.shape[0]):,.2f}")
st.divider()

st.subheader("Comparação Ano a Ano")
faturamento_ano = df.groupby("ano")["valor_total"].sum()
if len(faturamento_ano) >= 2:
    ano_atual = faturamento_ano.index.max()
    ano_anterior = ano_atual - 1

    valor_atual = faturamento_ano.loc[ano_atual]
    valor_anterior = faturamento_ano.loc[ano_anterior]

    variacao_ano = ((valor_atual - valor_anterior) / valor_anterior) * 100

    c1, c2, c3 = st.columns(3)
    c1.metric("Ano Atual", f"R${valor_atual:,.0f}")
    c2.metric("Ano Anterior", f"R${valor_anterior:,.0f}")
    c3.metric("Variação Ano a Ano", f"{variacao_ano:.2f}%")

vendas_ano = df.groupby(["ano", "mes"])["valor_total"].sum().reset_index()
vendas_ano["mes"] = vendas_ano["mes"].astype(str)
fig_ano = px.line(vendas_ano,
                  x = "mes",
                  y = "valor_total",
                  color = "ano",
                  markers = True)
fig_ano.update_layout(template = "plotly_dark")
st.plotly_chart(fig_ano, use_container_width = True)
st.divider()

st.subheader("Análises")
col1, col2 = st.columns(2)

cat = df.groupby("categoria_produto")["valor_total"].sum().reset_index()
fig1 = px.bar(cat,
              x = "categoria_produto",
              y = "valor_total",
              color = "categoria_produto",
              text_auto = True)
fig1.update_layout(template = "plotly_dark",
                   plot_bgcolor = "rgba(0, 0, 0, 0)",
                   paper_bgcolor = "rgba(0, 0, 0, 0)")
col1.plotly_chart(fig1, use_container_width = True)

prod = df.groupby("nome_produto")["quantidade"].sum().reset_index()
fig2 = px.bar(prod.sort_values("quantidade", ascending = False),
              x = "nome_produto",
              y = "quantidade",
              color = "nome_produto",
              text_auto = True)
fig2.update_layout(template = "plotly_dark",
                   plot_bgcolor = "rgba(0, 0, 0, 0)")
col2.plotly_chart(fig2, use_container_width = True)

st.subheader("Evolução das Vendas")

vendas_tempo = df.groupby("data_venda")["valor_total"].sum().reset_index()
fig3 = px.line(vendas_tempo,
               x = "data_venda",
               y = "valor_total",
               markers = True)
fig3.update_layout(template = "plotly_dark",
                   plot_bgcolor = "rgba(0, 0, 0, 0)",
                   xaxis_tickformat = "%d/%m/%Y")
st.plotly_chart(fig3, use_container_width = True)
st.divider()

st.subheader("Ranking Dinâmico")
col1, col2, col3 = st.columns(3)
dimensao = col1.selectbox("Dimensao", ["Produto", "Categoria"])
metrica = col2.selectbox("Métrica", ["Faturamento", "Quantidade"])
top_n = col3.slider("Exibir quantos itens?", 3, 10, 5)

if dimensao == "Produto":
    coluna = "nome_produto"
else:
    coluna = "categoria_produto"

if metrica == "Faturamento":
    valor = "valor_total"
else:
    valor = "quantidade"

ranking = (df.groupby(coluna)[valor].sum().reset_index().sort_values(valor, ascending = False).head(top_n))
fig_rank = px.bar(ranking,
                  x = coluna,
                  y = valor,
                  color = coluna,
                  text_auto = True)
fig_rank.update_layout(template = "plotly_dark")
st.plotly_chart(fig_rank, use_container_width = True)
st.dataframe(ranking, use_container_width = True)
if not ranking.empty:
    top_item = ranking.iloc[0]
    st.info(f"""Líder: {top_item[coluna]}
Valor: {top_item[valor]:,.0f}""")
st.divider()

st.subheader("Insights Estratégicos")
top_categoria = cat.sort_values("valor_total", ascending = False).iloc[0]
top_produto = prod.sort_values("quantidade", ascending = False).iloc[0]
st.success(f"Categoria líder de vendas: {top_categoria['categoria_produto']}")
st.success(f"Produto mais vendido: {top_produto['nome_produto']}")

st.markdown("----")
st.caption("Desenvolvido por Ana Paula Lopes Cruz PDITA174 | Projeto InsightFlow Analytics")