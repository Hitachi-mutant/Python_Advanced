/*
1. Виберіть перші 10 записів з таблиці "patients".
2. Знайдіть найменший та найбільший вік пацієнта з таблиці "patients".
3. Порахуйте загальну кількість лікарів у таблиці "doctors".
4. Виберіть всіх пацієнтів з ім'ям, що починається на "А".
5. Виберіть всіх пацієнтів, чий вік знаходиться в діапазоні 20-30 років.
6. Вибрати ім'я та спеціальність всіх лікарів з таблиці "doctors".
7. Знайти мінімальний та максимальний вік пацієнтів з таблиці "patients".
8. Вибрати всіх пацієнтів, які мають алергію на певний алерген. (Вам потрібно вказати стовпчик з алергіями та відповідне значення алергену.)
9. Обчислити кількість пацієнтів, які мають діагноз "діабет"
10. Вибрати всіх лікарів, чиє прізвище починається на "Сміт".
11. Вибрати діагнози, які були надані пацієнтам принаймні тричі. (Використовуйте HAVING)
12. Вибрати назви провінцій з таблиці "province names" та відсортувати їх за алфавітом у зростаючому порядку.
*/
--select * from patients LIMIT 10;
--SELECT MIN(birth_date), max(birth_date) from patients;
--select count(doctor_id) from doctors;
--select * from patients where first_name like "A%" limit 50;
--select * from patients where birth_date between '1990-01-01' and '2000-01-01' limit 50;
--select first_name, last_name, specialty from doctors limit 50;
--select * from patients where allergies="Penicillin" limit 50;
--select * from	admissions where diagnosis like "Diabet%" limit 50;
--select * from	doctors ORDER BY last_name asc
--select * from	doctors here last_name like "Sm%" limit 50;
--select COUNT(diagnosis), diagnosis from admissions GROUP BY diagnosis HAVING COUNT(diagnosis) >= 3 limit 50;
--select province_name from	province_names ORDER BY province_name asc

/*13. Знайти кількість пацієнтів у кожній провінції, відсортувавши 
результати за зростанням кількості.
14. Знайти кількість пацієнтів для кожної провінції та вивести 
тільки ті провінції, де кількість пацієнтів більше 50.
15. Знайти кількість пацієнтів з віком від 60 до 80 років для кожної провінції 
та вивести тільки ті провінції, де кількість пацієнтів більше 10
*/

/*select count(patients.first_name), province_names.province_name      
from patients JOIN province_names ON patients.province_id=province_names.province_id group by province_name     	 
order by count(patients.first_name) asc;*/
/*select count(patients.first_name), province_names.province_name      
from patients JOIN province_names ON patients.province_id=province_names.province_id group by province_name 
having count(patients.first_name) > 50      	 
order by count(patients.first_name)*/
/*select count(patients.first_name), patients.birth_date, province_names.province_name       
from patients JOIN province_names ON patients.province_id=province_names.province_id 
where birth_date between '1940-01-01' and '1960-01-01' group by province_name 
having count(patients.first_name) > 10;*/



--1. Show the category_name and description from the categories table sorted by category_name.
--select category_name, description from categories order by category_name asc
--2. Show the product_name and unit_price from the products table sorted by unit_price in descending order.
--select product_name, unit_price from products order by unit_price desc
--3. Show all the contact_name, address, city of all customers which are not from 'Germany', 'Mexico', 'Spain'
--select contact_name, address, country, city from customers WHERE country != 'Mexico' and country != 'Germany' and country != 'Spain' order by country;
--4. Show the employee_id, order_id, customer_id, required_date, shipped_date from all orders shipped later than the required date
--select employee_id, order_id, customer_id, required_date, shipped_date from orders where order_date between '2016-09-01' and '2016-10-29';
--5. Show the company_name, contact_name, fax number of all customers that has a fax number.
--select company_name, contact_name, fax from customers where fax != 'None' order by company_name;
--6. Show the employee_id, order_id, customer_id, required_date, shipped_date from all orders where shipped_date is later than required_date.
--select employee_id, order_id, customer_id, required_date, shipped_date from orders where shipped_date > required_date;
--7. Show the supplier_name, contact_name, phone number of all suppliers that have a phone number.
--select company_name, contact_name, phone from suppliers where phone != 'None';
--8. Show the first_name, last_name, hire_date of employees hired before '2022-01-01'.
--select first_name, last_name, hire_date from employees where hire_date < '2022-01-01';
--9. Show the product_name, quantity_per_unit, units_in_stock of all products that have less than 10 units in stock.
--select product_name, quantity_per_unit, units_in_stock from products where units_in_stock < 10;
--10. Show the company_name, contact_name, contact_title of customers that have a contact_title.
--select company_name, contact_name, contact_title from customers where contact_title != 'None';
--11. Show the order_id, ship_country, ship_region of orders where ship_country is not 'USA' and ship_region is not empty.
--select order_id, ship_country, ship_region from orders where ship_country != 'USA' and ship_region != 'None';
--12. Show the employee_id, last_name, first_name of the employees who have the title 'Sales Representative'.
--select employee_id, title, last_name, first_name from employees where title = 'Sales Representative';
--13. List the products that were ordered more than once in a single order. 
--Display the product name, order ID, and quantity ordered.

--select products.product_name, order_details.order_ID, order_details.quantity 
--from products INNER JOIN order_details ON products.product_id=order_details.product_id 
--where order_details.quantity > 1 limit 60;

--14. Retrieve the top 10 most ordered categories of products. 
--Display the category name and the total quantity of products ordered within each category.
/*select categories.category_name, order_details.quantity 
from categories 
JOIN products 
ON categories.category_id=products.category_id
join order_details 
on products.product_id=order_details.product_id 
order by order_details.quantity desc limit 10;*/

--15. Find the employees who have never handled any orders. Display their names and hire dates.
/*select employees.first_name, employees.last_name, employees.hire_date, orders.order_id 
from employees
join orders
on employees.employee_id=orders.employee_id where orders.order_id = 'None';*/

--16. Retrieve a list of orders with the customer's company name and the employee's first 
--and last names. Include only orders placed after January 1, 2010
/*select employees.first_name, employees.last_name, customers.company_name, orders.order_date  
from employees 
join orders
on employees.employee_id=orders.employee_id 
join customers
on orders.customer_id=customers.customer_id 
where orders.order_date > '2016-12-01';*/

--17. Retrieve a list of customers and suppliers who are located in the same city. 
--Display the company name and city for both customers and suppliers. 
--If a city doesn't have any customers or suppliers, show "No Data" for the missing side.
/*SELECT 
    customers.customer_id AS customer_id,
    customers.company_name AS customer_company,
    suppliers.supplier_id AS supplier_id,
    suppliers.company_name AS supplier_company,
    customers.city AS city
FROM 
    customers
JOIN 
    suppliers ON customers.city = suppliers.city;*/
