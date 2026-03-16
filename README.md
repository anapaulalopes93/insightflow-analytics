# InsightFlow Analytics
Projeto de análise de dados de e-commerce desenvolvido para o desafio de Dados (Data Analytics) do PD - Projeto Desenvolve

## Objetivo
Transformar dados brutos de vendas em insights de negócio utilizando Python, ETL e Visualização Interativa.

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
 └── analise_dados.py

requeriments.txt
README.md

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

## Pipeline de Dados
1. Geração de dataset simulado de e-commerce
2. Ingestão de dados
3. Transformação (ETL)
4. Análise de vendas
5. Dashboard interativo
