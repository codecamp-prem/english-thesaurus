import json
from difflib import get_close_matches

data = json.load(open("data.json"), strict=False)


def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, N for No: " % get_close_matches(w, data.keys())[0])
        if yn.lower() == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn.lower() == "n":
            return "Word doesn't Exist. Please check the word"
        else:
            return "We didn't understand your entry."
    else:
        return "Word doesn't Exist. Please check the word"


word = input("Enter Word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
