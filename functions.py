import os
import logging

def clean_str(text):
    x = text.strip("\n")
    x = x.strip("\r")
    x = x.strip("\t")
    x = x.strip("\v")
    return x

def update_times(files):
    with open("last_edit_times.txt", "w+") as f:
        for file in files:
            f.write(str(os.path.getmtime(file)))
            f.write("\n")
    
def clean_set(s):
    s.discard("\n")
    x = set()
    for a in s:
        x.add(clean_str(a))
    return x

def file_changes(file, copy):
    with open(file, "r") as f:
        x = set(f)
    with open(copy, "r") as fcopy:
        y = set(fcopy)
    
    x = clean_set(x)
    y = clean_set(y)
    
    added = x.difference(y)
    removed = y.difference(x)
    
    return added, removed

def change_message(file, copy, date, name):
    added, removed = file_changes(file, copy)
    message = name + " " + date
    if added:
        message = message + " Elements added: {}".format(added)
    if removed:
        message = message + " Elements removed: {}".format(removed)
    return message

def log(messages):
    logging.basicConfig(level = logging.INFO)
    for m in messages:
        logging.info(m)
