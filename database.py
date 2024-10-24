import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

server = os.getenv('SQL_SERVER')
database = os.getenv('SQL_DATABASE')
username = os.getenv('SQL_USERNAME')
password = os.getenv('SQL_PASSWORD')

connection_string = f'mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server'

engine = create_engine(connection_string)


survey_data = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/survey_data.csv')
have_worked_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/have_worked_ia.csv')
want_to_work_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/want_to_work_ia.csv')
admired_ia = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/admired_ia.csv')
have_worked_language = pd.read_csv('https://raw.githubusercontent.com/CaioSoares-V8/Analise_Survey_Stack_Overflow/refs/heads/main/data/have_worked_language.csv')

# Uso de IA
valor = 35.543 # Usuários que relataram uso de IA na pesquisa
total = 65.437 # Total de usuários (Dado retirado do DataFrame sem o tratamento de dados nulos)
porcentagem_valor = (valor / total) * 100
porcentagem_restante = 100 - porcentagem_valor

total_uso_ia = pd.DataFrame({
    'Categoria': ['Utilizaram IA', 'Não utilizaram IA'],
    'Porcentagem': [porcentagem_valor, porcentagem_restante]
})

total_uso_ia.to_sql('total_uso_ia', engine, if_exists='replace', index=False)

import pandas as pd

# Calculando os 5 IAs mais utilizados
have_worked_ia_results = {}
for i in have_worked_ia.columns:
    soma = have_worked_ia[i].sum()
    have_worked_ia_results[i] = soma

total_worked = sum(have_worked_ia_results.values())
have_worked_ia_results = {chave: round((valor / total_worked) * 100, 1) for chave, valor in have_worked_ia_results.items()}
have_worked_ia_results = dict(sorted(have_worked_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])
have_worked_ia_results = pd.DataFrame(list(have_worked_ia_results.items()), columns=['IA', 'Porcentagem'])
have_worked_ia_results.to_sql('have_worked_ia', engine, if_exists='replace', index=False)

# Top 5 IAs que mais buscam trabalhar
want_to_work_ia_results = {}
for i in want_to_work_ia.columns:
    soma = want_to_work_ia[i].sum()
    want_to_work_ia_results[i] = soma

total_want = sum(want_to_work_ia_results.values())
want_to_work_ia_results = {chave: round((valor / total_want) * 100, 1) for chave, valor in want_to_work_ia_results.items()}
want_to_work_ia_results = dict(sorted(want_to_work_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])
want_to_work_ia_results = pd.DataFrame(list(want_to_work_ia_results.items()), columns=['IA', 'Porcentagem'])
want_to_work_ia_results.to_sql('want_to_work_ia', engine, if_exists='replace', index=False)

# Top 5 IAs mais admiradas
admired_ia_results = {}
for i in admired_ia.columns:
    soma = admired_ia[i].sum()
    admired_ia_results[i] = soma

total_admired = sum(admired_ia_results.values())
admired_ia_results = {chave: round((valor / total_admired) * 100, 1) for chave, valor in admired_ia_results.items()}
admired_ia_results = dict(sorted(admired_ia_results.items(), key=lambda x: x[1], reverse=True)[:5])
admired_ia_results = pd.DataFrame(list(admired_ia_results.items()), columns=['IA', 'Porcentagem'])
admired_ia_results.to_sql('admired_ia', engine, if_exists='replace', index=False)

resultado_faixa_etaria = survey_data.groupby('Age')[['ChatGPT', 'GitHub Copilot', 'Google Gemini', 'Bing AI', 'Visual Studio Intellicode']].sum().reset_index()
resultado_long = resultado_faixa_etaria.melt(id_vars='Age', var_name='IA', value_name='Quantidade')
resultado_long.to_sql('resultado_faixa_etaria', engine, if_exists='replace', index=False)

resultado_paises = survey_data['Country'].value_counts().head(10).reset_index()
resultado_paises.columns = ['Países', 'Usuários'] 
resultado_paises['Países'] = resultado_paises['Países'].replace({
    'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom'
})
resultado_paises.to_sql('resultado_paises', engine, if_exists='replace', index=False)

# Calculando o total por linguagem
have_worked_language_results = {}
for i in have_worked_language.columns:
    soma = have_worked_language[i].sum()
    have_worked_language_results[i] = soma
    
total_worked = sum(have_worked_language_results.values())
have_worked_language_results = dict(sorted(have_worked_language_results.items(), key=lambda x: x[1], reverse=True)[:10])
percentages = [round(soma / total_worked * 100, 2) for soma in have_worked_language_results.values()]
df_have_worked_language = pd.DataFrame({
    'Linguagem': list(have_worked_language_results.keys()),
    'Porcentagem': percentages
})
df_have_worked_language.to_sql('have_worked_language', engine, if_exists='replace', index=False)


print("Dados enviados com sucesso!")
