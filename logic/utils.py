import os
import json

def get_files_of_type(folder_path:str, file_extension:str):
        extension_length = len(file_extension)
        files_in_folder = os.listdir(folder_path)
        files_of_type = [f for f in files_in_folder if f[-(extension_length):] == file_extension.lower()]
        return files_of_type

def add_value_to_json(json_filepath:str, value_name:str, value):
        with open(json_filepath, "r", encoding="utf8") as json_file:
                json_dict = json.load(json_file)
                json_dict[value_name] = value
        with open(json_filepath, "w", encoding="utf8") as json_file:
                json.dump(json_dict, json_file, ensure_ascii=False)