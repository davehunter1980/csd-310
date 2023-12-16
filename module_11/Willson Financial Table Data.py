import mysql.connector

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "1qaz!QAZ1qaz!QAZ",
    "database": "willson_financial"
}

conn = mysql.connector.connect(**db_config)

cursor = conn.cursor()

clients_data = [
    ("Smith", "Jerry", "2023-01-01", "17:57"),
    ("King", "Ethan", "2023-04-01", "09:56"),
    ("Book", "Julie", "2023-07-25", "14:14"),
    ("McGuire", "Fred", "2023-01-10", "16:29"),
    ("Jensen", "Sally", "2023-06-10", "14:01"),
    ("Pinkman", "Thomas", "2023-03-10", "09:40")
]

accounts_data = [
    (7500, "2023-04-01", "16:47", 1, 6),
    (255, "2023-04-10", "09:49", 1, 2),
    (522, "2023-05-01", "08:16", 3, 4),
    (654, "2023-02-02", "09:19", 1, 1),
    (12214, "2023-01-05", "13:45", 2, 1),
    (1443, "2023-08-02", "14:14", 2, 3),
    (2100, "2023-01-15", "09:11", 3, 4),
    (3324, "2023-06-25", "08:23", 2, 5)
]

transactions_data = [
    (6000, "2023-05-08", "04:54:46", 2, 1),
    (120, "2023-12-30", "21:11:25", 2, 1),
    (1500, "2023-10-06", "09:33:11", 2, 1),
    (522, "2023-04-06", "08:48:31", 2, 1),
    (700, "2023-12-25", "23:43:04", 2, 2),
    (46, "2023-04-28", "08:08:17", 2, 2),
    (135, "2023-06-01", "06:57:57", 1, 2),
    (2000, "2023-06-17", "08:38:04", 2, 2),
    (1755, "2023-10-21", "08:38:13", 2, 2),
    (2368, "2023-08-24", "06:15:05", 2, 3),
    (4000, "2023-05-12", "05:06:15", 2, 3),
    (750, "2023-11-13", "12:08:46", 1, 3),
    (1443, "2023-08-16", "08:44:23", 2, 7),
    (50, "2023-11-01", "03:54:39", 1, 7),
    (75, "2023-01-20", "09:26:24", 2, 7),
    (123, "2023-03-02", "04:34:28", 2, 7),
    (211, "2023-05-01", "02:09:26", 2, 7),
    (34, "2023-09-14", "11:34:56", 3, 7),
    (89, "2023-06-28", "03:21:03", 1, 7),
    (777, "2023-03-26", "09:29:46", 2, 7),
    (500, "2023-06-16", "11:43:42", 2, 4),
    (55, "2023-06-23", "04:34:17", 2, 4),
    (75, "2023-10-23", "02:05:35", 1, 4),
    (80, "2023-09-19", "13:50:07", 2, 4),
    (45, "2023-06-20", "07:24:26", 2, 4),
    (333, "2023-06-23", "07:52:57", 1, 4),
    (20, "2023-04-12", "11:04:02", 2, 4),
    (10, "2023-04-24", "14:13:10", 2, 1),
    (125, "2023-11-23", "12:29:14", 1, 1),
    (225, "2023-10-25", "14:28:38", 2, 1),
    (30, "2023-03-28", "09:53:23", 2, 5),
    (22, "2023-03-28", "14:47:47", 2, 5),
    (65, "2023-03-14", "08:03:49", 2, 5),
    (10, "2023-03-07", "15:47:13", 2, 5),
    (15, "2023-03-15", "13:02:17", 3, 5),
    (93, "2023-03-07", "09:02:47", 2, 5),
    (58, "2023-03-14", "13:15:53", 2, 5),
    (26, "2023-03-13", "06:38:00", 2, 5),
    (60, "2023-03-05", "16:49:56", 1, 5),
    (57, "2023-03-20", "16:18:17", 2, 5),
    (78, "2023-10-16", "11:42:31", 2, 6),
    (21, "2023-08-19", "13:45:59", 2, 6),
    (34, "2023-05-15", "11:13:49", 2, 8),
    (2122, "2023-08-26", "09:38:13", 2, 8),
    (1202, "2023-07-03", "15:07:14", 2, 8)
]

transaction_type_data = [
    ("withdrawal",),
    ("deposit",),
    ("transfer",)
]

account_type_data = [
    ("checking",),
    ("savings",),
    ("investment",)
]

insert_client_query = """
INSERT INTO client (client_last_name, client_first_name, client_join_date, client_join_time)
VALUES (%s, %s, %s, %s)
"""

insert_account_type_query = """
INSERT INTO account_type (account_type_name)
VALUES (%s)
"""

insert_transaction_type_query = """
INSERT INTO transaction_type (transaction_type_name)
VALUES (%s)
"""

insert_account_query = """
INSERT INTO account (account_balance, account_open_date, account_open_time, account_type_id, client_id)
VALUES (%s, %s, %s, %s, %s)
"""

insert_transaction_query = """
INSERT INTO transaction (transaction_amount, transaction_date, transaction_time, transaction_type_id, account_id)
VALUES (%s, %s, %s, %s, %s)
"""

cursor.executemany(insert_client_query, clients_data)

cursor.executemany(insert_account_type_query, account_type_data)

cursor.executemany(insert_transaction_type_query, transaction_type_data)

cursor.executemany(insert_account_query, accounts_data)

cursor.executemany(insert_transaction_query, transactions_data)

conn.commit()
