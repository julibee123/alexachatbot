from lyricsgenius import Genius

GENIUS_TOKEN = "EyEVtjzy-N_ToCPy7nJZs90sVA9nkaHBuGy_NSEv6Vpqn-Rb9uNbZxuKkW9O8jUm"
genius = Genius(GENIUS_TOKEN)

def find(query):
    try:
        data = genius.search_songs(query, per_page=1)
        matches = data["hits"]

        if matches:
            result = matches[0]["result"]
            title = result["title"]
            artist = result["primary_artist"]["name"]
            print(f"The song is '{title}' by {artist}.")
        else:
            print("Could not find song from lyrics.")
    except Exception as e:
        print("Error searching:", e)