import os
import pathlib

def get_data(data_location):
    data = ""
    
    for file in os.listdir(data_location):
        file_path = os.path.join(data_location,file)
        with open(file_path,"r",encoding="utf-8") as f:
            file_data = f.read()
            # print(file_data)
            data = data + file_data + '\n'
    
    return data

data_loc = "doc"

data = get_data(data_loc)
