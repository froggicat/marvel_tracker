import sqlite3

def connect():
    connection = sqlite3.connect("database/marvel.db")
    return connection

def add_or_get_user(username):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        SELECT id FROM users
        WHERE user = ?
    """, (username,))

    user = cursor.fetchone()

    if user:
        user_id = user[0]
    else:
        cursor.execute("""
        INSERT INTO users (user)
        VALUES (?)
    """, (username,))
                
        connection.commit()

        user_id = cursor.lastrowid
    connection.close()

    return user_id