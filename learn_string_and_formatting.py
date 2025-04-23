# print("hello world")

"""
Variables (Değişkenler)
çoklu satar

String  = iki tırnak işareti içinme yazılan herşey
''
""
""""""
"""
a = 9
b = 11
toplam = a + b

print(toplam)

first_string = 'Muhammed Nur'
second_string = "ece"
third_string = """meltem"""

str1 = """merhaba ben Cuma tekin TOPu. Size Python'da string öğretmek istiyoru. Bunun için "w3scholl.com" sitesinde tutorial üzerinde gideceğiz."""
print(str1)
#
# str1 = 'merhaba ben Cuma tekin TOPu. Size Python'da string öğretmek istiyoru. Bunun için "w3scholl.com" sitesinde tutorial üzerinde gideceğiz.'
# print(str1)

print("Toplam = ", toplam)

print("{0} {1} {2}".format("Toplam", "=", toplam))
print("{0} {1} {2}".format("Toplam", "=", a + b))
print(f"""{a} + {b} = {toplam}""")
