import os

from dotenv import load_dotenv
import requests

BASE_URL = "https://accounts.spotify.com"
CALLBACK_URI = "http://localhost:8888/callback"


class Session():
    def __init__(self):
        load_dotenv()
        self.client_id = os.environ.get("CLIENT_ID")
        self.client_secret = os.environ.get("CLIENT_SECRET")
        self.callback_uri = CALLBACK_URI

        authorization_url = self._get_authorization_url()
        print(authorization_url)
        code = input("Introduce code: ")
        self.token = self._get_token(code)

    def _get_authorization_url(self):
        endpoint= "/authorize"
        url = BASE_URL + endpoint

        params = {
            "client_id": self.client_id,
            "response_type": "code",
            "redirect_uri": self.callback_uri,
        }
        
        request = requests.request("get", url, params=params)

        return request.url


    def _get_token(self, code):
        endpoint = "/api/token"
        url = BASE_URL + endpoint

        body = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.callback_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }

        response = requests.post(url, data=body)

        response.raise_for_status()

        return response.json()["access_token"]

    def search_song(self, song_title, artist):
        query = f"track:{song_title} artist:{artist}"
        url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
        headers = {"Authorization": f"Bearer {self.token}"}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        data = response.json()
        if data["tracks"]["items"]:
            track = data["tracks"]["items"][0]
            return track["id"], track["name"], track["artists"][0]["name"], track["external_urls"]["spotify"]
        return None
