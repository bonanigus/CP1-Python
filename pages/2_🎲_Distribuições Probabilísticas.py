import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from plotnine import *

# Configuração da página
st.set_page_config(page_title="CP1", layout="wide")
df = st.session_state["data"]

# Adicionando o logo
st.logo("GB-monogram.png")

# Adicionando o logo
st.image("GB-monogram.png", width=150)

# Criando as sub-abas (pages)
pages = st.sidebar.selectbox("Escolha a Página:", [
    "Apresentação",
    "Pergunta 1",
    "Pergunta 2",
    "Pergunta 3",
    "Pergunta 4",
    "Pergunta 5"
])

dados = df.sample(n=1000, random_state = 50)

if pages == "Apresentação":
    st.title('Apresentação')
    st.write('Para essa análise de dados, escolhi uma base de dados chamada "Análise de Saúde Mental em Adolescentes". Os dados coletados envolvem idade e gênero dos sujeitos (as quais são divididas proporcionalmente); Tempo de tela de redes sociais por dia; Tempo de exercício por dia; Horas de sono; Tempo de tela total por dia; Estresse auto reportado (1- Pouco estresse / 5 - Muito estresse); Estresse medido por dispositivos (alcance de 0 a 1); Sistema de suporte e Desempenho Acadêmico.')
    st.write("Esses dados exibem traços de vivência de 5000 participantes, entre as idades de 13 e 19 anos, com o intuito de relacionar esses traços para observação da saúde mental adolescente, detecção de distúrbios ou problemas mentais e cuidado preventivo.")
    st.write("Com os fatores apresentados, surgem as dúvidas:")
    st.subheader('1. Qual o fator que mais influencia episódios de estresse?')
    st.write('- Nesse caso, iremos usar as medidas de  estresse medido por dispositivos maior que 0,7')
    st.subheader('2. Qual idade experiencia mais estresse?')
    st.write('- Faremos duas medidas, uma baseada no estresse auto reportado, para sabermos qual idade acha que passa mais estresse, e outra baseada no estresse medido, para vermos qual idade realmente passa mais estresse.')
    st.subheader('3. Há correlação entre estresse experienciado e desempenho acadêmico?')
    st.write('- Nesse tópico, iremos procurar por uma proporção inversa, quanto maior o índice de estresse, pior o desempenho')
    st.subheader('4. Qual gênero experiencia maior estresse?')
    st.write('- Checaremos qual gênero entre masculino e feminino é mais estressado')
    st.subheader('5. Mais horas de exercício por dia resultam em menores índices de estresse?')
    st.write('- Novamente, estaremos procurando uma proporção inversa: um número maior de horas de exercício para um índice menor de estresse')
    st.write('Nessa análise, visamos responder essas perguntas. Abaixo também se encontra a tabela que usaremos como base de dados.')

    tipos='Todos'
    tipos = np.append(tipos,df["Support_System"].unique())
    tipo = st.sidebar.selectbox("Sistema de Suporte", tipos)
    st.sidebar.markdown("Gustavo Bonani Favero Marcos. (LinkedIn: https://www.linkedin.com/in/gustavo-bonani-favero-marcos-2b6165292/)")

    if tipo == 'Todos':
        df_filtered = df
    else:
        df_filtered = df[(df["Support_System"]==tipo)]


    st.dataframe(df_filtered,
             column_config={
                 "Age": st.column_config.ProgressColumn(
                     "Age", format="%f", min_value=0, max_value=int(df_filtered["Age"].max()))
                 })
    st.write("Nessa tabela, temos as seguintes colunas:")
    st.write("- User ID - código único de cada participante (Qualitativa Nominal)")
    st.write("- Idade - de 13 à 19 anos (Quantitativa Discreta)")
    st.write("- Gênero - Masculino e Feminino (Qualitativa Nominal)")
    st.write("- Tempo de Redes Sociais - Tempo de tela de Redes Sociais por dia de 0h à 10h (Quantitativa Contínua)")
    st.write("- Horas de Exercício - Horas de Exercício Diárias, de 0h à 3h (Quantitativa Contínua)")
    st.write("- Horas de Sono - Tempo de sono diário de 4h à 10h (Quantitativa Contínua)")
    st.write("- Tempo de tela - Tempo total de tela por dia, de 2h à 12h (Quantitativa Contínua)")
    st.write("- Estresse Auto Reportado - Quantidade de estresse reportada pelos sujeitos, em uma escala de 1 a 5 (Quantitativa Discreta)")
    st.write("- Estresse Medido por Dispositivos - Quantidade de estresse medida por dispositivos utilizáveis, em uma escala de 0 a 1 (Quantitativa Contínua)")
    st.write("- Sistema de Apoio (Qualitativa Ordinal)")
    st.write("- Desempenho Acadêmico (Qualitativa Ordinal)")

if pages == "Pergunta 1":
    st.header('Qual o fator que mais influencia episódios de estresse?')
    st.subheader('Aqui, checaremos entre todos os fatores qual resulta em um maior índice de estresse geral.')
    st.write('Para isso, precisaremos fazer uma série de distribuições usando estresse medido por dispositivos como eixo X, enquanto utilizamos as outras medidas como eixo Y. Os gráficos exibidos são:')

    st.write('- Estresse medido por dispositivos x Tempo de uso de Redes Sociais')
    fig = px.histogram(dados, x ='Wearable_Stress_Score', y = 'Social_Media_Hours', histfunc = 'avg')
    fig.update_layout(bargap = 0.2)
    st.plotly_chart(fig)

    st.write('- Estresse medido por dispositivos x Tempo de Exercício diáro')
    fig = px.histogram(dados, x ='Wearable_Stress_Score', y = 'Exercise_Hours', histfunc = 'avg')
    fig.update_layout(bargap = 0.2)
    st.plotly_chart(fig)
    st.write('- Estresse medido por dispositivos x Horas de Sono')
    fig = px.histogram(dados, x ='Wearable_Stress_Score', y = 'Sleep_Hours', histfunc = 'avg')
    fig.update_layout(bargap = 0.2)
    st.plotly_chart(fig)
    st.write('- Estresse medido por dispositivos x Tempo total de tela diário')
    fig = px.histogram(dados, x ='Wearable_Stress_Score', y = 'Screen_Time_Hours', histfunc = 'avg')
    fig.update_layout(bargap = 0.2)
    st.plotly_chart(fig)

    st.subheader("Vale notar que utilizamos uma amostra de 1000 participantes e a média dos fatores no eixo Y.")
    st.write("Para definir qual fator influencia mais nos índices de estresse, levaremos em conta o gráfico que tende mais ao fim do eixo X. Baseando-se nesses parâmetros, chegamos à conclusão que o fator que mais influencia episódios de estresse é o tempo de tela de redes sociais")


if pages == "Pergunta 2":
    st.header("Qual idade experiencia mais estresse?")
    st.subheader('Nesse tópico, iremos quantificar e separar as idades dos participantes e definir qual idade passa maior estresse')
    st.write('Para isso, precisamos primeiro ordenar as idades e separá-las.')
    fig = px.bar(df.sort_values('Age'), x ='Age', y = 'Gender', color = "Age")
    st.plotly_chart(fig)
    st.write("Agora, vamos descobrir qual idade acha que passa mais estresse, utilizando a medida de estresse auto reportado.")
    fig = px.histogram(df.sort_values('Survey_Stress_Score'), histfunc="avg", x ='Age', y = 'Survey_Stress_Score', color = "Age", color_discrete_sequence=px.colors.sequential.Viridis)
    st.plotly_chart(fig)
    st.write("Baseando-se no que podemos ver, a idade que reportou mais episódios de estresse foi 18 anos.")
    st.subheader("Agora, descobriremos qual a idade que realmente passa mais estresse.")
    fig = px.histogram(df.sort_values('Age'), x ='Age', y = 'Wearable_Stress_Score', histfunc="avg", color = "Age")
    st.plotly_chart(fig)
    st.write("Vemos que as idades de 15 e 16 ficam muito próximas, mas 16 anos acaba experienciando maior estresse entre todas as idades.")
if pages == "Pergunta 3":
    st.header('Há correlação entre estresse experienciado e desempenho acadêmico?')
    st.subheader('Aqui a resposta que estamos procurando é: Maior estresse resulta em pior desempenho?')
    fig = px.histogram(df.sort_values('Survey_Stress_Score'), x ='Academic_Performance', y = 'Survey_Stress_Score', color = "Academic_Performance")
    st.plotly_chart(fig)
    st.write("Baseando-se nas informações exibidas, as pessoas que dizem experienciar mais estresse acabam tendo um desempenho acadêmico pior.")
    st.subheader("Agora, veremos as estatísticas reais:")
    fig = px.histogram(df.sort_values('Wearable_Stress_Score'), x ='Academic_Performance', y = 'Wearable_Stress_Score', color = "Academic_Performance")
    st.plotly_chart(fig)
    st.write("Conforme o mostrado, as pessoas que passam mais estresse tendem a ter um desempenho acadêmico ruim, mesmo que o desempenho bom tenha quase o mesmo nível de estresse.")
if pages == "Pergunta 4":
    st.header("Qual gênero experiencia mais estresse?")
    st.subheader("Queremos saber qual gênero é mais calmo e qual gênero é mais nervoso.")
    st.write("Para isso, precisamos fazer dois gráficos, um para o estresse auto reportado e um para o estresse medido por dispositivos")
    fig = px.histogram(df.sort_values('Survey_Stress_Score'), x ='Gender', y = 'Survey_Stress_Score', color = "Gender", color_discrete_sequence=['#ff0000', '#0000ff'])
    st.plotly_chart(fig)
    st.write("Vemos que o gênero feminino reporta ter mais episódios de estresse.")
    fig = px.histogram(df.sort_values('Wearable_Stress_Score'), x ='Gender', y = 'Wearable_Stress_Score', color = "Gender", color_discrete_sequence=['#0000ff', '#ff0000'])
    st.plotly_chart(fig)
    st.write("E com esse gráfico comprovamos que de fato o gênero femimino experiencia maior estresse quando comparado com o gênero masculino.")


if pages == "Pergunta 5":
    st.header('Mais horas de exercício por dia resultam em menores índices de estresse?')
    st.subheader("Aqui estamos procurando uma influência positiva, será que fazer mais exercícios resulta em menos estresse?")
    fig = px.histogram(df.sort_values('Survey_Stress_Score'), x ='Exercise_Hours', y = 'Survey_Stress_Score')
    fig.update_layout(bargap = 0.2)
    st.plotly_chart(fig)
    fig = px.histogram(df.sort_values('Wearable_Stress_Score'), x ='Exercise_Hours', y = 'Wearable_Stress_Score')
    fig.update_layout(bargap = 0.2)    
    st.plotly_chart(fig)
    st.write("Baseando-se no apresentado, não há uma relação direta entre tempo de exercício e redução do estresse, visto que nos extremos os índices de estresse são mais baixos do que no meio de ambos os gráficos")