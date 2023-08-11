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
