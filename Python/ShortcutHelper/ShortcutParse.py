import os
import json
import pprint
from thefuzz import fuzz
from thefuzz import process
from collections import defaultdict

dirname = os.path.dirname(__file__)


def get_filepaths():
    paths = {}
    for shortcut_file in os.listdir(dirname + "\\json\\"):
        if shortcut_file.endswith(".json"):
            shortcut_filepath = dirname + "\\json\\" + shortcut_file
            # Dict from app name of the filename ie. fman from fman.json
            paths[str(shortcut_file)[0:-5]] = shortcut_filepath

    return paths


def load_json(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        # pprint.pprint(data)

    return data


def score_function_list(app, data, query):

    app_functions = []
    for item in data:

        score = fuzz.partial_token_sort_ratio(query.lower(), item["function"].lower())

        app_functions.append(
            {
                "app": app,
                "function": item["function"],
                "keybinding": item["keybinding"],
                "score": score,
            }
        )

    return app_functions


def get_top_5(function_list):
    # Sort the list of scores and use them as keys for the function dictionary

    sorted_func_scores = sorted(function_list, key=lambda x: x["score"], reverse=True)
    return sorted_func_scores


def main(query):
    paths = get_filepaths()
    master_function_list = []
    # Sorting isn't necessary since the score from Fuzz can be used for FlowLauncher as well.

    for key, value in paths.items():
        json_output = load_json(value)
        # pprint.pprint(json_output)
        master_function_list += score_function_list(key, json_output, query)

    # pprint.pprint(master_function_list)
    return master_function_list


if __name__ == "__main__":

    main("palette")

# pprint.pprint(master_function_list)
# sorted_funcs = get_top_5(master_function_list)
# pprint.pprint(sorted_funcs[:10])
