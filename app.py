import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Análise de Postos de Combustíveis")

@st.cache_data
def load_data():
    df = pd.read_csv('dados_postos_limpos.csv', parse_dates=['DATAPUBLICACAO', 'DATAVINCULACAO'])
    return df

df = load_data()

ufs = df['UF'].unique()
bandeiras = df['BANDEIRA'].unique()

selected_ufs = st.sidebar.multiselect('Selecione os Estados (UF): ', options=ufs, default=ufs)
selected_bandeiras = st.sidebar.multiselect('Selecione as Bandeiras: ', options=bandeiras, default=bandeiras)

data_min = df['DATAPUBLICACAO'].min()
data_max = df['DATAPUBLICACAO'].max()
selected_periodo = st.sidebar.date_input(
    'Selecione o período de publicação: ', 
    value=[data_min, data_max]
)

df_filtrado = df[
    (df['UF'].isin(selected_ufs)) &
    (df['BANDEIRA'].isin(selected_bandeiras)) &
    (df['DATAPUBLICACAO'] >= pd.to_datetime(selected_periodo[0])) &
    (df['DATAPUBLICACAO'] <= pd.to_datetime(selected_periodo[1]))
]

st.subheader("Indicadores")
col1, col2, col3 = st.columns(3)
col1.metric("Total de Postos", df_filtrado['CODIGOISIMP'].nunique())
col2.metric("Total de Publicações", len(df_filtrado))
col3.metric("Bandeira mais Frequente", df_filtrado['BANDEIRA'].mode()[0] if not df_filtrado.empty else "N/A")

df_uf = df_filtrado.groupby('UF').size().reset_index(name='Quantidade')
fig_mapa = px.choropleth(
    df_uf,
    locations='UF',
    locationmode='USA-states',
    color='Quantidade',
    scope='south america',
    color_continuous_scale='Viridis',
    labels={'Quantidade':'Número de Postos'},
    title='Número de Postos por Estado'
)
st.plotly_chart(fig_mapa, use_container_width=True)

df_bandeira = df_filtrado['BANDEIRA'].value_counts().reset_index()
df_bandeira.columns = ['Bandeira', 'Quantidade']
fig_barras = px.bar(
    df_bandeira.head(10),
    x='Bandeira',
    y='Quantidade',
    title='Top 10 Bandeiras mais Frequentes',
    labels={'Quantidade':'Número de Postos', 'Bandeira':'Bandeira'}
)
st.plotly_chart(fig_barras, use_container_width=True)

df_filtrado = df_filtrado.copy()
df_filtrado['MesAno'] = df_filtrado['DATAPUBLICACAO'].dt.to_period('M')
df_tempo = df_filtrado.groupby('MesAno').size().reset_index(name='Quantidade')
df_tempo['MesAno'] = df_tempo['MesAno'].dt.to_timestamp()
fig_linha = px.line(
    df_tempo,
    x='MesAno',
    y='Quantidade',
    title='Publicações por Mês',
    labels={'MesAno':'Mês/Ano', 'Quantidade':'Número de Publicações'}
)
st.plotly_chart(fig_linha, use_container_width=True)
