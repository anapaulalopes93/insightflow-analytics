# InsightFlow Analytics
Projeto de análise de dados de e-commerce desenvolvido para o desafio de Dados (Data Analytics) do PD - Projeto Desenvolve

## Objetivo
Transformar dados brutos de vendas em insights de negócio utilizando Python, ETL e Visualização Interativa de um dataset simulado.

**Sprint 1**: Ingestão e ETL (Limpeza de Dados)
- Geração do dataset simulado (ecom_data.csv) com 5000 linhas ou mais;
- Tratamento de valores nulos, duplicados e inconsistentes;
- Padronização de formatos (datas, moedas) e
- Carga dos dados tratados num banco de dados relacional.

## Tecnologias utilizadas
- Python
- Pandas
- PostgreSQL
- SQLAlchemy

## Estrutura do Projeto
```
insightflow-analytics

    data
    ├── raw
    │   └── ecom_data.csv
    |
    └── processed
        └── ecom_data_tratado.csv

    src
    ├── gera_dados.py
    ├── ingestao_dados.py
    ├── trata_dados.py
    └── carrega_postgres.py

    ├── .gitignore
    ├── requirements.txt
    └── README.md


                   gera_dados.py
                        ↓
                ingestao_dados.py
                        ↓
                   trata_dados.py
                        ↓
               carrega_postgres.py
                        ↓
                    PostgreSQL
```

## Como Rodar
1. Clonar o repositório:
```
git clone https://github.com/anapaulalopes93/insightflow-analytics.git
cd insightflow-analytics
```
2. Criar e ativar o ambiente virtual:
```
python3 -m venv .venv
source .venv/bin/activate   # Para ativar no Linux/macOS
.venv\Scripts\activate      # Para ativar no Windows
```
3. Instalar dependências:
```
pip install -r requirements.txt
```
4. Gerar o dataset simulado:
```
python src/gera_dados.py
```
- O dataset será salvo em data/raw/ecom_data.csv

5. Tratar os dados e padronizar formatos:
```
python src/trata_dados.py
```
- Os dados tratados serão salvos em data/processed/ecom_data_tratado.csv

6. Carregar os dados tratados no banco de dados:
```
python src/carrega_postgres.py
```
- Os dados serão inseridos em um banco de dados relacional configurado em src/carrega_postgres.py

## Pipeline de Dados
1. Geração de dataset simulado de e-commerce
2. Ingestão de dados
3. Transformação (ETL)
4. Análise de vendas
5. Dashboard interativo

**Observação: nessa sprint não inclui as análises e o dashboard.**
