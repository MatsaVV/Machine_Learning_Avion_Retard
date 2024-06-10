import streamlit as st
import joblib
import pandas as pd
import os
print("Répertoire de travail actuel :", os.getcwd())

model = joblib.load('model/model.joblib')


def predict_delay(day_of_month, day_of_week, crs_dep_time, dest_airport_id, crs_arr_time, origin_airport_id):
    input_data = pd.DataFrame({
        'DAY_OF_MONTH': [day_of_month],
        'DAY_OF_WEEK': [day_of_week],
        'CRS_DEP_TIME': [crs_dep_time],
        'DEST_AIRPORT_ID': [dest_airport_id],
        'CRS_ARR_TIME': [crs_arr_time],
        'ORIGIN_AIRPORT_ID': [origin_airport_id]
    })
    prediction = model.predict(input_data)
    return prediction[0]


st.title('Prédiction de Retard de Vol')

day_of_week = st.number_input('Jour de la Semaine : ex Lundi = 1', min_value=1, max_value=7, step=1)
day_of_month = st.number_input('Jour du Mois', min_value=1, max_value=31, step=1)
crs_dep_time = st.number_input('Heure de Départ vol', min_value=0, max_value=2359, step=1)
origin_airport_id = st.number_input('ID de l’Aéroport d’Origine', min_value=0, step=1)
crs_arr_time = st.number_input('Heure d’Arrivée vol', min_value=0, max_value=2359, step=1)
dest_airport_id = st.number_input('ID de l’Aéroport de Destination', min_value=0, step=1)

if st.button('Prédire'):
    result = predict_delay(day_of_month, day_of_week, crs_dep_time, dest_airport_id, crs_arr_time, origin_airport_id)
    st.write(f'Prédiction de Retard: {"Oui" if result == 1 else "Non"}')
