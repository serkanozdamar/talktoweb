list1 = ["Irmak", "Gizem", "Ece"]

list2 = ["Python", "C", "C++"]

"""
Kartezyan Product

n * n --> O(n^2)
"""
for x in list1:
    for y in list2:
        print(x, y)


# list3 = list1 + list2
#
# for x in list3:
#     print(x)

assert len(list1) == len(list2)
for i in range(len(list1)):
    print(list1[i], list2[i])
"""
n--> O(n)
"""