import  streamlit as st
import pandas as pd
st.title ("Une application Web simplifiée simple")
nom = st.text_input("Entrez votre nom", '')
st.write(f"Bonjour {nom}!")
x = st.slider("Sélectionnez un entier x", 0, 10, 1)
y = st.slider("Sélectionnez un entier y", 0, 10, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
st.write(df )