from typing import Any
import json

def read_json(file_path: str) -> Any:
    with open(file_path, "r+", encoding="utf-8") as file:
        data = json.load(file)

    return data

def write_json(file_path: str, data: Any) -> None:
    with open(file_path, "w+", encoding="utf-8") as file:
        data = json.dump(data, file)
