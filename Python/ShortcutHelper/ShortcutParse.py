import os
import json
import pprint
import jellyfish

dirname = os.path.dirname(__file__)

shortcut_file = dirname + "\\fman.json"
print(shortcut_file)

with open(shortcut_file, "r") as f:
    data = json.load(f)

pprint.pprint(data)

for binding in data["fman"]:
    print(binding["function"])
    print(binding["keybinding"])
