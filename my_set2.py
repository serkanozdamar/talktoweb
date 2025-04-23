A = {1, 2, 3}
B = {1, 2, 3, 4, 5, 6}

# AUB = {1, 2, 3, 4, 5, 6}
# A.join(B)
# A & B = {1, 2, 3}

# AUB = B
# B
# A
# yı
# kapsar, A
# B'nin alt kümüseidr

print(A.issubset(B))
print(B.issuperset(A))
print(B.issuperset(B))
"""
A'nın alt kümeleri = {}, {1},{2}, {3}, {1,2},{1,3},{2,3}, {2,1,3}
b ise alt küme = 2^n = 8
"""
print(id(A), id(B))
C = A.copy()
print(id(A), id(B), id(C))
print(C)

print(A == C)
print(A is C)