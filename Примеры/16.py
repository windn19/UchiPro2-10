import sqlite3

con = sqlite3.connect('movies_db.db')
cur = con.cursor()

new_movie = ('Гарри Поттер и философский камень', 2001, 152)

cur.execute('''
    INSERT INTO movies(title, year, duration)
    VALUES (?, ?, ?);
''', new_movie)

con.commit()

result = cur.execute('''
   SELECT *
   FROM movies
   ORDER BY id DESC;
''').fetchone()

print(result)
# (13, 'Гарри Поттер и философский камень', 2001, 152, None)
