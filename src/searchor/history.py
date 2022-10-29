import os
import json
import os.path
from datetime import datetime

DATA_PATH = os.path.join(os.getenv("HOME"), ".searchor-history.json")
tmp = {"searches": []}


def update(engine, query, url):
    search_data = {
        "url": url,
        "engine": engine,
        "query": query,
        "time": str(datetime.today().strftime("%I:%M %p")),
    }

    if not os.path.exists(DATA_PATH):  # check if data file does not exist
        with open(DATA_PATH, "w") as history_file:
            json.dump(tmp, history_file)  # create file if it does not exist
    with open(DATA_PATH, "+r") as history_file:
        history_data = json.load(history_file)
        history_data["searches"].append(search_data)
        history_file.seek(0)
        json.dump(history_data, history_file, indent=4)


def clear():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "w") as history_file:
            json.dump(tmp, history_file)


def view():
    with open(DATA_PATH, "+r") as history_file:
        history_data = json.load(history_file)
        for search in history_data["searches"]:
            print(f"{search['time']}: {search['url']}")
