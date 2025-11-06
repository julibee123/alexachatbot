from PyMovieDb import IMDB
import json

def recommend(genre):
    try:
        data = json.loads(IMDB().popular_movies(genre, start_id=1, sort_by=None))
        top_10_titles = [(movie['name'], movie['year']) for movie in data['results'][:10]]
        print("Alexa: You might like these movies!")
        for i, (name, year) in enumerate(top_10_titles,1):
            print(f"{i}. {name} ({year})")
    except:
        print("Alexa: Sorry, I didn't find anything for that genre.")