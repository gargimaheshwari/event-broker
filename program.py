import os
from shutil import copy
from datetime import date
from functions import clean_str, update_times, change_message, log

with open("list_of_files.txt", "r") as f:
    list_files = f.readlines()

files = []
for f in list_files:
    files.append(clean_str(f))

with open("last_edit_times.txt", "r") as f:
    times = f.readlines()

changed = False
messages = []

for i, f in enumerate(files):
    f = clean_str(f)
    new_time = os.path.getmtime(f)
    old_time = float(times[i])
    name = os.path.basename(f)
    if new_time > old_time:
        changed = True
        name = os.path.basename(f)
        fcopy = os.path.join("file_versions", name)
        d = date.fromtimestamp(new_time).strftime("%d.%m.%Y")
        messages.append(change_message(f, fcopy, d, name))
        copy(f, "file_versions")

if changed:
    log(messages)
    update_times(files)
