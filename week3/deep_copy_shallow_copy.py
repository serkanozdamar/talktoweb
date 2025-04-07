my_list = ["ali", "veli", 1, 2]

my_list2 = my_list # shallow copy
my_list3 = [x for x in my_list] # my_list.copy()

if my_list == my_list2:
    print("my_list == my_list2")

if my_list3 == my_list2:
    print("my_list == my_list2")

if my_list3 is my_list2:
    print("my_list == my_list2")

print(f"""ID of my_list: {id(my_list)}""")
print(f"""ID of my_list2: {id(my_list2)}""")
print(f"""ID of my_list3: {id(my_list3)}""")
my_list[2] *= 10
my_list2[3] *= 9

print(my_list)
print(my_list2)

if my_list is my_list2:
    print("The same list")

if my_list is my_list3:
    print("The same list")
else:
    print("NOT The same list")