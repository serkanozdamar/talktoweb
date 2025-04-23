import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

# cur.execute('''
# CREATE TABLE Counts (email TEXT, count INTEGER)''')
cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = 'mbox.txt'

fh = open(fname)
emails = {}
organisations = {}
for line in fh:
    if not line.startswith('From: '): # or line.startswith('To: ')):
        continue
    pieces = line.split()
    email = pieces[1]
    if email in emails:
        emails[email] += 1
    else:
        emails[email] = 1

    org = (email.split("@")[-1])#.split(".")[0]

    if org in organisations:
        organisations[org] += 1
    else:
        organisations[org] = 1

# for email, count in emails.items():
#     cur.execute('''INSERT INTO Counts (email, count) VALUES (?, ?)''', (email,count))
for org, count in organisations.items():
    cur.execute('''INSERT INTO Counts (org, count) VALUES (?, ?)''', (org,count))
conn.commit()

# https://www.sqlite.org/lang_select.html
# sqlstr = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()