import re
import pywhatkit
import lyrics_genius as genius
import pyjokes
import random
import sympy as sp
import fixed_wikipedia as wiki
import dictionary
import movie_recommend as movie

def extract(line, phrase):
    return line.replace(phrase, "").strip()

# fixes alexa syntax
def fix_alexa(command):
    sp_index = command.find(' ')
    for char in command[:sp_index]:
        if char not in ['a','l','e','x','a']:
            command = command.replace(char, '')
    return command

def run_alexa():
    command = input("You: ").lower().strip()
    # command = re.sub(r'[^a-z0-9\s+\-*/^().!]', '', command)
    command = re.sub(r'\s+', ' ', command).strip()
    command = fix_alexa(command)

    if not command.startswith("alexa"):
        print("Sorry, I don't understand that. You have to type 'Alexa'.")
        return

# alexa play music on yt
    if 'alexa play' in command:
        song = extract(command, 'alexa play')
        print("Alexa: Playing", song)
        pywhatkit.playonyt(song)

# alexa genius feature
    elif 'alexa what song goes like' in command:
        song_lyrics = extract(command, 'alexa what song goes like')
        genius.find(song_lyrics)

# alexa joke
    elif 'alexa tell a joke' in command:
        j = random.randint(1,4)
        if j > 1:
            print("Alexa:", pyjokes.get_joke())
        else:
            print("Alexa: Joke")

# Math
    elif 'solve' in command:
        problem = extract(command, 'alexa solve')

        if "^" in problem:
            problem = problem.replace("^", "**")

        try:
            result = sp.sympify(problem).evalf()
            if result == int(result):
                result = int(result)
            else:
                result = round(float(result), 4)

            print("Alexa:", result)

        except:
            print("Alexa: Sorry, Alexa can't solve complex things. Ask ChatGPT.")

# Person Search Up
    elif 'alexa who is' in command or 'alexa what is' in command:
        if 'who is' in command:
            query = extract(command, 'alexa who is')
        else:
            query = extract(command, 'alexa what is')
        wiki.search(query)

# Definition
    elif 'alexa define' in command or 'alexa what does' in command:
        if 'define' in command:
            word = extract(command, 'alexa define')
        else:
            word = extract(command, 'alexa what does')
        word = word.replace('mean', '').strip()
        dictionary.define(word)

# Movie Recommend
    elif 'alexa recommend a movie' in command or 'alexa suggest a movie' in command:
        print("Alexa: What genre do you like?")
        genre = input("You: ").lower().strip()
        movie.recommend(genre)

# Exit
    elif 'alexa shutdown' in command or 'goodbye' in command:
        print("Alexa: Goodbye!")
        exit()
    else:
        print("Alexa: I'm sorry, I do not understand.")

if __name__ == "__main__":
    print("Alexa: Hi! I am your chatbot assistant. Type commands starting with 'Alexa'")
    while True:
        run_alexa()