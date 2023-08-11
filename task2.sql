-- I'm using my own MySQL database instead of LiteSQL from the task

/* write a query to display the names (first_name, last_name) 
using alias name "First Name", "Last Name" from the table of employees (customers);*/
select first_name as "First Name", last_name as "Last Name" from customers;

-- write a query to get the unique department ID (countries) from the employee (addresses) table
select distinct country from addresses;

-- write a query to get all customers details from the customers table ordered by first name, descending
select * from customers order by first_name desc;

-- write a query to get the names (first_name, last_name), registration date in 2022
select * from customers where registration_date between '2022-01-01' and '2022-12-31';

-- write a query to get the maximum and minimum registration date
SELECT MIN(registration_date), first_name, last_name from customers;
SELECT MAX(registration_date), first_name, last_name from customers;

-- write a query to get registration date in european format
SELECT first_name, last_name, DATE_FORMAT(registration_date, '%d-%m-%Y') AS Day_Months_Year from customers;
