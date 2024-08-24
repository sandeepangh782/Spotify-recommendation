# src/recommendation.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
from src.fetch_song_feature import fetch_song_features

def calculate_weighted_popularity(release_date):
    release_date = datetime.strptime(release_date, '%Y-%m-%d')
    time_span = datetime.now() - release_date
    weight = 1 / (time_span.days + 1)
    return weight

def content_based_recommendations(input_song_name, music_df, music_features_scaled, num_recommendations=5):
    if input_song_name not in music_df['Track Name'].values:
        song_features = fetch_song_features(input_song_name)
        if not song_features:
            return
        input_song_features = song_features['Features']
    else:
        input_song_index = music_df[music_df['Track Name'] == input_song_name].index[0]
        input_song_features = music_features_scaled[input_song_index]

    similarity_scores = cosine_similarity([input_song_features], music_features_scaled)
    similar_song_indices = similarity_scores.argsort()[0][::-1][1:num_recommendations + 1]
    return music_df.iloc[similar_song_indices][['Track Name', 'Artists', 'Album Name', 'Release Date', 'Popularity']]

def hybrid_recommendations(input_song_name, music_df, music_features_scaled, num_recommendations=5, alpha=0.5):
    if input_song_name not in music_df['Track Name'].values:
        song_features = fetch_song_features(input_song_name)
        if not song_features:
            return
        input_song_data = {
            'Track Name': [song_features['Track Name']],
            'Artists': [song_features['Artists']],
            'Album Name': [song_features['Album Name']],
            'Release Date': [song_features['Release Date']],
            'Popularity': [song_features['Popularity']]
        }
        input_song_df = pd.DataFrame(input_song_data)
        weighted_popularity_score = song_features['Popularity'] * calculate_weighted_popularity(song_features['Release Date'])
        input_song_df['Popularity'] = weighted_popularity_score
    else:
        input_song_df = music_df[music_df['Track Name'] == input_song_name]
        weighted_popularity_score = input_song_df['Popularity'].values[0] * calculate_weighted_popularity(input_song_df['Release Date'].values[0])
        input_song_df['Popularity'] = weighted_popularity_score

    content_based_rec = content_based_recommendations(input_song_name, music_df, music_features_scaled, num_recommendations)
    hybrid_recommendations = pd.concat([content_based_rec, input_song_df], ignore_index=True)
    hybrid_recommendations = hybrid_recommendations.sort_values(by='Popularity', ascending=False)
    return hybrid_recommendations[hybrid_recommendations['Track Name'] != input_song_name]