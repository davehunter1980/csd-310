import mysql.connector
from mysql.connector import errorcode

def show_films(cursor, title):
    # Method to execute an inner join on all tables,
    #    iterate over the dataset and output the results to terminal window.

    # inner join query
    cursor.execute("SELECT film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'Studio Name' from\
                  film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")
    
    # get the results from the cursor object
    films = cursor.fetchall()

    print("\n -- {} --".format(title))

    #iterate over the film data set and display the results
    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0],film[1],film[2],film[3]))

config = {
    "user": "movies_user",
    "password": "popcorn",
    "host": "127.0.0.1",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} to connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))

    cursor = db.cursor()

    show_films(cursor, 'DISPLAYING FILMS')

    cursor.execute("SELECT studio_id from studio WHERE studio_name='Universal Pictures';")
    studios = cursor.fetchall()
    studio = studios[0]

    cursor.execute("SELECT genre_id FROM genre WHERE genre_name='Horror';")
    genres = cursor.fetchall()
    genre = genres[0]

    call = "INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)\
                   VALUES('Frankenstein', '1931', '71', 'James Whale', {}, {});".format(studio[0], genre[0])
    cursor.execute(call)

    show_films(cursor, 'DISPLAYING FILMS AFTER INSERT')
    
    call = "UPDATE film SET genre_id={} WHERE film_name='Alien';".format(genre[0])
    cursor.execute(call)

    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    cursor.execute("DELETE FROM film WHERE film_name='Gladiator'")

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)
finally:
    db.close()