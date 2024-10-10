import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu
import plotly.express as px

survey_data = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/survey_data.csv')
have_worked_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/have_worked_ia.csv')
want_to_work_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/want_to_work_ia.csv')
admired_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/admired_ia.csv')
have_worked_language = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/have_worked_language.csv')


with st.sidebar:
    selected = option_menu(
        menu_title="Menu",
        options=["Home", "Análise"],
        icons=["house", "graph-up"], 
        menu_icon="list", 
        default_index=1,
        styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "nav-link-selected": {"background-color": "#777777"}
    }
    )

if selected == 'Home':
    st.title('Análise Survey Stack Overflow 2024')
    st.write('Com o avanço significativo dos Modelos de Inteligência Artificial LLM e o surgimento de diversas ferramentas que os utilizam, a empresa V8.Tech está interessada em incorporar algumas dessas soluções no dia a dia de seus colaboradores. Para tomar uma decisão mais assertiva sobre qual ferramenta adotar, foi solicitado que uma análise seja feita utilizando os registros de dados da pesquisa Survey Stack Overflow 2024, que em meio a tratativa de diversos assuntos relacionados a tecnologia, investigou o uso de IA entre profissionais de tecnologia e desenvolvimento, abordando questões como popularidade das ferramentas, confiabilidade e utilidade em tarefas mais complexas.')

elif selected == 'Análise':
    st.title('Análise')
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')
    st.divider()

# Top 10 participações de paises na Pesquisa
st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')
resultado_paises = survey_data['Country'].value_counts().head(10).reset_index()
resultado_paises.columns = ['Países', 'Usuários'] 
resultado_paises['Países'] = resultado_paises['Países'].replace({
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom'
})
fig = px.bar(resultado_paises, 
              x='Usuários', 
              y='Países', 
              orientation='h', 
              title='Maiores articipações de paises na Pesquisa',
              color='Usuários',
              color_continuous_scale=px.colors.sequential.Blues)
st.plotly_chart(fig)
st.divider()

# Top 10 Utilização de IA por Paises
st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')
def utilizacao_por_pais(data, coluna):
    utilizacao_paises = data.groupby('Country')[coluna].sum().sort_values(ascending=False).head(10).reset_index()
    utilizacao_paises['Country'] = utilizacao_paises['Country'].replace({
        'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom'
    })
    fig = px.bar(utilizacao_paises,
                  x=coluna,
                  y='Country',
                  orientation='h',
                  title=f'Paises que mais utilizam o {coluna}',
                  color=coluna,
                  color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig)

lista_IA = have_worked_ia.columns.tolist() 
IA_selecionada = st.selectbox('Selecione uma IA:', lista_IA)
utilizacao_por_pais(survey_data, IA_selecionada)

st.divider()

# Top 10 IAs mais utilizadas
have_worked_ia_results = {}

for i in have_worked_ia.columns:
    soma = have_worked_ia[i].sum()
    have_worked_ia_results[i] = soma

total_worked = sum(have_worked_ia_results.values())
have_worked_ia_results = {chave: round((valor / total_worked) * 100, 1) for chave, valor in have_worked_ia_results.items()}
sum(have_worked_ia_results.values())
have_worked_ia_results = dict(sorted(have_worked_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])

st.bar_chart(have_worked_ia_results)