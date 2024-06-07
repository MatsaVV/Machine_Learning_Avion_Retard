import streamlit as st
import pandas as pd
import joblib

def load_model(path):
    try:
        model = joblib.load(path)
        st.success("Modèle chargé avec succès.")
        return model
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle: {e}")
        return None

def user_input_features(data):
    inputs = {}
    for column in data.columns:
        if column != 'ARR_DELAY_NEW':
            if data[column].dtype == 'object':
                inputs[column] = st.selectbox(f'{column}', options=data[column].unique())
            else:
                inputs[column] = st.number_input(f'{column}', value=float(data[column].mean()))
    return pd.DataFrame([inputs])

def display_predictions(model, data, preprocessor):
    if data is not None and model is not None:
        try:
            data_preprocessed = preprocessor.transform(data)
            prediction = model.predict(data_preprocessed)
            result = 'Retard' if prediction[0] == 1 else 'Pas de retard'
            st.success(f'La prédiction est : {result}')
        except Exception as e:
            st.error(f"Erreur lors de la prédiction: {e}")

def main():
    st.title('Prédiction de retard de vol')

    model = load_model('RF_model.joblib')  # Remplacez par le chemin vers votre modèle

    if model:
        # Charger les données pour obtenir les colonnes
        try:
            data = pd.read_parquet('data_cleaned.parquet')  # Remplacez par le chemin vers votre fichier de données
            st.success("Données chargées avec succès.")
        except Exception as e:
            st.error(f"Erreur lors du chargement des données: {e}")
            return

        input_df = user_input_features(data)

        if st.button('Prédire'):
            display_predictions(model, input_df, model.named_steps['preprocessor'])

if __name__ == "__main__":
    main()
