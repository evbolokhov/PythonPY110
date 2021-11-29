import json


def to_json_string(python_object) -> str:
    json_string = json.dumps(python_object)  # метод dumps сериализует объект в JSON строку
    # print(type(json_string))
    return json_string


def from_json_string(json_string: str):
    python_object = json.loads(json_string)  # метод loads десериализует из JSON строки в python объект
    # print(type(python_object))
    return python_object


if __name__ == "__main__":
    dict_json = {
        1: 1,
        "2": 5,
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
    }

    print("Исходный объект:", dict_json)

    json_str = to_json_string(dict_json)
    print("JSON строка:", json_str)

    python_obj = from_json_string(json_str)
    print("Объект из JSON строки:", python_obj)

    print(dict_json == python_obj)
