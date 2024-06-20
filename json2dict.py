import json
import os

def load_json(file_name):
    file_path = f"./Answer-Key/{file_name}.json"
    print(file_path)
    if os.path.exists(file_path):
        with open(file_path,"r",encoding="utf-8") as json_file:
            return json.load(json_file)
    else:
        print("File does not exist!!")



