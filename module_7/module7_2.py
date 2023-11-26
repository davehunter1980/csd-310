import mysql.connector
from mysql.connector import errorcode

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

  #  input("\n\n Press any key to continue...")

    print("-- DISPLAYING Studio RECORDS --")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM studio;")
    studios = cursor.fetchall()

    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0],studio[1]))
    
    print("\n--DISPLAYING Genre RECORDS --")

    cursor.execute("SELECT * FROM genre;")
    genres = cursor.fetchall()
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0],genre[1]))

    print("-- DISPLAYING Short Film RECORDS --")

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime<120;")
    filmsByRuntime = cursor.fetchall()
    for film in filmsByRuntime:
        print("Film Name: {}\nFilm Runtime: {}\n".format(film[0],film[1]))

    print("-- DISPLAYING Director RECORDS in Order")

    cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director;")
    filmsByDirector = cursor.fetchall()

    for film in filmsByDirector:
        print("Film Name: {}\nDirector: {}\n".format(film[0],film[1]))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)
finally:
    db.close()