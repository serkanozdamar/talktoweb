# import re
# import numpy as np
# string = 'bat, lat, mat, bet, let, met, bit, lit, mit, bot, lot, mot'
# result = re.findall('b[ao]t', string)
# print(result)
#
#
# def l2_dist(a, b):
#     result = ((a - b) * (a - b)).sum()
#     result = result ** 0.5
#     return result
#
# a =  np.random.randint(0, 10, (20, 20))
# b =  np.random.randint(0, 10, (20, 20))
# print(l2_dist(a, b))
# print(l2_dist(a.T, b.T))
# print(l2_dist( np.reshape(a, (20*20)), np.reshape(b, (20*20))))
# print(l2_dist( np.reshape(a, (20*20)), np.reshape(b, (20*20, 1))))
# x = np.reshape(a, (20*20)), np.reshape(b, (20*20, 1))
# print(x)
#
#
# a1 = np.random.rand(4)
# a2 = np.random.rand(4, 1)
# a3 = np.array([[1, 2, 3, 4]])
# a4 = np.arange(1, 4, 1)
# a5 = np.linspace(1 ,4, 4)
#
# print(a1.shape)
# print(a1.shape == a2.shape)
# print(a1.shape == a5.shape)
# print(a4)
#
#
# old = np.array([[1, 1, 1], [1, 1, 1]])
# new = old
# new[0, :2] = 0
#
# print(old)
#
# r = np.arange(36).reshape((6, 6))
# print(r[2:4,2:4])
#
#
# import re
# s = 'ACBCAC'
#
# print(re.findall("^AC",s))
#
# import re
# s = 'ACAABAACAAAB'
# result = re.findall('A{1,2}', s)
# print(result)
# L = len(result)
# print(f"""'ACAABAACAAAB' = {L}""")
#
# my_text = """Office of Research Administration: (734) 647-6333 | 4325 North Quad
# Office of Budget and Financial Administration: (734) 647-8044 | 309 Maynard, Suite 205
# Health Informatics Program: (734) 763-2285 | 333 Maynard, Suite 500
# Office of the Dean: (734) 647-3576 | 4322 North Quad
# UMSI Engagement Center: (734) 763-1251 | 777 North University
# Faculty Adminstrative Support Staff: (734) 764-9376 | 4322 North Quad"""
#
# my_regex = "[(]\d{3}[)]\s\d{3}[-]\d{4}"
# result = re.findall(my_regex, my_text)
# print(result)
#
# my_text = 'I refer to https://google.com and I never refer http://www.baidu.com if I have to search anything'
# my_regex = "(?<=[https]:\/\/)([A-Za-z0-9.]*)"
# result = re.findall(my_regex, my_text)
# print(result)
#
# text=r'''Everyone has the following fundamental freedoms:
#     (a) freedom of conscience and religion;
#     (b) freedom of thought, belief, opinion and expression, including freedom of the press and other media of communication;
#     (c) freedom of peaceful assembly; and
#     (d) freedom of association.'''
#
# import re
# pattern = '\(.\)'
# print(len(re.findall(pattern,text)))

import pandas as pd
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj1 = pd.Series(sdata)
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj2 = pd.Series(sdata, index=states)
obj3 = pd.isnull(obj2)

import math
print(f"A= {math.isnan(obj2['California'])}")
print(f"B= {obj3['California']}")
x = obj2['California']
print(f"C= {obj2['California'] != x}")
print(f"D= {obj2['California'] == None}")