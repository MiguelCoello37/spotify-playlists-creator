from get_songs_ids import get_songs_ids_from_text_file, get_songs_ids
from session_streamlit import Session


def create_playlist_with_input_songs(session: Session, playlist_name: str, playlist_description: str, playlist_songs: str):
    songs_ids = get_songs_ids(playlist_songs, session)
    playlist_id, playlist_url = session.create_playlist(playlist_name, playlist_description)
    slices_size = 100
    for i in range(len(songs_ids) // slices_size + 1):
        lower_threshold = i*slices_size
        upper_threshold = (i+1)*slices_size
        songs_ids_slice = songs_ids[lower_threshold:upper_threshold]
        upper_threshold = upper_threshold if upper_threshold <= len(songs_ids) else len(songs_ids)

        session.add_track_ids_to_playlist(songs_ids_slice, playlist_id)

    return playlist_url


def create_playlist_with_input_songs_from_text_file(text_file_path: str, playlist_name: str, playlist_description: str):
    session = Session()
    songs_ids = get_songs_ids_from_text_file(text_file_path, session)
    playlist_id = session.create_playlist(playlist_name, playlist_description)
    slices_size = 100
    for i in range(len(songs_ids) // slices_size + 1):
        lower_threshold = i*slices_size
        upper_threshold = (i+1)*slices_size
        songs_ids_slice = songs_ids[lower_threshold:upper_threshold]
        upper_threshold = upper_threshold if upper_threshold <= len(songs_ids) else len(songs_ids)

        session.add_track_ids_to_playlist(songs_ids_slice, playlist_id)
