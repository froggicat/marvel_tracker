import json
from database.database import add_movie

with open("database/mcu_seeding.json", "r") as file:
    movies = json.load(file)

    for movie in movies:
        add_movie(
            movie["title"],
            movie["type"],
            movie["chronological_order"],
            movie["release_year"]
        )