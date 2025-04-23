set1 = {1,2,3}
# set2 = {"ali", "veli", "deli"}
#
# print(id(set1), id(set2))
# set1.update(set2)
# print(id(set1), id(set2))
#
# print(set1)
#
# a = 5
#
# a = "ayşe"
thisset = {"apple", "banana", "cherry"}
try:
    thisset.remove("orange")
except KeyError:
    print("Hata aldım")
print(id(thisset))

"""
int a[10] = {1,2,3,4,5,6,7,8,9,0};
for(int i=0;i<10;i++){
    a[i]
}
for VARIABLE in ITERABLE:
    ...
    
for VARIABLE in range():
   ...
"""
ali = 4
def my_func():
    # global ali
    ali = "Merhaba"
    z = 1
    for item in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        z *= item
        print(item)
my_func()
print(ali)
