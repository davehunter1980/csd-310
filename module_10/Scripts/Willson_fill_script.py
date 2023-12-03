import json
import mysql.connector
from mysql.connector import errorcode

# Open data file
filename = "Willson.json"
file = open(filename)

config = {
    "user": "dba",
    "password": "groupproject",
    "host": "127.0.0.1",
    "database": "Willson",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)

print("\n Database user {} to connected to MySQL on host {} with database {}\n".format(config["user"], config["host"], config["database"]))

# Load data to list
data = json.load(file)

try:
    cursor = db.cursor()
    fileName = file.name
    output = "Loading from file: {}..."
    print(output.format(filename))

    # Load transaction types to table
    print("\nLoading transaction types...")
    counter = 1
    for i in data["Willson"]["transaction_type"]:
        typeID = counter
        typeName = i["transaction_type_name"]
        counter += 1

        # SQL Call to add the data into the table
        sqlCmd = format("INSERT INTO transaction_type (transaction_type_id, transaction_type_name) VALUES \
                        ({},'{}');").format(typeID, typeName)
        cursor.execute(sqlCmd)
        db.commit()
    print("SUCCESS!\n")
    

    # Load account types from table
    print("Loading account types...")
    counter = 1
    for i in data["Willson"]["account_type"]:
        typeID = counter
        typeName = i["account_type_name"]
        counter += 1

        # SQL Call to add the data into the table
        sqlCmd = format("INSERT INTO account_type (account_type_id, account_type_name) VALUES \
                        ({},'{}');").format(typeID, typeName)
        cursor.execute(sqlCmd)
        db.commit()
    print("SUCCESS!\n")

    # Load client data into database
    print("Loading clients...")
    counter = 1
    for i in data["Willson"]["client"]:
        clientID = counter
        clientLast = i["client_last_name"]
        clientFirst = i["client_first_name"]
        clientDate = i["client_join_date"]
        clientTime = i["client_join_time"]
        counter += 1

        # SQL Call to add the data into the table
        sqlCmd = format("INSERT INTO client (client_id, client_last_name, client_first_name, client_join_date, client_join_time) \
                            VALUES ({},'{}','{}','{}','{}');").format( clientID,clientLast,clientFirst,clientDate,clientTime )
        cursor.execute(sqlCmd)
        db.commit()
    print("SUCCESS\n")

    # load accounts from database
    print("Loading acounts...")
    counter = 1
    for i in data["Willson"]["account"]:
        acctID = counter
        acctType = i["account_type_id"]
        acctBal = i["account_balance"]
        acctCreDate = i["account_open_date"]
        acctCreTime = i["account_open_time"]
        acctCli = i["client_id"]
        counter += 1

        # SQL Call to add the data into the table
        sqlCmd = format("INSERT INTO account (account_id, account_type_id, account_balance, account_open_date, \
                        account_open_time,client_id) VALUES ({},{},{},'{}','{}',{});").format(\
                            acctID,acctType,acctBal,acctCreDate,acctCreTime,acctCli)
        cursor.execute(sqlCmd) 
        db.commit()
    print("SUCCESS!\n")
    
    # load transactions from database
    print("Loading transactions...")
    counter = 1
    for i in data["Willson"]["transaction"]:
        tranID = counter
        tranType = i["transaction_type_id"]
        tranDate = i["transaction_date"]
        tranTime = i["transaction_time"]
        tranAmt = i["transaction_amount"]
        acctID = i["account_id"]
        counter += 1

        # SQL Call to add the data into the table
        sqlCmd = format("INSERT INTO transaction (transaction_id, transaction_type_id, transaction_amount, transaction_date, transaction_time, \
                        account_id) VALUES ({},{},{},'{}','{}',{});").format(\
                            tranID,tranType,tranAmt, tranDate,tranTime,acctID)
        cursor.execute(sqlCmd) 
        db.commit()
    print("SUCCESS!\n")
    print("All data has been loaded to the tables.")
        
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username and password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)
finally:
    db.close()
    file.close()