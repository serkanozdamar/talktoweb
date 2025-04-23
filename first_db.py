import sqlite3

import pandas as pd

conn = sqlite3.connect('firstdb.sqlite')


create_query = """DROP TABLE IF EXISTS Ages;
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)"""
cursor = conn.executescript(create_query)
conn.commit()

query_statement = """DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Salihah', 28);
INSERT INTO Ages (name, age) VALUES ('Roslyn', 32);
INSERT INTO Ages (name, age) VALUES ('Julieanne', 15);
INSERT INTO Ages (name, age) VALUES ('Seatle', 17);
INSERT INTO Ages (name, age) VALUES ('Geordan', 30);
INSERT INTO Ages (name, age) VALUES ('Ruaidhri', 31);"""

cursor2 = conn.executescript(query_statement)
conn.commit()


query_statement = 'SELECT hex(name || age) AS X FROM Ages ORDER BY X'
out = pd.read_sql(query_statement, conn)
cursor3 = conn.execute(query_statement)
out2 = cursor.fetchall()
print(out)
print(out2)

