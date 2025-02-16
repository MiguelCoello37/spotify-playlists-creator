import warnings

from spotify_playlists_creator.session import Session


def get_songs_ids_from_text_file(text_file_path: str, session: Session) -> list:
    with open(text_file_path, "r") as f:
        songs_info = list(f)

    songs_ids = []
    number_of_songs = len(songs_info)
    for i, song_info in enumerate(songs_info):
        print(f"Searching for {song_info} ({i+1}/{number_of_songs})")
        song_title, artist = song_info.split(" - ", maxsplit=1)
        track_id = session.search_song(song_title, artist)
        if not track_id:
            warnings.warn(f"WARNING!!! {song_title}, by {artist}, not found")
            continue

        songs_ids.append(track_id)

    return songs_ids
