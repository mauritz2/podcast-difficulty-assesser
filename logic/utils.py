import os

def get_files_of_type(folder_path:str, file_extension:str):
        files_in_folder = os.listdir(folder_path)
        files_of_type = [f for f in files_in_folder if f[-3:] == file_extension.lower()]
        return files_of_type
