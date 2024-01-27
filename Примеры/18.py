import sqlite3

con = sqlite3.connect('movies_db.db')
cur = con.cursor()

new_movies = [
    ('Гарри Поттер и Тайная комната', 2002, 161),
    ('Гарри Поттер и узник Азкабана', 2004, 142)
]

cur.executemany('''
    INSERT INTO movies(title, year, duration)
    VALUES (?, ?, ?);
''', new_movies)

con.commit()

result = cur.execute('''
   SELECT *
   FROM movies
   ORDER BY id DESC;
''').fetchmany(2)

print(*result, sep='\n')
# (15, 'Гарри Поттер и узник Азкабана', 2004, 142, None)
# (14, 'Гарри Поттер и Тайная комната', 2002, 161, None)
