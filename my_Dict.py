"""
hash
hashable; string, int, float, Boolean, None, Tuple
Non-HASHABLE: dict, list ve set

KEY : VALUE
"""

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    5: "ali",
    True: False,
    False: True,
    None: True,
    90.6: {
        "ali": 54,
        "veli": 6
    },
    (1,2): [1,2,3,4,],
    # [1,2,3]: "veli"
    # {1,2,3}: 5
}
# O(1)
print(thisdict["brand"])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020
    }
# print(thisdict)
#
# print(type(thisdict.keys()))
# print(thisdict.values())
# print(list(thisdict.keys()))
# print(list(thisdict.values()))

print(type(thisdict.items()))


for k,v in thisdict.items():
    print(k, v)


