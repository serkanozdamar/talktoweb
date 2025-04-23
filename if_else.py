"""
if CONDITION:
    ...
elif CONDITION2:
   ...
elif CONDITION3:
    ...
else:
    ...

Emeklinin yaşına göre 60 ve daha fazla ise->30bin;55ise 25 bin diğer durumlarda 20 bin alacak

"""
yas = int(input("Lüften yaşınızı giriniz: "))
ilk_basamak_maas = 30000
ikinci_basamak_maas = 25000
son_basamak_basamak_maas = 20000

if yas >= 60:
    print(f"""Maaşınız = {ilk_basamak_maas}""")
elif yas >= 55:
    print(f"""Maaşınız = {ikinci_basamak_maas}""")
else:
    print(f"""Maaşınız = {son_basamak_basamak_maas}""")

