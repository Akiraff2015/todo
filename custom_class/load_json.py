import json

def open_file(file, key, val):
    with open(file) as json_data:
        data = json.load(json_data)
        return data[key][val]