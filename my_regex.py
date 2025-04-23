import re

# Örnek metin
text = "Bu bir test 192.168.1.1 ve 10.0.0.1 ile 300.300.300.300 gibi IP'leri içerir."

# IP adresi regex'i
ip_regex = r"(\d{1,3}\.){3}\d{1,3}"

# Tüm eşleşmeleri bul
prog  = re.compile(ip_regex)

# Sonuçları yazdır
for w in text.split():
    m = prog.match(w)
    if m:
        print(m.string)