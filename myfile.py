read_file = open("C:\\Users\\tekin\\projects\\my_example.txt", mode="r", encoding="utf-8")
"""
"/home/tekin/my_file.txt"
"""
my_content = read_file.read()
my_splits = my_content.split("Ertuğrul")
read_file.close()

with open("C:\\Users\\tekin\\projects\\my_example.txt", mode="w", encoding="utf-8") as write_file:
    print(write_file.write(" Tekin Ertuğrul".join(my_splits)))

import io
with io.open("C:\\Users\\tekin\\projects\\my_example.txt", mode="w", encoding="utf-8") as write_file:
    print(write_file.write(" Tekin Ertuğrul".join(my_splits)))

