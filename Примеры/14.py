import sqlite3

con = sqlite3.connect('movies_db.db')

cur = con.cursor()

result = cur.execute('''
    SELECT *
    FROM movies
    WHERE director_id = 3
    ORDER BY title;
''').fetchall()

print(result)
# (8, 'Аватар', 2009, 162, 3)
# (6, 'Поймай меня, если сможешь', 2002, None, 3)
# (9, 'Терминатор', None, 108, 3)
# (7, 'Титаник', 1997, 194, 3)
