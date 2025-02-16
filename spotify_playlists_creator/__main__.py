import requests

from spotify_playlists_creator.session import Session


def main():
    session = Session()
    token = session.token

    song_title = "Cuando Zarpa el Amor"
    artist = "Camela"
    result = session.search_song(song_title, artist)

    if result:
        track_id, nombre, ARTIST, url = result
        print(f"🎵 Canción encontrada: {nombre} - {ARTIST}")
        print(f"🔗 URL en Spotify: {url}")
    else:
        print("❌ No se encontró la canción en Spotify.")


if __name__=="__main__":
    main()
