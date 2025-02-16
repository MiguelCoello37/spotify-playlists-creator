import requests

from spotify_playlists_creator.create_playlist_with_input_songs import create_playlist_with_input_songs


def main():
    input_file_path = "data/old_but_gold.txt"
    playlist_name = "Old But GOld"
    playlist_description = "Es mi vida, es ahora o nunca, porque no voy a vivir para siempre, sólo quiero vivir mientras siga vivo. ¡Nací libre! Libre como un río enfurecido, fuerte como el viento que choca con mi rostro persiguiendo sueños y corriendo contra el padre tiempo."
    create_playlist_with_input_songs(input_file_path, playlist_name, playlist_description)


if __name__=="__main__":
    main()
