import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

if "data" not in st.session_state:
    df = pd.read_excel("mental_health_analysis.xlsx", index_col="User_ID")
    df = df.sort_values(by="Wearable_Stress_Score", ascending=False)
    st.session_state["data"] = df

st.set_page_config(page_title="CP1", layout="wide")


st.logo("GB-monogram.png")
st.sidebar.markdown("Gustavo Bonani Favero Marcos. (LinkedIn: https://www.linkedin.com/in/gustavo-bonani-favero-marcos-2b6165292/)")

pages = st.sidebar.selectbox("Escolha a página:", [
    "Introdução",
    "Formação e Experiência",
    "Skills"
])


st.image("GB-monogram.png", width=150)

if pages == "Introdução":
    st.title("Introdução pessoal")

    st.write("Meu nome é Gustavo Bonani Favero Marcos. Tenho 19 anos e atualmente estou cursando o segundo ano de Engenharia de Software na FIAP.")

    st.write("Meu objetivo atualmente é conseguir um estágio para que eu ganhe experiência no mercado de trabalho. Futuramente, espero conseguir um emprego na área de design ou modelagem tridimensional.")

if pages == "Formação e Experiência":
    st.title("Formação Acadêmica")
    
    st.write("Ensino Fundamental: Colégio Emilie de Villeneuve (Completo)")
    st.write("Ensino Médio: Colégio Etapa (Completo)")
    st.write("Ensino Superior: Engenharia de Software - FIAP (Cursando)")
    st.write("Cursos Extra-curriculares: Formação Social e Sustentabilidade; Design Thinking; Gestão e Infraestrutura de TI; Estruturas de Computadores; Modelagem 3D (Cursando); Edição de Video (Cursando)")
    st.subheader("Design Thinking - Process")
    st.image("Design Thinking.png")
    st.subheader("Computer Structures")
    st.image("Estruturas.png")
    st.subheader("Sustentability and Social Formation")
    st.image("Formação Social.png")
    st.subheader("IT Infrastructure Management")
    st.image("Gestão.png")

if pages == "Skills":
    st.title("Habilidades e Ferramentas")
    
    st.write("Proeficiente em: Modelagem 3D (Maya/Blender); Programação em Python(VSCode/Pycharm)")
    st.write("Competente em: Design Front-End(HTML/CSS/JS/React)")
    
    st.title("Outras Competências")
    st.write("- Fluente em inglês; ")
    st.write("- Trabalho em equipe; ")
    st.write("- Proatividade em aprender; ")
    st.write("- Liderança; ")
    st.write("- Resolução de problemas; ")
    st.write("- Pensamento Crítico; ")
    st.write("- Lógica. ")