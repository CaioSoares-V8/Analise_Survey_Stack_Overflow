import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


survey_data = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/survey_data.csv')

have_worked_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/have_worked_ia.csv')

want_to_work_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/want_to_work_ia.csv')

admired_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/admired_ia.csv')

st.title('Análise Survey Stack Overflow 2024')

st.dataframe(survey_data.head())
resultado_paises = survey_data.groupby('Country')['ChatGPT'].sum()

have_worked_ia_results = {}

for i in have_worked_ia.columns:
    soma = have_worked_ia[i].sum()
    have_worked_ia_results[i] = soma

want_to_work_ia_results = {}

for i in want_to_work_ia.columns:
    soma = want_to_work_ia[i].sum()
    want_to_work_ia_results[i] = soma

admired_ia_results = {}

for i in admired_ia.columns:
    soma = admired_ia[i].sum()
    admired_ia_results[i] = soma

total_worked = sum(have_worked_ia_results.values())
have_worked_ia_results = {chave: round((valor / total_worked) * 100, 1) for chave, valor in have_worked_ia_results.items()}
sum(have_worked_ia_results.values())
have_worked_ia_results = dict(sorted(have_worked_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])

total_want = sum(want_to_work_ia_results.values())
want_to_work_ia_results = {chave: round((valor / total_want) * 100, 1) for chave, valor in want_to_work_ia_results.items()}
sum(want_to_work_ia_results.values())
want_to_work_ia_results = dict(sorted(want_to_work_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])

total_admired = sum(admired_ia_results.values())
admired_ia_results = {chave: round((valor / total_admired) * 100, 1) for chave, valor in admired_ia_results.items()}
sum(admired_ia_results.values())
admired_ia_results = dict(sorted(admired_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])


st.write('Top 5 - IAs mais utilizadas em 2023')
st.bar_chart(have_worked_ia_results)

st.write('Top 5 - IAs que mais buscam trabalhar em 2025')
st.bar_chart(want_to_work_ia_results)

st.write('Top 5 - IAs mais admiradas em 2024')
st.bar_chart(admired_ia_results)

st.write('Agrupamento por faixa etária')
resultado_faixa_etaria = survey_data.groupby('Age')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_faixa_etaria)

st.write('Agrupamento por função')
resultado_funcao = survey_data.groupby('DevType')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_funcao)

st.write('Agrupamento por anos de experiencia')
resultado_code_pro = survey_data.groupby('YearsCodePro')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_code_pro.sort_values(by='YearsCodePro'))

st.write('Você atualmente utiliza ferramentas de IA no seu processo de desenvolvimento?')
resultado_AISelect = survey_data.groupby('AISelect')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_AISelect)

st.write("Quão favorável é sua opinião sobre o uso de ferramentas de IA como parte do seu fluxo de trabalho em desenvolvimento?")
resultado_AISent = survey_data.groupby('AISent')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_AISent)

st.write('Quanto você confia na precisão dos resultados das ferramentas de IA?')
resultado_AIAcc = survey_data.groupby('AIAcc')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_AIAcc)

st.write('Como você avalia as ferramentas de IA na execução de tarefas complexas?')
resultado_AIComplex = survey_data.groupby('AIComplex')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_AIComplex)

st.write('Você acredita que as IAs são uma ameaça para seu trabalho atual?')
resultado_AIThreat = survey_data.groupby('AIThreat')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_AIThreat)

st.write('De qual ramo sua empresa é?')
resultado_Industry = survey_data.groupby('Industry')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_Industry)

st.write('Qual seu nivel de satisfação atual com seu fluxo de trabalho?')
resultado_satisfacao = survey_data.groupby('JobSat')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
st.write(resultado_satisfacao)

