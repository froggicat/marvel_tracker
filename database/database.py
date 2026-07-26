import sqlite3

def connect():
    connection = sqlite3.connect("database/marvel.db")
    return connection

def create_tables():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL UNIQUE,
            type TEXT NOT NULL,
            chronological_order INTEGER,
            release_year INTEGER
            )              
        ''')

    connection.commit()
    connection.close()

def add_movie(title, movie_type, chronological_order, release_year):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO movies (
                   title,
                   type,
                   chronological_order,
                   release_year)
        VALUES  (?, ?, ?, ?)
    """, (
        title, 
        movie_type,
        chronological_order,
        release_year
    ))
    connection.commit()
    connection.close()

def get_all_movies():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM movies
    """)
    movies = cursor.fetchall()
    connection.close()
    return movies

def get_all_movies_chron():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM movies
    ORDER BY chronological_order
    """)
    movies = cursor.fetchall()
    connection.close()
    return movies

def get_all_movies_release():
    connection = connect()
    cursor = connection.cursor()
    cursor.execute("""
    SELECT * FROM movies
    ORDER BY release_year
    """)
    movies = cursor.fetchall()
    connection.close()
    return movies