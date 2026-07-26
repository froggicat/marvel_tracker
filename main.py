from database.database import *

create_tables()

def view_titles():
    print("---")
    movies = get_all_movies()
    for movie in movies:
        print(movie[1])
    print("---")

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
        print("Marvel Tracker")
        print("--------------")
        print("1. View all titles")
        print("2. Sort chronologially")
        print("3. Sort by release year")
        print("4. Quit")
        choice = int(input("Enter Choice: "))

        if choice == 1:
            view_titles()
        elif choice == 2:
            view_chronologically()
        elif choice == 3:
            view_by_year()
        elif choice == 4:
            print("thank you for using my marvel tracker :)")
            break

main()

    



