# Análise de Preços de Combustíveis no Brasil

Este projeto é um dashboard interativo desenvolvido com **Streamlit**, que permite analisar dados de postos de combustíveis no Brasil. Utiliza as bibliotecas **Pandas** para manipulação de dados e **Plotly Express** para visualizações dinâmicas e responsivas.

---

## Objetivo

Criar um painel visual simples e funcional para explorar os dados dos preços e quantidade de postos de combustíveis, com filtros por estado (UF), bandeira da rede e período de publicação. 

---

## Funcionalidades

- Filtros interativos para estados, bandeiras e período de datas.
- Indicadores de KPI para total de postos, total de publicações e bandeira mais frequente.
- Mapa choropleth mostrando número de postos por estado.
- Gráfico de barras com as 10 bandeiras mais frequentes.
- Série temporal mostrando o número de publicações por mês.

---

## Tecnologias e Bibliotecas utilizadas

- [Python 3.x](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – Framework para criação rápida de apps web interativos.
- [Pandas](https://pandas.pydata.org/) – Manipulação e análise de dados.
- [Plotly Express](https://plotly.com/python/plotly-express/) – Visualização de dados interativa.
- [NumPy](https://numpy.org/) – Biblioteca de suporte para operações numéricas (indiretamente usada pelo Pandas).

---

## Como executar o projeto

### Pré-requisitos

- Python 3.7 ou superior instalado na sua máquina.
- Recomenda-se criar e ativar um ambiente virtual.

### Passos para rodar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/analise-combustiveis-br.git
cd analise-combustiveis-br

2. Crie um ambiente virtual (opcional, mas recomendado):
python -m venv venv

3. Ative o ambiente virtual:

* No Windows:
venv\Scripts\activate

* No Linux/macOS:
source venv/bin/activate

4. Instale as dependências:
pip install -r requirements.txt

5. Execute o app:
streamlit run app.py

6. O app abrirá automaticamente no navegador padrão. Se não abrir, acesse:
http://localhost:8501

