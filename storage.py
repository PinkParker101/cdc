import json
import os
from config import DATA_FILE, DEFAULT_RESERVED_PLATFORMS
from time_utils import time_to_minutes


def save_data(trains, reserved_platforms):
    data = {
        "trains": trains,
        "reserved_platforms": reserved_platforms
    }
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_data():
    if not os.path.exists(DATA_FILE):
        return [], DEFAULT_RESERVED_PLATFORMS

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        trains = data.get("trains", [])
        # Convert older HH:MM strings or saved minute values consistently.
        for train in trains:
            train["arrival"] = time_to_minutes(train["arrival"])
            train["departure"] = time_to_minutes(train["departure"])

        reserved = int(data.get("reserved_platforms", DEFAULT_RESERVED_PLATFORMS))
        print("Previous train records loaded successfully.")
        return trains, reserved

    except (json.JSONDecodeError, OSError, ValueError, TypeError, KeyError):
        print("Could not load saved data. Starting with empty records.")
        return [], DEFAULT_RESERVED_PLATFORMS
