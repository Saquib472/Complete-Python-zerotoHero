# Write a pyhton prohram to rename a file to "renamed_by_python.txt"

import os

oldname = "sample2.txt"
newname = "renamed_bt_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, "w") as f:
    f.write(content)

os.remove(oldname)