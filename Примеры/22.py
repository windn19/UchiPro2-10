import sqlite3

con = sqlite3.connect('movies_db.db')
try:
    con.execute('''
        INSERT INTO genres(title)
        VALUES('фантастика');
    ''')
    con.commit()
except sqlite3.DatabaseError as e:
    print(f'{e.__class__.__name__}: {e}')

# IntegrityError: UNIQUE constraint failed: genres.title
