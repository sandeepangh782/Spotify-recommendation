from config.config import config
from src.spotify_api import get_access_token, get_playlist_data
from src.preprocessing import preprocess_data
from src.recommendation import hybrid_recommendations
import pandas as pd

def main():
    access_token = get_access_token(config.CLIENT_ID, config.CLIENT_SECRET)
    playlist_data = get_playlist_data(config.PLAYLIST_ID, access_token)
    
    # Assuming you have a way to convert playlist_data to a DataFrame (not shown here)
    music_df = pd.DataFrame(playlist_data)  # Populate this DataFrame with actual data from playlist_data
    
    music_features_scaled = preprocess_data(music_df)
    input_song_name = "Barandaye Roddur"
    recommendations = hybrid_recommendations(input_song_name, music_df, music_features_scaled)
    
    print(f"Hybrid recommended songs for '{input_song_name}':")
    print(recommendations.to_string(index=False))

if __name__ == "__main__":
    main()
