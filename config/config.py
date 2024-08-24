
import os
from dotenv import load_dotenv


load_dotenv()

class Config:
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    PLAYLIST_ID = os.getenv('PLAYLIST_ID')

config = Config()
