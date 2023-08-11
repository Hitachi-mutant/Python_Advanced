'''Home work for the lesson 16'''

'''Task 1 - School:
 Make a class structure in python representing people at school. 
 Make a base class called Person, a class called Student, and another one called Teacher. 
 Try to find as many methods and attributes as you can which belong to different classes, 
 and keep in mind which are common and which are not. For example, the name should be a 
 Person attribute, while salary should only be available to the teacher. '''

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Teacher(Person):
    def __init__(self, first_name, last_name, age, subject, salary):
        super().__init__(first_name, last_name, age)
        self.subject = subject
        self.salary = salary

    @property
    def subject_teacher(self):
        return f'{self.subject}: {self.first_name} {self.last_name}'
    
    @property
    def show_salary(self):
        return f'{self.first_name} {self.last_name} has a salary ${self.salary}k per year'

class Student(Person):
    
    def __init__(self, first_name, last_name, age, list_of_subjects_and_grades, attendance):
        super().__init__(first_name, last_name, age)
        self.list_of_subjects_and_grades = list_of_subjects_and_grades
        self.attendance = attendance

    @property
    def student_card(self):
        avarage_grade = sum(self.list_of_subjects_and_grades.values()) /len(self.list_of_subjects_and_grades)
        return f'{self.first_name} {self.last_name}:\n{self.list_of_subjects_and_grades}\n Avarage grade: {avarage_grade:.2f}\n Attendance: {self.attendance}%'

mr_Edison = Teacher('Robert', 'Edison', 43, 'History', 36)
mr_Pool = Teacher('Tom', 'Pool', 51, 'Geography', 41)
mrs_Smith = Teacher('Anna', 'Smith', 27, 'English', 24)

teachers = [mr_Edison, mr_Pool, mrs_Smith]

for teacher in teachers:
    print(teacher.subject_teacher)
for teacher in teachers:
    print(teacher.show_salary)

student_1 = Student('Rob', 'Stark', 18, {'History' : 72, 'Geography' : 68, 'English' : 55}, 82)
student_2 = Student('Sansa', 'Stark', 16, {'History' : 88, 'Geography' : 58, 'English' : 79}, 91)
student_3 = Student('Aria', 'Stark', 15, {'History' : 43, 'Geography' : 95, 'English' : 89}, 73)

students = [student_1, student_2, student_3]

for student in students:
    print(student.student_card)


'''Task 2 - Mathematician: 
Implement a class Mathematician which is a helper class for doing math operations on lists
The class doesn't take any attributes and only has methods:
square_nums (takes a list of integers and returns the list of squares)
remove_positives (takes a list of integers and returns it without positive numbers
filter_leaps (takes a list of dates (integers) and removes those that are not 'leap years'.'''

class Mathematician:
        
    def square_nums(self, input_list):
        return [item **2 for item in input_list]

    def remove_positives(self, input_list):
        return [item for item in input_list if item < 0]

    def filter_leaps(self, input_list):
        result = []
        for year in input_list:
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        result.append(year)
                else:
                    result.append(year)
        return result
 
m = Mathematician()
print(m.square_nums([7, 11, 5, 4]))                     #[49, 121, 25, 16]
print(m.remove_positives([26, -11, -8, 13, -90]))       #[-11, -8, -90]
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))   #[1884, 2020]


'''Task 3 - Product Store:
Write a class Product that has three attributes:
type, name, price
Then create a class ProductStore, which will have some Products and will operate 
with all products in the store. All methods, in case they can’t perform its action, 
should raise ValueError with appropriate error information.'''

class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price

class ProductStore:
    def __init__(self):
        self.products = []

    def add(self, product, amount):
        product_info = {
            "type": product.type,
            "name": product.name,
            "price": product.price,
            "amount": amount
        }
        self.products.append(product_info)

    def list_products(self):
        for product in self.products:
            print(f"Type: {product['type']}, Name: {product['name']}, Price: ${product['price']}, Amount: {product['amount']}")

    def sell(self, product_to_sell, amount_to_sell):
        for product in self.products:
            if product['name'] == product_to_sell:
                if product['amount'] >= amount_to_sell:
                    product['amount'] -= amount_to_sell
                    return self.products
                else:
                    return f'Not enough amount of "{product_to_sell}" to sell.'
        raise ValueError(f'Product "{product_to_sell}" is not found in the store.')
    
    def get_product_info(self, info_about_product):
        for product in self.products:
            if product['name'] == info_about_product:
                return product['name'], product['amount']
        raise ValueError(f'There is no information about "{info_about_product}".')
    
p1 = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)

s = ProductStore()

s.add(p1, 10)
s.add(p2, 300)

s.list_products()

print(s.sell('Ramen', 10))
print(s.get_product_info('Ramen'))     #('Ramen', 290)
print(s.sell('Football T-Shirt', 50))

try:
    s.sell('Sushi', 10)
except ValueError as e:
    print(e)

try:
    s.get_product_info('Hoody')
except ValueError as e:
    print(e)


'''Task 4 - Custom exception:
Create your custom exception named 'CustomException', you can inherit from base Exception class, 
but extend its functionality to log every error message to a file named 'logs.txt'. Tips: 
Use __init__ method to extend functionality for saving messages to file'''

class ErrorHandler:

    def catch_error(self, func, *args):
        try:
            return func(*args)
        except Exception as e:
            error_type = type(e).__name__
            error_message = str(e)
            return f'Error Type: {error_type}. Message: {error_message}'

class CustomException(ErrorHandler):

    def __init__(self):
        self.log_file = open('Python_Advanced/logs.txt', "a")

    def log_error(self, msg):
        self.log_file.write(msg + '\n')

    def __del__(self):
        self.log_file.close()
    

def return_element(a):
    return a[2]
def divide_numbers(a, b):
    return a / b
def add_numbers(a, b):
    return a + b

error_handler = ErrorHandler()

result1 = error_handler.catch_error(return_element, [1, 2])
result2 = error_handler.catch_error(divide_numbers, 10, 0)
result3 = error_handler.catch_error(add_numbers, 10, '5')

print(result1)
print(result2)
print(result3)

error_log_file = CustomException()
error_log_file.log_error(result1)
error_log_file.log_error(result2)
error_log_file.log_error(result3)
