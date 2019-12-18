import os
import logging

def clean_str(text):
    x = text.strip("\n")
    x = x.strip("\r")
    x = x.strip("\t")
    x = x.strip("\v")
    return x

def update_times(files):
    f = open("last_edit_times.txt", "w+")
    for file in files:
        f.write(str(os.path.getmtime(file)))
        f.write("\n")
    f.close()
    
def clean_set(s):
    s.discard("\n")
    x = set()
    for a in s:
        x.add(clean_str(a))
    return x

def file_changes(file, copy):
    file = open(file, "r")
    copy = open(copy, "r")
    
    x = set(file)
    y = set(copy)
    
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
