#Counting Organizations This application will read the mailbox data (mbox.txt) count up the number email messages per organization (i.e. domain name of the email address) using a database with the following schema to maintain the counts.
import sqlite3

conn = sqlite3.connect('emaildb2(END).sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From:'):
            continue
    pieces = line.split()
    email = pieces[1]
    org=email.split("@")[1]
    
#split separa por defecto con espacio pero podemos tambien poner con otro parametro
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
# ? is a placeholder to avoid sql injection(destroying database using code injection)
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'
print("Counts:")

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()