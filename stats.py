def num_words(t):
    words = t.split()
    return len(words)

def num_characters(c):
    characters = c.lower()

    characters_dict = {}

    for character in characters:
        characters_dict.setdefault(character, 0)
        characters_dict[character] += 1

    return characters_dict

def convert_to_list(characters_dict):
    result = []

    for k, v in characters_dict.items():
        r = {"char": k, "num": v}
        result.append(r)

    return result

def sort_on(items):
    return items["num"]
