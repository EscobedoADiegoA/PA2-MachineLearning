import streamlit as st
import joblib
import numpy as np

model = joblib.load('modelos/steam_model.pkl')
encoder = joblib.load('modelos/genre_encoder.pkl')

st.title("Predicción de Popularidad de videojuegos")

genre = st.text_input("Género")
price = st.number_input ("Precio", min_value= 0.0)
recommendations = st.number_input("Recomendaciones", min_value=0)


if st.button("Predecir"):

    try:
        genre_encoded = encoder.transform([genre])[0]
        data = np.array([[genre_encoded,price, recommendations]])
        prediction = model.predict(data)

        if prediction[0] == 1:
            st.success ("El juego probablemente sea popular")
        else:
            st.error ("El juego probablemente no sea popular")
    except:
        st.warning("Ese género no existe en el dataset")