import os
import logging

def clean_str(text):
    """Remove all spaces from text"""
    x = text.strip("\n")
    x = x.strip("\r")
    x = x.strip("\t")
    x = x.strip("\v")
    return x

def update_times(files):
    """Update last_edit_times.txt"""
    with open("last_edit_times.txt", "w+") as f:
        for x in files:
            f.write(str(os.path.getmtime(x)))
            f.write("\n")
    
def clean_set(s):
    """Remove spaces from every element in set s using clear_str()"""
    s.discard("\n")
    x = set()
    for a in s:
        x.add(clean_str(a))
    return x

def file_changes(input_file, copy):
    """Compute the differences between input_file and copy"""
    with open(input_file, "r") as f:
        x = set(f)
    with open(copy, "r") as fcopy:
        y = set(fcopy)
    
    x = clean_set(x)
    y = clean_set(y)
    
    added = x.difference(y)
    removed = y.difference(x)
    
    return added, removed

def change_message(input_file, copy, date, name):
    """Create logging message for input_file"""
    added, removed = file_changes(input_file, copy)
    message = name + " " + date
    if added:
        message = message + " Elements added: {}".format(added)
    if removed:
        message = message + " Elements removed: {}".format(removed)
    return message

def log(messages):
    """Log message to console"""
    logging.basicConfig(level = logging.INFO)
    for m in messages:
        logging.info(m)
