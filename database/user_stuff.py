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

def get_user_id(username):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id FROM users
        WHERE user = ?
    """, (username,))

    user = cursor.fetchone()

    connection.close()

    if user:
        return user[0]
    else:
        return None
    
def get_movie_id(title):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id FROM movies
        WHERE title = ?
    """, (title,))

    movie = cursor.fetchone()

    connection.close()

    if movie:
        return movie[0]
    else:
        return None
    

def mark_watched(movie_id, user_id, rating):
    #make this work properly and then check if the movie has been already rated/watched
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO watched_movies (user_id, movie_id, rating)
        VALUES(?, ?, ?)
                   
        ON CONFLICT(user_id, movie_id)
        DO UPDATE SET rating = excluded.rating
    """, (user_id, movie_id, rating,))
    connection.commit()
    connection.close()