import streamlit as st
import joblib
import pandas as pd

# Charger le modèle
model = joblib.load('rf_model.joblib')

# Fonction pour faire une prédiction
def predict_delay(day_of_month, month, year, origin_city_name, dest_city_name, unique_carrier):
    input_data = pd.DataFrame({
        'DAY_OF_MONTH': [day_of_month],
        'MONTH': [month],
        'YEAR': [year],
        'ORIGIN_CITY_NAME': [origin_city_name],
        'DEST_CITY_NAME': [dest_city_name],
        'UNIQUE_CARRIER': [unique_carrier]
    })
    prediction = model.predict(input_data)
    return prediction[0]

# Interface utilisateur Streamlit
st.title('Prédiction de Retard de Vol')

day_of_month = st.number_input('Jour du Mois', min_value=1, max_value=31, step=1)
month = st.number_input('Mois', min_value=1, max_value=12, step=1)
year = st.number_input('Année', min_value=2000, max_value=2025, step=1)
origin_city_name = st.text_input('Nom de la Ville de Départ')
dest_city_name = st.text_input('Nom de la Ville d’Arrivée')
unique_carrier = st.text_input('Code du Transporteur Unique')

if st.button('Prédire'):
    result = predict_delay(day_of_month, month, year, origin_city_name, dest_city_name, unique_carrier)
    st.write(f'Prédiction de Retard: {"Oui" if result == 1 else "Non"}')
