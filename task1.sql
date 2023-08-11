mysql -u AlexS -p
USE my_test_database;

--Create a table (in cmd)
CREATE TABLE customers (
        account_id INT AUTO_INCREMENT PRIMARY KEY,
        account_type VARCHAR(50),
        first_name VARCHAR(50),
        last_name VARCHAR(100),
        email VARCHAR(100),
        registration_date DATE
    );

--Create a table (in DBeaver)
CREATE TABLE address (
        account_id INT AUTO_INCREMENT PRIMARY KEY,
        country VARCHAR(50),
        region VARCHAR(50),
        city VARCHAR(100),
        zip_code INT,
        street VARCHAR(50),
        house INT,
        appartment INT
    );

--rename a table
RENAME TABLE address TO addresses;

--add data
INSERT INTO customers (account_type, first_name, last_name, email, registration_date)
    VALUES
        ('Basic', 'John', 'Doe', 'john@example.com', '2023-01-15'),
        ('Premium', 'Jane', 'Smith', 'jane@example.com', '2022-11-10'),
        ('Standard', 'Michael', 'Johnson', 'michael@example.com', '2023-02-25'),
        ('Premium', 'Emily', 'Williams', 'emily@example.com', '2023-03-18'),
        ('Basic', 'William', 'Brown', 'william@example.com', '2022-09-30'),
        ('Standard', 'Olivia', 'Davis', 'olivia@example.com', '2023-04-12'),
        ('Premium', 'James', 'Anderson', 'james@example.com', '2022-12-08'),
        ('Basic', 'Sophia', 'Martinez', 'sophia@example.com', '2023-06-21'),
        ('Standard', 'Liam', 'Taylor', 'liam@example.com', '2023-07-29'),
        ('Premium', 'Ava', 'Wilson', 'ava@example.com', '2022-10-05'),
        ('Basic', 'Noah', 'Miller', 'noah@example.com', '2023-01-28'),
        ('Standard', 'Emma', 'Jones', 'emma@example.com', '2022-11-20'),
        ('Premium', 'Ethan', 'Garcia', 'ethan@example.com', '2023-02-08'),
        ('Basic', 'Isabella', 'Rodriguez', 'isabella@example.com', '2023-03-06'),
        ('Standard', 'Mia', 'Lopez', 'mia@example.com', '2022-09-12'),
        ('Premium', 'Aiden', 'Perez', 'aiden@example.com', '2023-04-02'),
        ('Basic', 'Lucas', 'Hernandez', 'lucas@example.com', '2023-05-18'),
        ('Standard', 'Charlotte', 'Gonzalez', 'charlotte@example.com', '2022-12-01'),
        ('Premium', 'Elijah', 'Martinez', 'elijah@example.com', '2023-01-10'),
        ('Basic', 'Amelia', 'Rivera', 'amelia@example.com', '2023-07-15'),
        ('Standard', 'Benjamin', 'Walker', 'benjamin@example.com', '2023-08-03');

--add a new column
ALTER TABLE customers ADD COLUMN phone_number VARCHAR(20);

--Insert a couple rows
INSERT INTO customers (account_type, first_name, last_name, email, registration_date, phone_number) 
    VALUES 
        ('Standart', 'Newname', 'Newlastname', 'new@gmail.com', '2023-01-02', '099-345-32-12');

--UPDATE rows (воно додало оркістан - це треба виправити!)
update addresses set country = 'India' where country = 'Russia';
update addresses set region = 'Rajasthan' where region = 'Moscow';
update addresses set city = 'Jaipur' where city = 'Moscow';

--DELETE rows
DELETE FROM customers WHERE email = 'new@gmail.com';
