import pandas as pd
import streamlit as st
import numpy as np


url = 'https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/survey_data.csv'
dados = pd.read_csv(url)

dados_tratados = dados[['ResponseId', 'MainBranch', 'Age', 'Employment',
                        'YearsCodePro', 'DevType', 'Country','AISearchDevHaveWorkedWith',
                        'AISearchDevWantToWorkWith', 'AISearchDevAdmired', 'AISelect', 'AISent',
                        'AIBen', 'AIAcc', 'AIComplex', 'AIThreat', 'ProfessionalQuestion', 'Industry', 'JobSat']]

dados_tratados = dados_tratados.dropna(subset=['AISearchDevHaveWorkedWith', 'AISearchDevWantToWorkWith', 'AISearchDevAdmired'])

AI_search = dados_tratados[['AISearchDevHaveWorkedWith', 'AISearchDevWantToWorkWith', 'AISearchDevAdmired']]

have_worked_ia = AI_search['AISearchDevHaveWorkedWith'].str.get_dummies(';')
want_to_work_ia = AI_search['AISearchDevWantToWorkWith'].str.get_dummies(';')
admired_ia = AI_search['AISearchDevAdmired'].str.get_dummies(';')

dados = pd.concat([dados_tratados, have_worked_ia], axis=1)

st.write('Dados tratados do Survey Stack Overflow 2024')

st.dataframe(dados.head())

resultado_paises = dados.groupby('Country')['ChatGPT'].sum()

have_worked_ia_results = {}

for i in have_worked_ia.columns:
    soma = have_worked_ia[i].sum()
    have_worked_ia_results[i] = soma

total_worked = sum(have_worked_ia_results.values())
have_worked_ia_results = {chave: round((valor / total_worked) * 100, 1) for chave, valor in have_worked_ia_results.items()}

sum(have_worked_ia_results.values())
have_worked_ia_results = dict(sorted(have_worked_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])

st.write('Top 5 - IAs mais utilizadas em 2023')

if st.button('Mostrar gráfico'):
    st.bar_chart(have_worked_ia_results)



