import json
import os

"""
Loads the JSON for the required data dump  
"""
def collect_data_lists(json_to_be_loaded):
    list_dir = os.listdir()  # List current directory
    direct = check_directory(list_dir)  # Check current directory
    if direct[0] == 'data' or not 'None':
        os.chdir('data')
    with open(json_to_be_loaded) as load_data:
        data = json.load(load_data)
    return data


"""
Checks the directory - if not 'data', changes to 'data'  
"""
def check_directory(dir_list):
    for file in dir_list:
        if file.endswith('py'):
            dir_list.remove(file)
            return dir_list

    return 'None'
