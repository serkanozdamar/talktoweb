import math


# def my_func():
#     return 1 / 0
#
# my_func()

print("Hello boys and girls")

def find_hippo(a, b):
    return math.sqrt(a * a + b * b)

print(find_hippo(3, 4))
print(find_hippo(5, 12))
print(find_hippo(24, 25))


# find_hippo(1,2,3)
# x = zip(("ali", "veli"), (1,2,3))
# print(tuple(x))

def my_zip(first_item, second_item, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print(len(args), args)
    print(len(kwargs), kwargs)

    if len(args) == 1:
        print(args[0])

    for item in args:
        print(item)


    print(kwargs["a"])

my_zip(1,2,3,4,5,6, ali=5, mehmet=7, aa=34, b="mehmet")
# my_zip(1,2,3,4,5)
# my_zip(1,2,3,4)

def my_function(a, *kids):
    if len(kids) >= 3:
        print("The youngest child is " + kids[2])
    elif len(kids) >= 2:
        print("The youngest child is " + kids[1])

my_function("Emil", "Tobias", "Linus")

'''
The two arguments for this function are the files:
    - currentMem: File containing list of current members
    - exMem: File containing list of old members

    This function should remove all rows from currentMem containing 'no' 
    in the 'Active' column and appends them to exMem.
    '''


def cleanFiles(currentMem, exMem):
    active_members = []
    with open(currentMem, "r+") as read_write_file:
        with open(exMem, "a+") as append_file:
            row_line = 0
            for line in read_write_file.readlines():
                if row_line == 0:
                    row_line += 1
                    continue
                row_line += 1
                if line.split()[2] == "no":
                    append_file.write(line)
                else:
                    active_members.append(line)
        read_write_file.seek(0, 0)
        read_write_file.writelines(active_members)


# The code below is to help you view the files.
# Do not modify this code for this exercise.
memReg = 'members.txt'
exReg = 'inactive.txt'
cleanFiles(memReg, exReg)

headers = "Membership No  Date Joined  Active  \n"
with open(memReg, 'r') as readFile:
    print("Active Members: \n\n")
    print(readFile.read())

with open(exReg, 'r') as readFile:
    print("Inactive Members: \n\n")
    print(readFile.read())