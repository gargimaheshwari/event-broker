import os
from shutil import copy
from functions import update_times, clean_str

f = open("list_of_files.txt", "r")
list_files = f.readlines()
f.close()

files = []
for file in list_files:
    files.append(clean_str(file))

os.makedirs("file_versions", exist_ok = True)
for file in files:
    copy(file, "file_versions")

update_times(files)
