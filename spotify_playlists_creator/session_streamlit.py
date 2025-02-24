import os

from dotenv import load_dotenv
import requests

BASE_URL = "https://accounts.spotify.com"


load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CALLBACK_URI = os.environ.get("CALLBACK_URI")


class Session:
    def __init__(self, token):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def search_song(self, song_title, artist):
        query = f"track:{song_title} artist:{artist}"
        url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
        
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        
        data = response.json()
        if data["tracks"]["items"]:
            track = data["tracks"]["items"][0]
            return track["id"]

        return None

    def get_user_profile(self):
        url = "https://api.spotify.com/v1/me"
        response = requests.get(url, headers=self.headers)

        return response.json()
    
    def get_user_id(self):
        url = "https://api.spotify.com/v1/me"

        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        user_profile = response.json()
        user_id = user_profile["id"]

        return user_id

    def create_playlist(self, playlist_name: str, playlist_description: str=""):
        user_id = self.get_user_id()
        playlist_data = {
            "name": playlist_name,
            "description": playlist_description,
            "public": False
        }
        url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

        response = requests.post(url, headers=self.headers, json=playlist_data)
        response.raise_for_status()
        playlist = response.json()

        playlist_id = playlist["id"]
        print(f"Playlist creada: {playlist['external_urls']['spotify']}")

        return playlist_id, playlist['external_urls']['spotify']

    def add_track_ids_to_playlist(self, track_ids: list, playlist_id: str):
            body = {
                "uris": [f"spotify:track:{track_id}" for track_id in track_ids]
            }
            url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

            response = requests.post(url, headers=self.headers, json=body)
            response.raise_for_status()

            print(f"Songs added to playlist {playlist_id}")
