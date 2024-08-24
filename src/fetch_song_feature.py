import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import numpy as np
from config.config import config
from sklearn.preprocessing import MinMaxScaler
import joblib

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= config.CLIENT_ID, client_secret=config.CLIENT_SECRET))

def fetch_song_features(song_name):
    results = sp.search(q=song_name, limit=1)
    if not results['tracks']['items']:
        print(f"'{song_name}' not found on Spotify.")
        return None

    track = results['tracks']['items'][0]
    track_id = track['id']
    track_features = sp.audio_features(track_id)[0]

    song_features = {
        'Track Name': track['name'],
        'Artists': ', '.join([artist['name'] for artist in track['artists']]),
        'Album Name': track['album']['name'],
        'Release Date': track['album']['release_date'],
        'Popularity': track['popularity'],
        'Features': [
            track_features['danceability'],
            track_features['energy'],
            track_features['key'],
            track_features['loudness'],
            track_features['mode'],
            track_features['speechiness'],
            track_features['acousticness'],
            track_features['instrumentalness'],
            track_features['liveness'],
            track_features['valence'],
            track_features['tempo']
        ]
    }
     # Preprocess the features
    scaler = joblib.load('scaler.pkl')
    features_array = np.array(song_features['Features']).reshape(1, -1)
    scaled_features = scaler.transform(features_array)
    song_features['Features'] = scaled_features[0].tolist()

    return song_features