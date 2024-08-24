# Spotify Recommendation System

This project is a Spotify recommendation system that fetches song features from Spotify, preprocesses the data, and provides song recommendations based on a hybrid recommendation algorithm.

## Project Structure
 ```sh
spotify-recommendation/
│
├── config/
│   ├── config.py
├── src/
│   ├── __init__.py                 # Initialization file for the src module
│   ├── recommendation.py           # Functions for recommendation logic
│   ├── spotify_api.py              # Functions for interacting with the Spotify API
│   ├── preprocessing.py            # Functions for data preprocessing and normalization
│   ├── fetch_song_feature.py       # Fetches song features for input song if not present in the dataset.
|
├── .gitignore
├── requirements.txt                # List of required Python packages
├── README.md                       # Project overview and instructions
└── main.py   
 ```

## Setup

1. **Clone the repository:**

    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install the required packages:**

    pip install -r requirements.txt
    

3. **Create a [`.env`] file in the root directory with your Spotify API credentials:**

    ```env
    CLIENT_ID='your_client_id'
    CLIENT_SECRET='your_client_secret'
    PLAYLIST_ID='your_playlist_id'
    ```

## Usage

1. **Run the main script:**

    ```sh
    python main.py
    ```

2. **Output:**

    The script will print hybrid recommended songs for the specified input song.