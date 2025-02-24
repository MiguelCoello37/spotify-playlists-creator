import warnings

from session_streamlit import Session


def get_songs_ids(playlist_songs_info: str, session: Session):
    songs_ids = []
    number_of_songs = len(playlist_songs_info)
    for i, playlist_song_info in enumerate(playlist_songs_info):
        print(f"Searching for {playlist_song_info} ({i+1}/{number_of_songs})")
        song_title, artist = playlist_song_info.split(" - ", maxsplit=1)
        track_id = session.search_song(song_title, artist)
        if not track_id:
            warnings.warn(f"WARNING!!! {song_title}, by {artist}, not found")
            continue

        songs_ids.append(track_id)

    return songs_ids


def get_songs_ids_from_text_file(text_file_path: str, session: Session) -> list:
    with open(text_file_path, "r") as f:
        songs_info = list(f)

    return get_songs_ids(songs_info, session)
