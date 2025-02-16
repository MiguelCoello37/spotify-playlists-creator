import requests

from spotify_playlists_creator.get_songs_ids import get_songs_ids_from_text_file
from spotify_playlists_creator.session import Session


def main():
    # input_file_path = "data/old_but_gold.txt"
    # get_songs_ids_from_text_file(input_file_path)

    session = Session()
    # print(session.get_user_profile())
    session.create_playlist("Yeepaa!", "La he creado con Python primo!")


if __name__=="__main__":
    main()
