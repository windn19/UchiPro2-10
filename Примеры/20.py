import sqlite3

con = sqlite3.connect('movies_db.db')

result = con.execute('''
    SELECT *
    FROM movies
    WHERE director_id = 1;
''').fetchall()

print(*result, sep='\n')

# (3, 'Назад в будущее', 1985, 116, 1)
# (4, 'Форрест Гамп', 1994, 142, 1)
