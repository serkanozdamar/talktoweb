thislist = ["apple", "banana", "cherry"]
print(thislist)
print(id(thislist))

thislist[0] = "orange"
print(thislist)
print(id(thislist))


print(len(thislist))

for item in thislist:
    print(item)

a = [1, 2, 3]
b = []
c = list()

print(len(a))
print(len(b))
print(len(c))

if c:
    print("Not empty")
else:
    print("Empty")

c.append(1)
c.append("ali")
c.append(3.14)
print(c)

new_list = a + b + c

print(new_list[-1])
print(new_list[:4])