# Projet Prédiction de Retard de Vol

## Description

Ce projet a pour but d'analyser et de prédire les retards de vol. Il utilise des données historiques pour entraîner un modèle d'apprentissage automatique, et une application web permet d'interagir avec ce modèle pour obtenir des prédictions.

## Fonctionnalités

- Prédiction des retards de vol via une application Streamlit.
- Exploration et Analyse de Données (EDA) sur les retards de vol.
- Nettoyage et prétraitement des données.
- Entraînement d'un modèle de prédiction des retards.

## Structure

```plaintext
flight-delay-prediction/
├── app/
│   └── streamlit_app.py
├── data/
│   ├── data_cleaned.parquet
├── docs/
│   └── presentation.pdf
├── models/
│   └── RFt_model.joblib
├── notebooks/
│   ├── eda.ipynb
│   ├── model_training.ipynb
│   └── prediction.ipynb
├── .gitignore
├── requirements.txt
└── README.md
