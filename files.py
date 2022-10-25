"""
Creating, reading, writing, opening files
"""

"""
'r' - Read Only
'r+' Read and write
'w' write only
'w+' write and read
'a' append only
'a+' append and read
"""

with open(filename, "r+") as f:
    data = f.read()
    f.seek(0)
    f.write(output)
    f.truncate()

#No line endings
with open(filename) as f:
    mylist = f.read().splitlines() 