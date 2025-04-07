# thistuple = ("apple", "banana", "cherry")
# y = "orange", "apple"
# # thistuple += y
# #
# # print(thistuple)
#
# print(type(y))
# print(y)

thistuple = ("apple", "banana", "cherry")
print(id(thistuple))
y = ("orange",)
thistuple += y

print(thistuple)
print(id(thistuple))