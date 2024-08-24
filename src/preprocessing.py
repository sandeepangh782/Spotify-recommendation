# src/preprocessing.py
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

def preprocess_data(df):
    scaler = MinMaxScaler()
    features = df[['Danceability', 'Energy', 'Key', 'Loudness', 'Mode', 'Speechiness', 'Acousticness',
                   'Instrumentalness', 'Liveness', 'Valence', 'Tempo']].values
    scaled_features = scaler.fit_transform(features)
    scaler_path = "scaler.pkl"
    joblib.dump(scaler, scaler_path)
    # print(pd.DataFrame(scaled_features))
    return scaled_features
