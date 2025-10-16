import wikipedia

def search(query):
    found = False
    for auto in (False, True):
        try:
            print(wikipedia.summary(query, sentences=2, auto_suggest=auto))
            found = True
            break
        except:
            continue
    if not found: print(f"Sorry, I couldn't find information on {query}.")