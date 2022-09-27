import json


class Utils:
    VALID_DATE = "pls"
    JSON_FILE = "./data/gtd.json"

    def __init__(self):
        pass

    @classmethod
    def raw_data(cls):
        with open(cls.JSON_FILE, 'r', encoding="UTF-8") as f:
            data = json.load(f)
        print(data)
        return data

    @classmethod
    def write(cls, data):
        with open(cls.JSON_FILE, 'w', encoding="UTF-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    @classmethod
    def data_map(cls, date):
        mapping = {
            'y': 'year',
            'd': 'day'
        }

        msg = mapping.get(date)

        return msg if msg is not None else cls.VALID_DATE
