class Ogrenci:
    isim = []
    soyisim = "GUL"
    yas = 38
    bolum = "Cevre Muhendisligi"


# sınıfların özelliklerine erişmek
print(Ogrenci.isim)
print(Ogrenci.soyisim)
print(Ogrenci.yas)
print(Ogrenci.bolum)

# sınıfların özelliklerini değiştirme
Ogrenci.soyisim = "Cicek"
Ogrenci.yas = 40
Ogrenci.school = "METU"

# sınıfların Örneklendirilmesi
ertugrul = Ogrenci()
irmak = Ogrenci()
emirhan = Ogrenci()
gizem = Ogrenci()

print(ertugrul.isim)
print(irmak.isim)
print(emirhan.isim)
print(gizem.isim)

ertugrul.isim.append("Ertuğrul")

print(ertugrul.isim)
print(irmak.isim)
print(emirhan.isim)
print(gizem.isim)


class Ogrenci2:
    yas = 38


    def __init__(self):
        self.soyisim = []
        self.bolum = []


ertugrul = Ogrenci2()
irmak = Ogrenci2()
emirhan = Ogrenci2()
gizem = Ogrenci2()

print(ertugrul.soyisim)
print(irmak.soyisim)
print(emirhan.soyisim)
print(gizem.soyisim)

ertugrul.soyisim.append("GUL")

print(irmak.soyisim)
print(emirhan.soyisim)
print(ertugrul.soyisim)
print(gizem.soyisim)

irmak.soyisim.append("SABUNCU")
emirhan.soyisim.append("OYMAK")
gizem.soyisim.append("KALENDER")

print(irmak.soyisim)
print(emirhan.soyisim)
print(ertugrul.soyisim)
print(gizem.soyisim)

print(irmak.yas)
print(emirhan.yas)
print(ertugrul.yas)
print(gizem.yas)
