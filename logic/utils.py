import os

def get_files_of_type(folder_path:str, file_extension:str):
        extension_length = len(file_extension)
        files_in_folder = os.listdir(folder_path)
        files_of_type = [f for f in files_in_folder if f[-(extension_length):] == file_extension.lower()]
        return files_of_type
