# This is a script I will use to mess around with building a database using SQLite
# I will use this database in the actual project once I have it running

import sqlite3

conn = sqlite3.connect('playerPointDatabase2020.db')
c = conn.cursor()

#c.execute("""CREATE TABLE players (
 #   name text,
  #  position text,
   # points real
    #)""")

#conn.commit()

#c.execute("INSERT INTO players VALUES ('Nathan Wales', 'WR', '14.6')")
#conn.commit()

c.execute("SELECT * FROM players WHERE position = 'WR'")
print(c.fetchall())
conn.close()