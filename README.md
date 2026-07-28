MARVEL TRACKER

A command-line application built with Python and SQLite that helps users track their Marvel Cinematic Universe (MCU) watch progress.

This project was built as a way to learn software engineering fundamentals, including databases, SQL, JSON, and building a complete application from scratch.

-

FEATURES

- Create or log into a basic account
- View every MCU entry
- Sort titles both chronologically and by release year
- Mark entries as watched and rate them
- View all your 5-star favourites
- Store user accounts, movies and their info, user ratings and watched movies in a SQLite database
- Automatically create and seed the database on first launch

- 

TECHNOLOGIES USED

- Python 3
- JSON
- SQLite

-

INSTALLATION

Clone the repository:

git clone https://github.com/YOUR_USERNAME/marvel-tracker.git

Move into the project folder:

cd marvel-tracker

Run the application:

python main.py

On the first launch, the application will automatically:

 - create the SQLite database
 - create all required tables
 - populate the movie database from the JSON file

-

WHAT I LEARNED

 - Python project structure
 - SQLite databases
 - SQL queries
 - Table relationships
 - Primary and foreign keys
 - Reading data from JSON
 - CRUD operations
 - UPSERT (ON CONFLICT)
 - Writing reusable functions
 - Building a complete command-line application

-

FUTURE IMPROVEMENTS

 - Search for titles
 - Display overall viewing statistics
 - Show percentage of the MCU completed
 - Edit or remove ratings
 - Better input validation
 - Terminal colours and improved UI
 - Import new MCU releases automatically from an API



