import os
from shutil import copy
from functions import update_times, clean_str

with open("list_of_files.txt", "r") as f:
    list_files = f.readlines()

files = []
for f in list_files:
    files.append(clean_str(f))

os.makedirs("file_versions", exist_ok = True)
for f in files:
    copy(f, "file_versions")

update_times(files)
