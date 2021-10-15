from json import load
file_name = open("characters.json")
content = load(file_name)

characters = content["characters"]
for character in characters:
    print(character["characterName"])
