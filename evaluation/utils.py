import json

def read_json_file(filepath):
    """Reads a JSON file from the given filepath."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return None

def read_string_from_file(filepath):
    """Reads a string from a text file."""
    try:
        with open(filepath, 'r') as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return None
