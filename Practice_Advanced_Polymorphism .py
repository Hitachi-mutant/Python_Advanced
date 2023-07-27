# '''Exercise 1: Building a Bank Account System
# Implement a BankAccount class that represents a bank account. 
# It should have private attributes like account number and balance, 
# and public methods for depositing, withdrawing, and getting the account balance.'''

# class Bank_acount_system:
#     def __init__(self, number, balance):
#         self.number = number
#         self.balance = balance
#     def depositing(self, deposit):
#         self.balance += deposit
#         return self.balance
#     def withdrawing(self, withdraw):
#         self.balance -= withdraw
#         return self.balance
#     def get_balance(self):
#         return self.balance

# bank = Bank_acount_system(123, 1000)
# print(bank.depositing(20))
# print(bank.withdrawing(30))
# print(bank.get_balance())


# '''Exercise 2: Creating a Student Class
# Implement a Student class that represents a student. 
# It should have public attributes like name and grade, and a 
# private attribute for storing the student's ID. Use protected attributes 
# to store a list of courses taken by the student.'''

# class Students:
#     def __init__(self, name, grade, _courses: list, __student_id):
#         self.name = name
#         self.grade = grade
#         self.__student_id = __student_id
#         self._courses = _courses
#     def info_student(self):
#         return f"Name: {self.name}\nGrade: {self.grade}\nCourses: {self._courses}"
    
#     def show_student_id(self):
#         return self.__student_id

# class Student(Students):
#     def __init__(self, name, grade, _courses, __student_id):
#         super().__init__(name, grade, _courses, __student_id)
#     def add_subject(self, new_subject):
#         self._courses.append(new_subject)
#         return self._courses

# student = Student("John", 8, ["math", "pe", "eng", "ua"], 933)
# print(student.add_subject("history"))
# print(student.info_student())


# '''Exercise 3: Social Media Post
# Create a class Post that represents a social media post. 
# The post should have attributes like content, author, and number of likes. 
# Use private access modifiers for the number of likes and provide methods to like and display the post.'''

# class Post:
#     def __init__(self, content, author, number_of_likes):
#         self.content = content
#         self.author = author
#         self.__number_of_likes = number_of_likes

#     # def display_post(self):
#     #     return self.content

#     def like_the_post(self):
#         self.__number_of_likes += 1
#         return self.__number_of_likes
    
#     def get_number_of_likes(self):
#         return self.__number_of_likes

# post = Post("Lorem ipsuuum, bitches!", "John Deer", 7)

# print(post.content)
# print(post.get_number_of_likes())
# post.like_the_post()
# print(post.get_number_of_likes())


# '''Exercise 4: Managing Employees
# Implement an Employee class that represents an employee in a company. 
# Each employee should have variables like name, department, manager, skills, 
# English level and salary. English level field should be protected and salary field should be private. 
# Create a Department class that contains employees and methods for adding and removing employees, 
# as well as calculating the average salary for the department.'''

# class Employee:
#     def __init__(self, name, department, manager, skills, English_level, salary):
#         self.name = name
#         self.department = department
#         self.manager = manager
#         self.skills = skills
#         self.English_level = English_level
#         self.salary = salary

# class Department:
#     def __init__(self, name):
#         self.name = name
#         self.employees = []

#     def add_employee(self, employee):
#         self.employees.append(employee)
#         return self.employees

#     def remove_employee(self, employee):
#         self.employees.remove(employee)
#         return self.employees
    
#     def __str__(self):
#         employee_list = "\n".join([f"{employee.name}, {employee.department}, {employee.salary}" for employee in self.employees])
#         return f"Employees in {self.name}:\n{employee_list}"

#     def average_salary_of_department(self):
#         if not self.employees:
#             return 0
#         total_salary = sum(employee.salary for employee in self.employees)
#         return total_salary / len(self.employees)


# employee_1 = Employee('Derec Carter', 'DevOps', 'Erwin Schrodinger', 'Fishing', 'A1', 37000)
# employee_2 = Employee('Liza Smith', 'Sales', 'Marie Curie', 'Great soprano', 'A2', 28000)
# employee_3 = Employee('Joshua Tree', 'Legal', 'Niels Bohr', 'Very tall', 'A3', 34000)

# dept = Department('Super-Department')
# dept.add_employee(employee_1)
# dept.add_employee(employee_2)
# dept.add_employee(employee_3)
# print(dept)
# dept.remove_employee(employee_2)
# print(dept)

# average_salary = dept.average_salary_of_department()
# print(f"Average salary of {dept.name}: {average_salary:.2f}")


# '''Exercise 5: Movie Database
# Create a Movie class that represents a movie in a movie database. 
# The class should have various fields to store information about the movie, such as its title, 
# director, genre, release year, duration, and ratings. Use public, private, 
# and protected access modifiers appropriately. Implement methods to update movie details, 
# calculate average ratings, and display movie information.'''

# class Movie:
#     _movies = []
#     def __init__(self, title, director, genre, release_year, duration, ratings):
#         self.title = title
#         self.director = director
#         self.genre = genre
#         self._release_year = release_year
#         self.duration = duration
#         self._ratings = ratings
#         Movie._movies.append(self)

#     @classmethod
#     def average_ratings(cls):
#         if not cls._movies:
#             return 0
#         avg_ratings = sum(movie._ratings for movie in cls._movies)
#         return avg_ratings / len(cls._movies)
    
#     @classmethod
#     def movie_information(cls, movie_name):
#         for movie in cls._movies:
#             if movie.title == movie_name:
#                 return movie
    
#     def __str__(self):
#         return f"Movie: {self.title}, Director: {self.director}, Genre: {self.genre}, Release Year: {self._release_year}, Duration: {self.duration}, Ratings: {self._ratings}"


# movie_1 = Movie('The Enigma', 'Michael Anderson', 'Thriller', 2020, 128, 6.8)
# movie_2 = Movie('Eternal Shadows', 'Sophia Ramirez', 'Drama', 2019, 145, 8.5)
# movie_3 = Movie('Quantum Horizon', 'Alexander Morgan', 'Sci-Fi', 2021, 153, 7.9)

# movie_1._movies.append(movie_1)
# movie_2._movies.append(movie_2)
# movie_3._movies.append(movie_3)

# avg_rating = Movie.average_ratings()
# print(avg_rating)

# movie_information = Movie.movie_information('Eternal Shadows')
# print(movie_information)


'''Exercise 6: Fitness Tracker
Create a FitnessTracker class that represents a fitness tracking application. 
The class should have various fields to store information about user activities, 
such as the user's name, age, weight, height, daily step count, and total calories burned. 
Use public, private, and protected access modifiers appropriately. 
Implement methods to log daily activities, calculate daily calorie burn, and display user information.'''

# class FitnessTracker:
#     _list_of_users = []
#     def __init__(self, name, age, weight, height, daily_step_count, total_calories_burned) -> None:
#         self.name = name
#         self.age = age
#         self._weight = weight
#         self._height = height
#         self.daily_step_count = daily_step_count
#         self.__total_calories_burned = total_calories_burned
#         FitnessTracker._list_of_users.append(self)

#     @classmethod
#     def log_daily_activities(cls):

#         with open("daily_activity_log.txt", "a") as log_file:
#             for user in cls._list_of_users:
#                 log_file.write(str(user) + '\n')
#         log_file.close()
#         return 'Data logged'

#     def __str__(self):
#         return f'{self.name}, age: {self.age}, weight: {self._weight}, height: {self._height}. Steps count today: {self.daily_step_count}, Calories burned: {self.__total_calories_burned}'

#     def daily_calorie_burn(self, amount_of_days):
#         return self.__total_calories_burned / amount_of_days


# user_1 = FitnessTracker('Anna', 22, 48, 161, 1500, 2800)
# user_2 = FitnessTracker('Oleg', 27, 88, 185, 3200, 5900)

# print(str(user_1))

# log_daily_activity = user_1.log_daily_activities()
# print(log_daily_activity)

# print(user_1.daily_calorie_burn(5))


'''Exercise 7: Flight Booking System
Create a Flight class that represents a flight in a booking system. 
The class should have various fields to store information about the flight, 
such as flight number, departure city, destination city, departure time, and available seats. 
Use public, private, and protected access modifiers appropriately. Implement methods to book seats, 
check seat availability, calculate flight duration, and display flight information'''

class Flight:
    pass














