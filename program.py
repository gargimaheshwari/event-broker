import os
from shutil import copy
from datetime import date
from functions import clean_str, update_times, change_message, log

f = open("list_of_files.txt", "r")
list_files = f.readlines()
f.close()

files = []
for file in list_files:
    files.append(clean_str(file))

f = open("last_edit_times.txt", "r")
times = f.readlines()
f.close()

changed = False
messages = []

for i, file in enumerate(files):
    file = clean_str(file)
    new_time = os.path.getmtime(file)
    old_time = float(times[i])
    name = os.path.basename(file)
    if new_time > old_time:
        changed = True
        name = os.path.basename(file)
        fcopy = os.path.join("file_versions", name)
        d = date.fromtimestamp(new_time).strftime("%d.%m.%Y")
        messages.append(change_message(file, fcopy, d, name))
        copy(file, "file_versions")

if changed:
    log(messages)
    update_times(files)
