import sqlite3

con = sqlite3.connect('movies_db.db')
cur = con.cursor()

result = cur.execute('''
    SELECT *
    FROM movies
    WHERE director_id = 1;
''')

for row in result:
    print(*row)

for row in result:
    print(*row)

# 3 Назад в будущее 1985 116 1
# 4 Форрест Гамп 1994 142 1
