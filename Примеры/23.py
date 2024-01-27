import sqlite3

con = sqlite3.connect('movies_db.db')

try:
    with con:
        con.execute('''
            INSERT INTO genres(title)
            VALUES('аниме');
        ''')
except sqlite3.DatabaseError as e:
    print(e)

result = con.execute('''
    SELECT *
    FROM genres;
''').fetchall()

print(result)

# [(1, 'фантастика'), ... , (9, 'аниме')]
