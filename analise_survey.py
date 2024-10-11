import pandas as pd
import streamlit as st
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
        default_index=0,
        styles={
        "container": {"padding": "0!important", "background-color": "transparent"},
        "nav-link-selected": {"background-color": "#777777"}
    }
    )

if selected == 'Home':
    st.title('Análise Survey Stack Overflow 2024')
    st.subheader('Contexto')
    st.write('O Survey Stack Overflow é uma pesquisa anual realizada pela plataforma Stack Overflow, que coleta dados sobre desenvolvedores ao redor do mundo. Ela aborda temas como linguagens de programação, tecnologias, carreira, ferramentas, frameworks, ambientes de desenvolvimento, bem como tendências e desafios que os profissionais enfrentam. A pesquisa oferece insights sobre o perfil dos desenvolvedores, suas preferências tecnológicas, práticas de trabalho, e a adoção de novas tecnologias, como inteligência artificial. Esses dados são amplamente utilizados por empresas e a comunidade de tecnologia para entender tendências do mercado, melhorar produtos, e orientar decisões estratégicas.')
    st.write('Com o crescimento exponencial da Inteligência Artificial (IA) e seu impacto nas práticas de desenvolvimento de software, a pesquisa fornece uma oportunidade única para entender como os profissionais de tecnologia estão adotando e utilizando ferramentas de IA em seus trabalhos. Este projeto visa analisar os dados da pesquisa para identificar tendências, preferências e insights sobre o uso de IA entre programadores de diferentes linguagens, faixas etárias, funções e paises.')
    st.caption('Desenvolvido por Caio Soares')

elif selected == 'Análise':
    st.title('Análise dos dados')
    st.write('Nesta análise, partimos dos registros brutos da pesquisa do Stack Overflow 2024, filtramos e tratamos os dados para garantir a relevância e a precisão da informação. Após esse processo, obtivemos um DataFrame final contendo 1.563.892 dados, distribuídos em 35.543 linhas e 44 colunas. A partir desse conjunto, exploramos a relação entre as linguagens de programação, funções de desenvolvimento, paises, faixas etárias, experiência profissional e o uso de ferramentas de inteligência artificial, destacando tendências no setor de tecnologia.')
    st.divider()

    # Porcentagem de utilização de IA
    st.write('Para otimizar o aproveitamento dos registros da pesquisa em nossa análise, optamos por utilizar apenas os dados dos usuários que relataram o uso de inteligência artificial em suas atividades (54,32%). Esse filtro nos permitiu focar nas respostas mais relevantes, garantindo que as tendências e insights gerados fossem diretamente relacionados à utilização de ferramentas IA.')
    valor = 35.543 # Usuários que relataram uso de IA na pesquisa
    total = 65.437 # Total de usuários (Dado retirado do DataFrame sem o tratamento de dados nulos)
    porcentagem_valor = (valor / total) * 100
    porcentagem_restante = 100 - porcentagem_valor

    total_uso_ia = pd.DataFrame({
        'Categoria': ['Utilizaram IA', 'Não utilizaram IA'],
        'Porcentagem': [porcentagem_valor, porcentagem_restante]
    })

    fig = px.bar(total_uso_ia,
                x='Categoria',
                y='Porcentagem', 
                title='Porcentagem de utilização de IA no último ano', 
                labels={'Porcentagem': 'Porcentagem (%)'}, 
                text='Porcentagem')
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')

    st.plotly_chart(fig)

    # Top 5 IAs mais utilizadas
    st.write('Iremos explorar as percepções dos desenvolvedores em relação às ferramentas de inteligência artificial, destacando agora três categorias gerais: as cinco IAs mais utilizadas no último ano, as cinco IAs que os desenvolvedores mais desejam utilizar no próximo ano e as cinco IAs que eles mais admiram. Essa abordagem permite uma visão abrangente sobre o cenário atual da IA no desenvolvimento de software, identificando quais ferramentas estão em uso, quais são as preferências futuras e quais soluções são consideradas admiráveis por sua inovação e eficácia.')
    
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
                title='Top 5 IAs mais utilizadas no último ano')
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
                title='Top 5 IAs que mais buscam trabalhar no próximo ano')
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
    st.write('Para complementar nossa análise, apresentamos um gráfico que destaca os principais países representados na pesquisa por quantidade de usuários, ilustrando a distribuição dos desenvolvedores que participaram do estudo.')
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
    st.write('Uma das funcionalidades da nossa análise é a de selecionar uma ferramenta de inteligência artificial específica e permitir a visualização sobre quais países a utilizam com mais frequência. Essa abordagem permite identificar tendências regionais e reconhecer onde cada ferramenta é mais popular.')
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
    st.write('Realizamos uma comparação das cinco IAs mais utilizadas em relação às diferentes faixas etárias dos desenvolvedores. Essa análise nos permite entender como a adoção de ferramentas de inteligência artificial varia conforme a idade dos profissionais, revelando possíveis diferenças nas preferências e no nível de experiência com essas tecnologias.')
    
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
    st.write('Estabelecemos uma relação entre as ferramentas de inteligência artificial e os diferentes tipos de desenvolvedores, como desenvolvedores front-end, back-end, full stack e de dados. Essa análise revela como as preferências por IAs variam conforme a especialização dos profissionais, destacando quais ferramentas são mais populares entre cada tipo de desenvolvedor. Selecione uma função específica e visualize quais IAs são mais utilizadas por profissionais dessa categoria.')

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
    st.write('Analisamos a relação entre a utilização de ferramentas de inteligência artificial e os anos de experiência profissional dos desenvolvedores. Essa abordagem nos permite observar como a adoção de IAs varia de acordo com o nível de experiência, identificando quais ferramentas são mais utilizadas por profissionais iniciantes em comparação com aqueles com mais anos de atuação no setor')

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
    st.write('Apresentamos agora um gráfico que ilustra as 10 linguagens de programação mais utilizadas pelos desenvolvedores participantes da pesquisa. Essa visualização nos permite, no futuro, comparar essas linguagens com as preferências dos profissionais em relação às ferramentas de inteligência artificial, oferecendo insights sobre como as escolhas de programação podem influenciar a adoção de IAs no setor.')

    have_worked_language_results = {}
    for i in have_worked_language.columns:
        soma = have_worked_language[i].sum()
        have_worked_language_results[i] = soma

    total_worked = sum(have_worked_language_results.values())
    have_worked_language_results = dict(sorted(have_worked_language_results.items(), key=lambda x: x[1], reverse=True)[:10])
    percentages = [soma / total_worked * 100 for soma in have_worked_language_results.values()]
    languages = list(have_worked_language_results.keys())
    usuarios_percent = percentages

    fig = px.bar(x=usuarios_percent,
                y=languages,
                orientation='h',
                labels={'x': 'Porcentagem de usuários (%)', 'y': 'Linguagens'},
                title='Top 10 Linguagens de Programação mais utilizadas')

    st.plotly_chart(fig)

    
    dados_combinados = pd.concat([have_worked_ia[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']],
                                have_worked_language[['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'TypeScript']]],
                                axis=1)

    def usabilidade_por_linguagem(data, language):
        language_users = data[data[language] == 1]
        ia_counts = language_users[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum()

        return ia_counts

    st.write('Disponibilizamos a funcionalidade de selecionar uma linguagem de programação específica e visualizar a adoção de ferramentas de inteligência artificial associadas a ela. Essa funcionalidade permite que os usuários explorem como a preferência por uma linguagem pode impactar a escolha das IAs utilizadas, oferecendo uma compreensão mais profunda das interações entre linguagens de programação e tecnologias de inteligência artificial no ambiente de desenvolvimento.')

    linguagem_selecionada = st.selectbox("Selecione uma linguagem de programação:", ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'TypeScript'])

    ia_usage = usabilidade_por_linguagem(dados_combinados, linguagem_selecionada)
    st.write(f"IAs utilizadas por usuários que programam em {linguagem_selecionada}:")
    st.bar_chart(ia_usage)

elif selected == 'Opiniões':
     # Opinião dos desenvolvedores
    st.title('Opiniões dos desenvolvedores')
    st.write('Nesta seção dedicada às opiniões dos usuários, apresentamos de forma gráfica as experiências e feedbacks sobre a ferramenta de inteligência artificial selecionada. Isso nos proporciona uma compreensão mais profunda da usabilidade, eficácia, precisão, limitações e impacto dessa IA em seus projetos. As respostas  da pesquisa oferecem insights valiosos que podem orientar a escolha da ferramenta mais adequada, além de destacar áreas que necessitam de melhorias e os desafios potenciais enfrentados durante a utilização.')

    def opiniao_desenvolvedores(selected_IA):
        # AISelect
        st.subheader(f'Você atualmente utiliza o {selected_IA} no seu processo de desenvolvimento?')
        resultado_AISelect = survey_data.groupby('AISelect')[selected_IA].sum().reset_index()
        fig_AISelect = px.bar(resultado_AISelect, x='AISelect', y=selected_IA, title='Opinião sobre AI Select')
        st.plotly_chart(fig_AISelect)

        # AISent
        st.subheader(f'Quão favorável é sua opinião sobre o uso do {selected_IA} como parte do seu fluxo de trabalho em desenvolvimento?')
        resultado_AISent = survey_data.groupby('AISent')[selected_IA].sum().reset_index()
        fig_AISent = px.bar(resultado_AISent, x='AISent', y=selected_IA, title='Opinião sobre AI Sentiment')
        st.plotly_chart(fig_AISent)

        # AIAcc
        st.subheader(f'Quanto você confia na precisão dos resultados do {selected_IA}?')
        resultado_AIAcc = survey_data.groupby('AIAcc')[selected_IA].sum().reset_index()
        fig_AIAcc = px.bar(resultado_AIAcc, x='AIAcc', y=selected_IA, title='Opinião sobre AI Accuracy')
        st.plotly_chart(fig_AIAcc)

        # AIComplex
        st.subheader(f'Como você avalia o {selected_IA} na execução de tarefas complexas?')
        resultado_AIComplex = survey_data.groupby('AIComplex')[selected_IA].sum().reset_index()
        fig_AIComplex = px.bar(resultado_AIComplex, x='AIComplex', y=selected_IA, title='Opinião sobre AI Complexity')
        st.plotly_chart(fig_AIComplex)

        # AIThreat
        st.subheader(f'Você acredita que o {selected_IA} é uma ameaça para seu trabalho atual?')
        resultado_AIThreat = survey_data.groupby('AIThreat')[selected_IA].sum().reset_index()
        fig_AIThreat = px.bar(resultado_AIThreat, x='AIThreat', y=selected_IA, title='Opinião sobre AI Threats')
        st.plotly_chart(fig_AIThreat)

    select_IA = ['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']
    selected_IA = st.selectbox('Selecione uma IA e veja as opiniões dos usuários dela', select_IA)

    opiniao_desenvolvedores(selected_IA)

