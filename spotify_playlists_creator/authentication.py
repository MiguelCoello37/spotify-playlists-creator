import os

from dotenv import load_dotenv
import requests

BASE_URL = "https://accounts.spotify.com"
CALLBACK_URI = "http://localhost:8888/callback"

load_dotenv()
CLIENT_ID = os.environ.get("CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


def get_authorization_url():
    endpoint= "/authorize"
    url = BASE_URL + endpoint

    client_id = CLIENT_ID
    callback_uri = CALLBACK_URI
    params = {
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": callback_uri,
    }
    
    request = requests.request("get", url, params=params)

    return request.url


def get_token(code):
    endpoint = "/api/token"
    url = BASE_URL + endpoint

    client_id = CLIENT_ID
    client_secret = CLIENT_SECRET
    callback_uri = CALLBACK_URI
    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": callback_uri,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=body)

    response.raise_for_status()

    return response.json()["access_token"]
