import requests

from spotify_playlists_creator.authentication import get_authorization_url, get_token

SONG_TITLE = "Bohemian Rhapsody"
ARTIST = "Queen"


def search_song(token, song_title, artist):
    query = f"track:{song_title} artist:{artist}"
    url = f"https://api.spotify.com/v1/search?q={query}&type=track&limit=1"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    data = response.json()
    if data["tracks"]["items"]:
        track = data["tracks"]["items"][0]
        return track["id"], track["name"], track["artists"][0]["name"], track["external_urls"]["spotify"]
    return None

authorize_url = get_authorization_url()
print(authorize_url)
code = input("Introduce el code: ")
token = get_token(code)
print(token)

result = search_song(token, SONG_TITLE, ARTIST)

if result:
    track_id, nombre, ARTIST, url = result
    print(f"🎵 Canción encontrada: {nombre} - {ARTIST}")
    print(f"🔗 URL en Spotify: {url}")
else:
    print("❌ No se encontró la canción en Spotify.")
