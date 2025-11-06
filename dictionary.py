import requests

def define(word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    try:
        resp = requests.get(api_url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            entry = data[0]
            meanings = entry.get("meanings", [])
            if meanings:
                m = meanings[0]
                pos = m.get("partOfSpeech", "unknown")
                defs = m.get("definitions", [])
                if defs:
                    definition = defs[0].get("definition", "")
                    print(f"Alexa: {word.capitalize()} ({pos}): {definition}")
                    return
        print(f"Alexa: Sorry, I couldn’t find a definition for '{word}'.")
    except Exception as e:
        print(f"Alexa: Error retrieving definition — {e}")