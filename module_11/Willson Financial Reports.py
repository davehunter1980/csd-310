import mysql.connector
from mysql.connector import errorcode
import calendar

config = {
    "user": "root",
    "password": "1qaz!QAZ1qaz!QAZ",
    "host": "127.0.0.1",
    "database": "willson_financial",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

#Query displaying all clients who've joined in the past 6 months
cursor.execute("SELECT * FROM client WHERE client_join_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH)")
clients = cursor.fetchall()
print("-- Clients Enrolled in Past 6 Months --")
count = 1
for client in clients:
    output = "{}: {} {}".format(count,client[2],client[1])
    print(output)
    count += 1

#Query displaying clients who've made more than 10 transactions per month
query = """
    SELECT 
        client.client_id, 
        client_first_name, 
        client_last_name, 
        YEAR(transaction.transaction_date) AS year,
        MONTH(transaction.transaction_date) AS month, 
        COUNT(transaction.transaction_id) AS transaction_count
    FROM 
        client
    JOIN 
        account ON client.client_id = account.client_id
    JOIN 
        transaction ON account.account_id = transaction.account_id
    GROUP BY 
        client.client_id, YEAR(transaction.transaction_date), MONTH(transaction.transaction_date)
    HAVING 
        COUNT(transaction.transaction_id) >= 10;"""

cursor.execute(query)
clients = cursor.fetchall()

print("\n-- Clients with 10+ Transactions in a Single Month --")
for i, (client_id, first_name, last_name, year, month, transaction_count) in enumerate(clients, start=1):
    month_name = calendar.month_name[month]
    print(f"{i}: {first_name} {last_name} made {transaction_count} transactions in {month_name} {year}")

#Query displaying the average amount of assets held by all clients
cursor.execute("SELECT AVG(account_balance) AS average_assets FROM account;")
average_assets = cursor.fetchone()[0]
averageString = "{:,.2f}".format(average_assets)
output = "\nAverage Client Assets: ${}".format(averageString)
print(output)

db.close()