from database.database import *
from database.user_stuff import *
import json
from database.database import add_movie

create_tables()

def seed_database():
    with open("database/mcu_timeline.json", "r") as file:
        movies = json.load(file)

        for movie in movies:
            add_movie(
                movie["title"],
                movie["type"],
                movie["chronological_order"],
                movie["release_year"] 
            )

def view_chronologically():
    movies = get_all_movies_chron()
    counter = 1
    print("---")
    for movie in movies:
        print(f"{counter}. {movie[1]}")
        counter += 1
    print("---")

def view_by_year():
    movies = get_all_movies_release()
    counter = 1
    print("---")
    for movie in movies:
        print(f"{counter}. {movie[1]}")
        counter += 1
    print("---")

if database_empty() == 0:
    seed_database()


print("Welcome, User!")
username = input("Enter Username: ")
id = add_or_get_user(username)
print(f"Logged in as {username}, ID {id}")

def main():
    while True:
        print(f"{username}'s Marvel Tracker")
        print("--------------")
        print("1. View all titles")
        print("2. Mark as watched")
        print("3. View favourite")
        print("4. Quit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            order = input("Release or Timeline order? (R/T) : ")
            if order.upper() == "R":
                print("-----------")
                view_by_year()
                print("-----------")
            elif order.upper() == "T":
                print("-----------")
                view_chronologically()
                print("-----------")
        elif choice == 2:
            title = input("Which movie? ")
            rating = int(input("Rating out of 5? "))

            user_id = get_user_id(username)
            movie_id = get_movie_id(title)

            if movie_id is None:
                print("That movie doesn't exist - please try again.")

            mark_watched(movie_id, user_id, rating)
            print("-----------")
            print(f"Marked {title} as watched, with a rating of {rating} stars!")
            print("-----------")
        elif choice == 3:
            print("-----------")
            movies = get_favourites(id)
            for movie in movies:
                print(movie[0])
            print("-----------")
        elif choice == 4:
            print("thank you for using my marvel tracker :)")
            break

main()

    



