import os

from dotenv import load_dotenv
import requests

BASE_URL = "https://accounts.spotify.com"


load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CALLBACK_URI = os.environ.get("CALLBACK_URI")

def get_authorization_url():
    endpoint= "/authorize"
    url = BASE_URL + endpoint

    params = {
        "scope": "playlist-modify-private",
        "show_dialog": False,
        "client_id": CLIENT_ID,
        "response_type": "code",
        "redirect_uri": CALLBACK_URI,
    }
    
    request = requests.request("get", url, params=params)

    return request.url


def get_token(code):
    endpoint = "/api/token"
    url = BASE_URL + endpoint

    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": CALLBACK_URI,
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }

    response = requests.post(url, data=body)

    response.raise_for_status()

    return response.json()["access_token"]
