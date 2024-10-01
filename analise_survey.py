"""
# Análise Survey Stack Overflow

## Contexto

Com o avanço significativo dos Modelos de Inteligência Artificial LLM e o surgimento de diversas ferramentas que os utilizam, a empresa V8.Tech está interessada em incorporar algumas dessas soluções no dia a dia de seus colaboradores.

Para tomar uma decisão mais assertiva sobre qual ferramenta adotar, foi solicitado que uma análise seja feita utilizando os registros de dados da pesquisa **Survey Stack Overflow 2024**, que em meio a tratativa de diversos assuntos relacionados a tecnologia, investigou o uso de IA entre profissionais de tecnologia e desenvolvimento, abordando questões como popularidade das ferramentas, confiabilidade e utilidade em tarefas mais complexas.

## Extração

Importando as bibliotecas necessárias
"""

import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('survey_results_public.csv')


"""Visualizando o DataFrame em detalhes"""

dados.head()

dados.columns

dados.size

dados.shape

"""O arquivo bruto contém um total de **7.459.818** dados, organizados em **65.437** linhas e **114** colunas, abrangendo assuntos como: Educação, Trabalho, Carreira, Linguagens, Frameworks, Softwares e Sistemas Operacionais mais utilizados, Comunidade Stack Overflow e Inteligência Artificial.

Diante da necessidade de uma análise mais precisa e direcionada, se torna importante filtrar as informações mais relevantes para o nosso contexto.

## Tratamento

Selecionando as colunas relevantes
"""

dados_tratados = dados[['ResponseId', 'MainBranch', 'Age', 'Employment',
                        'YearsCodePro', 'DevType', 'Country','AISearchDevHaveWorkedWith',
                        'AISearchDevWantToWorkWith', 'AISearchDevAdmired', 'AISelect', 'AISent',
                        'AIBen', 'AIAcc', 'AIComplex', 'AIThreat', 'ProfessionalQuestion', 'Industry', 'JobSat']]

"""
Visualizando os dados selecionados
"""

dados_tratados.head()

"""Removendo os dados nulos referentes a utilização de IA"""

dados_tratados = dados_tratados.dropna(subset=['AISearchDevHaveWorkedWith', 'AISearchDevWantToWorkWith', 'AISearchDevAdmired'])

"""Agrupando a sessão de respostas referentes a utilização de IA"""

AI_search = dados_tratados[['AISearchDevHaveWorkedWith', 'AISearchDevWantToWorkWith', 'AISearchDevAdmired']]

"""Fragmentando a coluna, possibilitando a análise isolada e o agrupamento de cada IA específica"""

have_worked_ia = AI_search['AISearchDevHaveWorkedWith'].str.get_dummies(';')
want_to_work_ia = AI_search['AISearchDevWantToWorkWith'].str.get_dummies(';')
admired_ia = AI_search['AISearchDevAdmired'].str.get_dummies(';')

"""Visualizando as colunas"""

have_worked_ia.head()

"""## Compactando o DataFrame

Unindo os dados tratados ao DataFrame de utilização de IAs
"""

dados = pd.concat([dados_tratados, have_worked_ia], axis=1)

dados.to_csv('survey_data.csv', index=False)
