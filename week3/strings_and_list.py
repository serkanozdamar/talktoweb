my_str = "talk to web"
my_list = [1, 2, "ali", "veli"]

print(type(my_str[0]))
print(my_str[0])
print(my_list[0])
print(len(my_list))

print(type(my_list))    # <class 'list'>
print(type(my_list[0])) # <class 'int'>
print(type(my_list[2])) # <class 'str'>


# str = "ali"
#
# print(str)
#
# veli = str(5)
#
# print(veli)
thislist = list()
print(thislist)  # boş list yarattı

# From Tuple-->To List
my_tuple = ("apple", "banana", "cherry")
thislist = list(my_tuple)
print(thislist)  # 3 elamanlı list
"""
[start_index:end_index:step]
my_list[0:5:1]
my_list[-6:-1]
my_list[-1:-6]
"""
my_list = [1, 2, "ali", "veli", 3, 5, 7, 9]
x = my_list[-2:-6:] # []
print(x)

y =  my_list[-1:-6:-1] # [9, 7, 5, 3, "veli"]
print(y)

my_bool = "apple" in my_list # False  boolean değer üretiyor
my_bool2 = "ali" in my_list # True
"""
Trace ediyoruz
tracing
"""
fruits = ["apple", "banana", "cherry", "kiwi", "mango", "apple", "mango"]
newlist = [] # list()

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

newlist2 = ["ali veli" + x for x in fruits if "a" in x]
print(newlist2)


for i in range(0,7):
    print(f"""i = {i}""")
    print(fruits[i])
