import json
def load(file: str, default_return):
    """Load a json file content, returns default_return if file is not found"""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        if type(default_return) == dict or type(default_return) == list:
            return default_return.copy()
        else:
            return default_return
    
def save(file: str, thing_to_dump):
    """Overwrite a json file with thing_to_dump"""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(thing_to_dump, f)

"""Usefull ?"""