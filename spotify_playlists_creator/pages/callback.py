import time

import streamlit as st

from authentication import get_token
from create_playlist_with_input_songs import create_playlist_with_input_songs
from session_streamlit import Session


st.title("Spotify Playlists Creator")

if "access_token" not in st.session_state:
    query_params = st.query_params
    code = query_params.get("code")
    st.session_state.access_token = get_token(code)

with st.form("user_form"):
    playlist_name = st.text_input("Playlist title")
    playlist_description = st.text_area("Playlist description")
    songs_info = st.text_area("List of songs titles and artists")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        st.success("Form submitted successfully! Creating playlist...")
        session = Session(st.session_state.access_token)
        playlist_url = create_playlist_with_input_songs(session, playlist_name, playlist_description, songs_info.split("\n"))

        st.write(f"Ready! You can access to your playlist here: {playlist_url}")
