from ..utils.console import print_error, print_info
from json import load, JSONDecodeError

def load_json(self, filepath: str):
    print_info(f"Loading JSON data from '{self.jsonpath}'...")

    try:
        with open(filepath, 'r') as file:
            return load(file)

    except FileNotFoundError:
        print_error(f"File '{filepath}' not found.")
        exit(1)
    
    except JSONDecodeError:
        print_error(f"File '{filepath}' is not a valid JSON file.")
        exit(1)

def load_env(self, env_path: str):
    raise NotImplementedError

def merge(*args: dict):
    return {**args}

