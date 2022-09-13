
# The main code is in the app_base.ipynb file, this code here was just for practice purposes.


import os, json
import pandas as pd
import numpy as np
import glob
#pd.set_option('display.max_columns', None)























def get_files(filepath):
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,"*json"))
        for f in files:
            all_files.append(os.path.abspath(f))
    return all_files


device_files =get_files("dsm-api")


# Loading all the json data & then appending into a list named "json_list"
json_list = []

for json_id in device_files:
    with open(json_id) as doc:
        exp = json.load(doc)
        json_list.append(exp)


# Creating a dataframe of all the json files data.

df1 = pd.DataFrame(json_list[0])


print(df1.columns)

















'''
temp = pd.DataFrame()

path_to_json = '/HIPER Final Task/dsm-api/*'

json_pattern = os.path.join(path_to_json, "*.json")
file_list = glob.glob(json_pattern)

dfs = []

for file in file_list:
    data = pd.read_json(file, lines=True)
    dfs.append(data)

print(dfs[0])
'''

# temp = pd.concat(dfs, ignore_index=True)

# with open('2022-08-22.json') as f:
#     data = json.load(f)

# for id in data:
#     for ts in id:
#         print(id['ts'])

# print(data[0]['ts'])




