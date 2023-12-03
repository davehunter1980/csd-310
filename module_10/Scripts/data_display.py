import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "dba",
    "password": "groupproject",
    "host": "127.0.0.1",
    "database": "Willson",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n Database user {} to connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))
    
    print("-- DISPLAYING client RECORDS --")

    cursor = db.cursor()
    cursor.execute("SELECT * FROM client;")
    clients = cursor.fetchall()

    for client in clients:
        print("\nClient ID: {}\nName: {} {}\nJoin Date and Time: {} {}".format(client[0],client[2],client[1],client[3],client[4]))
    
    print("\n\n--DISPLAYING account RECORDS --")

    cursor.execute("SELECT * FROM account INNER JOIN account_type ON account.account_type_id=account_type.account_type_id \
        INNER JOIN client ON account.client_id=client.client_id;")
    accounts = cursor.fetchall()
    for account in accounts:
        balance = float(account[2])
        balanceString = "{:.2f}".format(balance)
        print("\nAccount ID: {}\nType: {}\nBalance: ${}\nOpen Date and Time: {} {}\nAccount Owner: {} {}\
              ".format(account[0],account[7],balanceString,account[3],account[4],account[10],account[9]))

    print("\n\n-- DISPLAYING transaction RECORDS --")

    cursor.execute("SELECT * FROM transaction INNER JOIN transaction_type ON \
                   transaction.transaction_type_id=transaction_type.transaction_type_id INNER JOIN account ON \
                   account.account_id=transaction.transaction_id INNER JOIN client ON account.client_id=client.client_id;")
    transactions = cursor.fetchall()
    for transaction in transactions:
        amount = float(transaction[2])
        amountString = "{:.2f}".format(amount)
        print("\nTransaction ID: {}\nType: {}\nAmount: ${}\nDate and Time: {} {}\nAccount Owner: {} {}".format(transaction[0],transaction[7],amountString,transaction[3],transaction[4],transaction[16],transaction[15]))

    print("\n\n-- DISPLAYING transaction_types RECORDS --")

    cursor.execute("SELECT * FROM transaction_type;")
    types = cursor.fetchall()

    for type in types:
        print("\nTransaction Type ID: {}\nType Name: {}\n".format(type[0],type[1]))

    print("\n\n-- DISPLAYING account_type RECORDS --")
    cursor.execute("SELECT * FROM account_type")
    types = cursor.fetchall()

    for type in types:
        print("\nAccount Type ID: {}\nType Name {}".format(type[0],type[1]))

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)
finally:
    db.close()