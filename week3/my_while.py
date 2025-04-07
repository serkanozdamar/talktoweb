i = 0
"""
INFINETE LOOP (sonsuz döngü)
koşul şart-condition ; doğru olduğu müddetçe bu kod çalışacak
"""
while i < 5:
    print(i)
    i += 1

print(i)


my_list = ["apple", "banana", "cherry"]

for i in range(len(my_list)):
    print(my_list[i])