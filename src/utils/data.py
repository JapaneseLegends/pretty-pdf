from typing import Any
import json

def open_json(path: str) -> dict[str, Any] | list[Any]:
    with open(path, 'r') as file:
        return json.load(file)
