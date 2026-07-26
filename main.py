from database.database import *
from database.user_stuff import *

create_tables()

print("Welcome, User!")
username = input("Enter Username: ")
id = add_or_get_user(username)
print(f"Logged in as {username}, ID {id}")

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

def main():
    while True:
        print(f"{username}'s Marvel Tracker")
        print("--------------")
        print("1. View all titles")
        print("2. Mark as watched")
        print("3. Quit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            order = input("Release or Timeline order? (R/T) : ")
            if order.upper() == "R":
                view_by_year()
            elif order.upper() == "T":
                view_chronologically()
        elif choice == 2:
            # add error handling
            title = input("Which movie? ")
            rating = int(input("Rating out of 5? "))

            user_id = get_user_id(username)
            movie_id = get_movie_id(title)

            mark_watched(movie_id, user_id, rating)
            print(f"Marked {title} as watched, with a rating of {rating} stars!")
        elif choice == 3:
            print("thank you for using my marvel tracker :)")
            break

main()

    



