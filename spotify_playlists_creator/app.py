import streamlit as st

from authentication import get_authorization_url
from session_streamlit import Session


st.title("Spotify Playlists Creator")
create_playlist_button = st.button("Create playlist on Spotify")

if create_playlist_button:
    authorization_url = get_authorization_url()
    st.markdown(f'<meta http-equiv="refresh" content="0;url={authorization_url}">', unsafe_allow_html=True)
