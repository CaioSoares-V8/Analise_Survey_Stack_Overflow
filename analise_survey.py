import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
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
        options=["Home", "Análise", "Opiniões"],
        icons=["house", "graph-up", "chat-left-dots"], 
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

    st.write(survey_data.head())

elif selected == 'Análise':
    st.title('Análise')
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')
    st.divider()

    # Porcentagem de utilização de IA
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')
    valor = 35.543 # Usuários que relataram uso de IA na pesquisa
    total = 65.437 # Total de usuários (Dado retirado do DataFrame sem o tratamento de dados nulos)
    porcentagem_valor = (valor / total) * 100
    porcentagem_restante = 100 - porcentagem_valor

    total_uso_ia = pd.DataFrame({
        'Categoria': ['Utilizam IA', 'Não utilizaram IA'],
        'Porcentagem': [porcentagem_valor, porcentagem_restante]
    })

    fig = px.bar(total_uso_ia,
                x='Categoria',
                y='Porcentagem', 
                title='Porcentagem de utilização de IA', 
                labels={'Porcentagem': 'Porcentagem (%)'}, 
                text='Porcentagem')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

    st.plotly_chart(fig)

    # Top 5 IAs mais utilizadas
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')
    
    have_worked_ia_results = {}
    for i in have_worked_ia.columns:
        soma = have_worked_ia[i].sum()
        have_worked_ia_results[i] = soma

    total_worked = sum(have_worked_ia_results.values())
    have_worked_ia_results = {chave: round((valor / total_worked) * 100, 1) for chave, valor in have_worked_ia_results.items()}
    have_worked_ia_results = dict(sorted(have_worked_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])
    ias = list(have_worked_ia_results.keys())
    porcentagens = list(have_worked_ia_results.values())

    fig = px.bar(x=ias,
                y=porcentagens,
                labels={'x': 'IA', 'y': 'Porcentagem (%)'},
                title='Top 5 IAs mais utilizadas')
    st.plotly_chart(fig)

    # Top 5 IAs que mais buscam trabalhar
    want_to_work_ia_results = {}
    for i in want_to_work_ia.columns:
        soma = want_to_work_ia[i].sum()
        want_to_work_ia_results[i] = soma

    total_want = sum(want_to_work_ia_results.values())
    want_to_work_ia_results = {chave: round((valor / total_want) * 100, 1) for chave, valor in want_to_work_ia_results.items()}
    want_to_work_ia_results = dict(sorted(want_to_work_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])
    ias = list(want_to_work_ia_results.keys())
    porcentagens = list(want_to_work_ia_results.values())

    fig = px.bar(x=ias,
                y=porcentagens,
                labels={'x': 'IA', 'y': 'Porcentagem (%)'},
                title='Top 5 IAs que mais buscam trabalhar')
    st.plotly_chart(fig)

    # Top 5 IAs mais admiradas
    admired_ia_results = {}
    for i in admired_ia.columns:
        soma = admired_ia[i].sum()
        admired_ia_results[i] = soma

    total_admired = sum(admired_ia_results.values())
    admired_ia_results = {chave: round((valor / total_admired) * 100, 1) for chave, valor in admired_ia_results.items()}
    admired_ia_results = dict(sorted(admired_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])
    ias = list(admired_ia_results.keys())
    porcentagens = list(admired_ia_results.values())

    fig = px.bar(x=ias,
                y=porcentagens,
                labels={'x': 'IA', 'y': 'Porcentagem (%)'},
                title='Top 5 IAs mais admiradas')
    st.plotly_chart(fig)

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
                title='Maiores participações de paises na Pesquisa',
                color='Usuários',
                color_continuous_scale=px.colors.sequential.Blues)
    st.plotly_chart(fig)

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

    # Utilização de IA por faixa etaria
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')
    
    resultado_faixa_etaria = survey_data.groupby('Age')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
    resultado_long = resultado_faixa_etaria.melt(id_vars='Age', var_name='IA', value_name='Quantidade')

    fig = px.line(resultado_long, 
                x='Age', 
                y='Quantidade', 
                color='IA', 
                title='Utilização de Ferramentas de IA por Faixa Etária',
                labels={'Age': 'Faixa Etária', 'Quantidade': 'Quantidade de Usuários'})

    st.plotly_chart(fig)
    
    def somatoria(IA):
        return resultado_faixa_etaria[IA].sum()

    lista_IA = ['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']
    IA_selecionada = st.selectbox('Selecione uma IA:', lista_IA)
    st.write(f'A soma de usuários em todas as faixas etárias que utilizam o {IA_selecionada} é: {somatoria(IA_selecionada)}')

    st.divider()

     # Utilização de IA por tipo de desenvolvedor
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')

    resultado_funcao = survey_data.groupby('DevType')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
    tipo_selecionado = st.selectbox('Selecione o tipo de desenvolvedor', survey_data['DevType'].unique())
    resultado_funcao = resultado_funcao[resultado_funcao['DevType'] == tipo_selecionado]
    df_long = resultado_funcao.melt(id_vars='DevType', var_name='IA', value_name='Usuários')

    fig = px.bar(df_long,
                x='IA',
                y='Usuários',
                title=f'Utilização de IAs por {tipo_selecionado}')
    st.plotly_chart(fig)

    st.divider()

    # Utilização de IA por anos de experiencia
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')

    resultado_code_pro = survey_data.groupby('YearsCodePro')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
    resultado_long = resultado_code_pro.melt(id_vars='YearsCodePro', var_name='IA', value_name='Quantidade')

    fig = px.bar(resultado_long, 
                x='YearsCodePro', 
                y='Quantidade', 
                color='IA', 
                title='Utilização de Ferramentas de IA anos de experiencia',
                labels={'YearsCodePro': 'Anos de Experiencia', 'Quantidade': 'Quantidade de Usuários'})

    st.plotly_chart(fig)

    st.divider()

    # Linguagens mais utilizadas
    st.write('Lorem ipsum dolor sit amet. Et error ipsam qui reprehenderit dolor qui deserunt quia a voluptatem tenetur aut labore modi et exercitationem veniam. Qui nesciunt quas vel modi quia non quos atque hic saepe consequatur cum tempore dolor. Eos temporibus blanditiis At corporis maxime est quia minus et voluptas excepturi At rerum explicabo.')

    have_worked_language_results = {}
    for i in have_worked_language.columns:
        soma = have_worked_language[i].sum()
        have_worked_language_results[i] = soma

    total_worked = sum(have_worked_language_results.values())
    have_worked_language_results = dict(sorted(have_worked_language_results.items(), key=lambda x: x[1], reverse=True)[:10])
    languages = list(have_worked_language_results.keys())
    usuarios = list(have_worked_language_results.values())

    fig = px.bar(x=usuarios,
                y=languages,
                orientation='h',
                labels={'x': 'Quantidade de usuários', 'y': 'Linguagens'},
                title='Top 10 Linguagens de progamação mais utilizadas')
    st.plotly_chart(fig)

elif selected == 'Opiniões':
     # Opinião dos desenvolvedores

    def opiniao_desenvolvedores(selected_IA):
        # Grupo por 'AISelect'
        resultado_AISelect = survey_data.groupby('AISelect')[selected_IA].sum().reset_index()
        st.write(resultado_AISelect)
        fig_AISelect = px.bar(resultado_AISelect, x='AISelect', y=selected_IA, title='Opinião sobre AI Select')
        st.plotly_chart(fig_AISelect)

        # Grupo por 'AISent'
        resultado_AISent = survey_data.groupby('AISent')[selected_IA].sum().reset_index()
        st.write(resultado_AISent)
        fig_AISent = px.bar(resultado_AISent, x='AISent', y=selected_IA, title='Opinião sobre AI Sentiment')
        st.plotly_chart(fig_AISent)

        # Grupo por 'AIAcc'
        resultado_AIAcc = survey_data.groupby('AIAcc')[selected_IA].sum().reset_index()
        st.write(resultado_AIAcc)
        fig_AIAcc = px.bar(resultado_AIAcc, x='AIAcc', y=selected_IA, title='Opinião sobre AI Accuracy')
        st.plotly_chart(fig_AIAcc)

        # Grupo por 'AIComplex'
        resultado_AIComplex = survey_data.groupby('AIComplex')[selected_IA].sum().reset_index()
        st.write(resultado_AIComplex)
        fig_AIComplex = px.bar(resultado_AIComplex, x='AIComplex', y=selected_IA, title='Opinião sobre AI Complexity')
        st.plotly_chart(fig_AIComplex)

        # Grupo por 'AIThreat'
        resultado_AIThreat = survey_data.groupby('AIThreat')[selected_IA].sum().reset_index()
        st.write(resultado_AIThreat)
        fig_AIThreat = px.bar(resultado_AIThreat, x='AIThreat', y=selected_IA, title='Opinião sobre AI Threats')
        st.plotly_chart(fig_AIThreat)

    select_IA = ['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']
    selected_IA = st.selectbox('Selecione uma IA e veja as opiniões dos usuários dela', select_IA)

    opiniao_desenvolvedores(selected_IA)

