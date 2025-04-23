from hw import my_str

myList = my_str.split()

mySet = set(myList) # dictionarynin setlri
my_Dict = {}
for item in mySet: # burada da n kere işlem yapıoyuorsun
    my_Dict[item] = myList.count(item) # her seferde n kere işlem yapıyorsun

# n * n