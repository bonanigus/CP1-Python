import streamlit as st
import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import poisson, binom
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dados",
    page_icon="🏃🏼",
    layout="wide"
)

df = st.session_state["data"]

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

st.header("Distribuição de Poisson")
st.subheader("Utilizaremos da distribuição de poisson utilizando os dados de estresse auto reportado. para ver qual nível de estresse é mais provável que um próximo adolescente reporte.")

media_estresse = df_filtered["Survey_Stress_Score"].mean()
st.write(f"Média do Estresse Autorreportado: {media_estresse:.2f}")

x = np.arange(0, 6)
y = poisson.pmf(x, media_estresse)

fig, ax = plt.subplots()
ax.bar(x, y, color='purple', alpha=0.6)
ax.set_xlabel("Nível de estresse autorreportado")
ax.set_ylabel("Probabilidade")
ax.set_title(f"Distribuição de Poisson (λ = {media_estresse:.2f})")

st.pyplot(fig)

st.header("Distribuição Binomial")
st.subheader("Modelagem do tempo de tela diário, considerando sucesso quando o tempo de tela é maior que 7 horas.")

sample_size = st.slider("Escolha o tamanho da amostra", min_value = 10, max_value = 2500, value = 100)

amostra = df_filtered['Screen_Time_Hours'].sample(n=sample_size, random_state = 42)

n = len(amostra)
sucessos = np.sum(amostra > 7)

p = sucessos / n if n > 0 else 0

st.write(f"Número de amostras selecionadas: {n}")
st.write(f"Proporção de tempo de tela > 7 horas: {p:.2f}")

k = np.arange(0, n + 1)
prob = binom.pmf(k, n, p)

fig, ax = plt.subplots()
ax.bar(k, prob, color='blue', alpha=0.6, label='Distribuição Binomial')

ax.plot(k, prob, color='red', linestyle='--', linewidth=1.5, label='Linha da Distribuição')


ax.set_xlabel("Número de pessoas com tempo de tela excessivo")
ax.set_ylabel("Probabilidade")
ax.set_title(f"Distribuição Binomial (n = {n}, p = {p:.2f})")
ax.legend()

st.pyplot(fig)
st.write("Esse gráfico exibe a probabilidade de um jovem da quantidade amostral ter o tempo de tela maior que 7 horas por dia.")