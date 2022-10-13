from distutils.command.upload import upload
from operator import index
import streamlit as st
import pandas as pd

st.write("# Bienvenue sur l'app compta.")

upload_file = st.file_uploader("Envoyer votre fichier")

if upload_file:

    df = pd.read_csv(upload_file, sep=";", index_col=0)
    
    with st.expander("Voir vos données"):
    
        filter_salary = st.slider("Valeur minimum de salaire",
                                  int(df["salaire"].min()),
                                  int(df["salaire"].max()))
        
        st.dataframe(df[df["salaire"] >= filter_salary])
        
    col1, col2, col3 = st.columns(3)
    
    col1.metric("Salaire max", round(df["salaire"].max()), round(df["salaire"].max() - df["salaire"].median()))
    col2.metric("Salaire min", round(df["salaire"].min()), -round(df["salaire"].median() - df["salaire"].min()))
    col3.metric("Salaire moyen", round(df["salaire"].mean()), round(df["salaire"].mean() - df["salaire"].median()))
        
        