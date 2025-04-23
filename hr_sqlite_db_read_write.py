# print("X degerini giriniz")
# x = input()
# print("Y degerini giriniz")
# y = input()
#
# toplam = int(x) + int(y)
#
# print("{0} {1} {2}".format("Toplam ","=",toplam))

import sqlite3

import pandas as pd

conn = sqlite3.connect('HR.db')

# data = pd.read_csv('./employees.csv')
#
# data.to_sql('Employees', conn)

query_statement = 'SELECT * FROM Employees'
out = pd.read_sql(query_statement, conn)
cursor = conn.execute(query_statement)
out2 = cursor.fetchall()
print(out)
print(out2)