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
