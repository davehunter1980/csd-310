CREATE TABLE client(  
    client_id INT NOT NULL AUTO_INCREMENT,
    client_last_name VARCHAR(25) NOT NULL,
    client_first_name VARCHAR(30) NOT NULL,
    client_join_date DATE NOT NULL,
    client_join_time TIME NOT NULL,
    PRIMARY KEY(client_id)
);

CREATE TABLE account_type (  
    account_type_id INT NOT NULL AUTO_INCREMENT,
    account_type_name VARCHAR(15) NOT NULL,
    PRIMARY KEY(account_type_id)
);

CREATE TABLE account(  
    account_id INT NOT NULL AUTO_INCREMENT,
    account_type_id INT,
    account_balance DOUBLE NOT NULL,
    account_open_date DATE NOT NULL,
    account_open_time TIME NOT NULL,
    client_id INT,
    PRIMARY KEY(account_id),
    FOREIGN KEY(account_type_id) REFERENCES account_type (account_type_id),
    FOREIGN KEY (client_id) REFERENCES client(client_id)
);

CREATE TABLE transaction_type (  
    transaction_type_id INT NOT NULL AUTO_INCREMENT,
    transaction_type_name VARCHAR(15) NOT NULL,
    PRIMARY KEY(transaction_type_id)
);

CREATE TABLE transaction (  
    transaction_id INT NOT NULL AUTO_INCREMENT,
    transaction_type_id INT,
    transaction_amount DOUBLE NOT NULL,
    transaction_date DATE NOT NULL,
    transaction_time TIME NOT NULL,
    account_id INT,
    PRIMARY KEY(transaction_id),
    FOREIGN KEY(transaction_type_id) REFERENCES transaction_type (transaction_type_id),
    FOREIGN KEY(account_id) REFERENCES account (account_id)
);