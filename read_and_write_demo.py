## Reading from and writing to files
# We learned the basics of using context managers (with block) to read data
# from a file, make sure to have the data.txt file in the same
# directory as this file, otherwise you have to provide the full
# path to the file

# 'with' context manager is good so you dont have to use f.close() later
filename = 'data.txt'
with open(filename) as f:
    for line in f:
        print(line.strip())

# We then looked at how to append a new line to the file
# the second argument for 'open' is usually 'r' for read. 
# It can be 'a+' to append, or 'w' to overwrite a file
record_to_add = "jane,doe:c,ruby,javascript"
with open(filename, "a+") as to_write:
    to_write.write(record_to_add+"\n")
