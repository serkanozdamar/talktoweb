thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon", "a", "c"]
# ['apple', 'blackcurrant', 'watermelon', 'a', 'c', 'orange', 'kiwi', 'mango']

print(thislist)

thislist = [6, "apple", "banana", "cherry", "orange", "kiwi", "mango"]

"""
thislis[0] = 6
thislist[0:1] =  ["apple"]
thislist[3:] = ["orange", "kiwi", "mango"]
"""
new_list = thislist[:1] + ["blackcurrant", "watermelon", "a", "c"] + thislist[3:]

print(new_list)