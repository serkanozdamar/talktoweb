"""
(0,1,2,3,4)

range --> aralık üretir
range(başlanggıç,bitiş,step)


"""
# print(range(5,3))
# for i in range(7, 150, 7):
#     print(i)

thislist = ["apple", "banana", "cherry"]
print(range(len(thislist)))
# for i in range(len(thislist)):
#   print(thislist[i])

my_list = ["3.14", "150.5", "5", 1, 2]

for i in range(len(my_list)):
    my_list[i] = float(my_list[i])

print(my_list)