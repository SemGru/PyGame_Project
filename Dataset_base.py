import sqlite3

DB = sqlite3.connect('server_for_game.db')
SQL = DB.cursor()
SQL.execute("""CREATE TABLE IF NOT EXISTS users  (
    login TEXT,
    score INTEGER)""")
DB.commit()

al = SQL.execute("SELECT * FROM users ORDER BY score DESC").fetchall()

num_1 = al[0]
num_2 = al[1]
num_3 = al[2]
print(num_1, num_2, num_3)


def save_plaer(name, score):
    SQL.execute(f"INSERT INTO users VALUES (?, ?)", (name, score))
    DB.commit()
