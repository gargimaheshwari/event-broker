import os

with open("list_of_files.txt", "w+") as f:
    f.write(os.path.abspath("test.txt"))
