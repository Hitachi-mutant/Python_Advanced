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


# class Flight:

#     def __init__(self, flight_number, departure, arrival, number_of_seats, seat_availability):
#         self.flight_number = flight_number
#         self.departure = departure
#         self.arrival = arrival
#         self.number_of_seats = number_of_seats
#         self.seat_availability = seat_availability

#     def generating_passenger_manifests(self):
#         return f'Flight number {self.flight_number} departure at {self.departure}, arrival at {self.arrival}'


# class DomesticFlight(Flight):
#     def __init__(self, flight_number, departure, arrival, number_of_seats, seat_availability):
#         super().__init__(flight_number, departure, arrival, number_of_seats, seat_availability)

#     available_domestic_airports = ['Miami', 'Houston', 'New York', 'Chicago']
#     def get_domestic_airports(self, destination_city):
#         if destination_city in self.available_domestic_airports:
#             return f'You can book a ticket to the {destination_city}'
#         else:
#             return f'{destination_city} is not available as your destination point. Here is a list of available domestic airports: {self.available_domestic_airports}'



# class InternationalFlight(Flight):
#     def __init__(self, flight_number, departure, arrival, number_of_seats, seat_availability, baggage_fee):
#         super().__init__(flight_number, departure, arrival, number_of_seats, seat_availability)
#         self.baggage_fee = baggage_fee

#     def calculate_baggage_fee(self, baggage_weight):
#         if baggage_weight < 5:
#             return 'No baggage fee applied'
#         elif 5 <= baggage_weight <= 20:
#             return f'Your baggage fee is: {self.baggage_fee}%'
#         else:
#             return 'Baggage weight limit is exceeded'



# def checking_flight_availability(flight):
#     return f'{flight.seat_availability} seats are still available.'


# def booking_seats(flight):
#     return 'You have successfully booked 1 seat' if flight.seat_availability > 0 else 'There are no available seats on this flight'


# domestic_flight = DomesticFlight(1111, '12-00', '18-30', 42, 18)
# international_flight = InternationalFlight(222, '9-00', '15-40', 32, 9, 3)

# print(checking_flight_availability(domestic_flight))
# print(booking_seats(international_flight))

# print(domestic_flight.get_domestic_airports('Seattle'))
# print(international_flight.calculate_baggage_fee(18))
















# Exercise 1: Building a Bank Account System
# Implement a BankAccount class that represents a bank account. 
# It should have private attributes like account number and balance, 
# and public methods for depositing, withdrawing, and getting the account balance.

# class BankAccount:
#     def __init__(self, account_number, balance):
#         self.account_number = account_number
#         self.balance = balance

#     def deposit(self, sum):
#         self.balance = self.balance + sum
#         print(self.balance)

#     def withdraw(self, sum):
#         self.balance = self.balance - sum
#         print(self.balance)

#     def check_balance(self):
#         print(self.balance)


# my_account = BankAccount(123456789, 3000)
# my_account.deposit(500)
# my_account.withdraw(1000)
# my_account.check_balance()


# Exercise 2: Creating a Student Class
# Implement a Student class that represents a student. It should have public attributes 
# like name and grade, and a private attribute for storing the student's ID. Use protected 
# attributes to store a list of courses taken by the student.

# class Student:
#     def __init__(self, name, grade, student_id, courses: list):
#         self.name = name
#         self.grade = grade
#         self.__student_id = student_id
#         self._courses = courses

#     def list_courses(self):
#         print(self._courses)


# my_courses = ["Math", "Computer Science", "Programming", "Statistics"]
# student1 = Student("Petro Fedun", "A", 48920849, my_courses)
# student1.list_courses()


# Exercise 3: Social Media Post
# Create a class Post that represents a social media post. 
# The post should have attributes like content, author, and number of likes. 
# Use private access modifiers for the number of likes and provide methods to like and display the post.

# class Post:
#     def __init__(self, content, author, likes: int):
#         self.content = content
#         self.author = author
#         self.__likes = likes

#     def like(self):
#         self.__likes = self.__likes + 1 
#         print(self.__likes)

#     def display(self):
#         print(f"Check out the article '{self.content}' by {self.author}")


# my_post = Post("5 methods to remove bad breath smell! You will be shocked!", "pipka228", 12)
# my_post.like()
# my_post.display()


# Exercise 4: Managing Employees
# Implement an Employee class that represents an employee in a company. 
# Each employee should have attributes like name, department, manager, skills, 
# English level and salary. English level field should be protected and 
# salary field should be private. Create a Department class that contains employees 
# and methods for adding and removing employees, as well as calculating the average salary for the department.

# class Employee:
#     def __init__(self, name, department, manager, skills, eng_lvl, salary):
#         self.name = name
#         self.department = department
#         self.manager = manager
#         self.skills = skills
#         self._eng_lvl = eng_lvl
#         self.__salary = salary

#     def get_info(self):
#         print(f"Name: {self.name}, Department: {self.department}, Manager: {self.manager}, Skills: {self.skills}, Eng Lvl: {self._eng_lvl}, Salary: {self.__salary}")

#     def get_salary(self):
#         return self.__salary
        

# class Department:
#     def __init__ (self, name, employees: list):
#         self.name = name
#         self.employees = employees

#     def hire(self, employee):
#         self.employees.append(employee)
#         print("A new employee has been hired")
#         print(self.employees)

#     def fire(self, employee):
#         self.employees.remove(employee)
#         print("An employee has been fired")
#         print(self.employees)

#     def view_employees(self):
#         for employee in self.employees:
#             employee.get_info()

#     def average(self):
#         salaries = 0
#         for employee in self.employees:
#             salaries = salaries + employee.get_salary()
#         print(salaries)
#         avrg = salaries // len(self.employees)
#         print(avrg)
        

# empl1 = Employee("Petro Fedun", "IT", "Iryna Zaiets", "programming, bungee jumping, cooking", "C2", 5000)
# empl2 = Employee("Alisiya Horbenko", "IT", "Iryna Zaiets", "business analysis, sky diving, gaming", "C2", 5000)
# empl3 = Employee("Oleksandr Horbenko", "IT", "Iryna Zaiets", "programming, dancing, painting", "C2", 15000)

# employees = [empl1, empl2, empl3]

# it_dept = Department("IT", employees)
# it_dept.hire(empl2)
# it_dept.fire(empl2)
# it_dept.view_employees()
# it_dept.average()


# Exercise 5: Movie Database
# Create a Movie class that represents a movie in a movie database. 
# The class should have various fields to store information about the movie, 
# such as its title, director, genre, release year, duration, and ratings. 
# Use public, private, and protected access modifiers appropriately. 
# Implement methods to update movie details, calculate average ratings, and display movie information.

# class Movie:
#     def __init__(self, title, director, genre, year, dur, rate):
#         self.title = title
#         self.director = director
#         self.genre = genre
#         self.year = year
#         self.dur = dur
#         self.rate = rate

#     def display_info(self):
#         print(f"Title: {self.title}, director: {self.director}, genre: {self.genre}, year: {self.year}, duration: {self.dur}, rating: {self.rate}")

#     def update_info(self, title, director, genre, year, dur, rate):
#         self.title = title
#         self.director = director
#         self.genre = genre
#         self.year = year
#         self.dur = dur
#         self.rate = rate
#         print(f"Title: {self.title}, director: {self.director}, genre: {self.genre}, year: {self.year}, duration: {self.dur}, rating: {self.rate}")

#     def get_rate(self):
#         return self.rate

# my_movie = Movie("Titanic", "Cameron", "Drama", 1997, "2:45", 9)
# # my_movie.display_info()
# # my_movie.update_info("Titanic", "Petro Cameron", "Drama", 1997, "2:48", 9)

# mov1 = Movie("Great Gatsby", "Lurmann", "Drama", 2013, "2:32", 8)
# mov2 = Movie("Barbie", "Del Toro", "Comedy", 2023, "1:48", 7)

# movie_list = [my_movie, mov1, mov2]

# def average_rate(list):
#     ratings = []
#     for movie in list:
#         ratings.append(movie.get_rate())
#     print(ratings)
#     avrg = sum(ratings) / len(ratings)
#     print(avrg)

# average_rate(movie_list)

# Exercise 6: Fitness Tracker
# Create a FitnessTracker class that represents a fitness tracking application. 
# The class should have various fields to store information about user activities, 
# such as the user's name, age, weight, height, daily step count, and total calories burned. 
# Use public, private, and protected access modifiers appropriately. 
# Implement methods to log daily activities, calculate daily calorie burn, and display user information.

# class FitnessTracker:
#     def __init__(self, name, age, weight, height, steps):
#         self.name = name
#         self.__age = age
#         self._weight = weight
#         self._height = height
#         self.steps = steps

#     def display_info(self):
#         print(f"Name: {self.name}. Age: {self.__age}. Weight: {self._weight}. Height: {self._height}. Steps: {self.steps}.")

#     def add_steps(self, new_steps):
#         self.steps = self.steps + new_steps
#         print(f"Your daily steps have been increased by {new_steps} and now it's {self.steps}!")

#     def calorie_calc(self):
#         calories = self.steps / 1000 * 40
#         print(calories)


# my_tracker = FitnessTracker("Alisiya", 23, 60, 174, 10000)
# my_tracker.display_info()
# my_tracker.add_steps(2000)
# my_tracker.calorie_calc()

# Exercise 7: Flight Booking System
# Create a Flight class that represents a flight in a booking system. 
# The class should have various fields to store information about the flight, 
# such as flight number, departure city, destination city, departure time, and available seats. 
# Use public, private, and protected access modifiers appropriately. 
# Implement methods to book seats, check seat availability, calculate flight duration, and display flight information.

# class Flight:
#     def __init__(self, number, dep_city, dest_city, dep_time, arrival_time, seats): 
#         self.__number = number
#         self.dep_city = dep_city
#         self.dest_city = dest_city
#         self._dep_time = dep_time
#         self._arrival_time = arrival_time
#         self.seats = seats

#     def display_info(self):
#         print(f"Flight number: {self.__number}. \nDeparture city: {self.dep_city}. \nDestination city: {self.dest_city}. \nDeparture time: {self._dep_time}. \nArrival Time: {self._arrival_time}. \nSeats available: {self.seats}.")

#     def seat_availability(self):
#         return self.seats
    
#     def book_seats(self):
#         return self.seats-1
    
#     def calculate_flight_duration(self):
#         from datetime import datetime

#         time1 = datetime.strptime(self._arrival_time, "%Y-%m-%d %H:%M")
#         time2 = datetime.strptime(self._dep_time, "%Y-%m-%d %H:%M")
#         time_stamp1 = datetime.timestamp(time1)
#         time_stamp2 = datetime.timestamp(time2)
#         flight_duration = time_stamp2 - time_stamp1
#         end_result = flight_duration/3600
#         return end_result

    
# my_flight = Flight("185H29A", "Odesa", "New York", "2023-07-28 18:45", "2023-07-29 23:00", 12)
# # my_flight = Flight("185H29A", "Odesa", "New York", "18:45", "23:00", 12)
# my_flight.display_info()
# print(my_flight.calculate_flight_duration())

# Завдання 1: Клас "Приз"
# Створіть клас Prize, який представляє приз з можливістю додавання двох призів, порівняння їх за вартістю або категорією, а також виведення опису призу у 
# зрозумілому форматі.

# class Prize:
#     def __init__(self, prize1, value_prize1, prize2, value_prize2):
#         self.prize1 = prize1
#         self.prize2 = prize2
#         self.value_prize1 = value_prize1
#         self.value_prize2 = value_prize2
        
#     def __str__(self):
#         return f'the first prize is {self.prize1}, the second prize {self.prize2}'

#     def __eq__(self):
#         print(f'this is the value of the first prize self{self.value_prize1}, this is of the second {self.value_prize2}')
#         return self.value_prize1 == self.value_prize2
    
        
# prize1 = Prize("A cat", "Priceless", "a Desk", "Priceless")
# print(prize1.__eq__())
# print(prize1.__str__())

# Завдання 2: Клас "Музичний трек"
# Створіть клас MusicTrack, який представляє музичний трек з можливістю додавання двох треків (комбінація імен треків), порівняння треків за тривалістю або стилем, а 
# також виведення назви треку у зрозумілому форматі.

# class MusicPlaylist:
#     def __init__(self, name_of_the_group, name_of_the_song, duration):
#         self.name_of_the_group = name_of_the_group
#         self.name_of_the_song = name_of_the_song
#         self.duration = duration

#     def __str__(self):
#         return f"this is the name of the group {self.name_of_the_group}, this is the name of the song {self.name_of_the_song}"
    
#     def __eq__(self, other):
#         return self.duration == other.duration
    
#     def __lt__(self, other):
#         return self.duration < other.duration
    
# song1 = MusicPlaylist("Darude", "Sandstorm", 247)
# song2 = MusicPlaylist("Rammstein", "Ohne Dich", 360)

# print(song1==song2)
# print(song1<song2)

# Завдання 3: Клас "Часовий інтервал"
# Створіть клас TimeInterval, який представляє часовий інтервал. Кожен інтервал має атрибути: початкова дата та кінцева дата. Перепишіть магічний метод __contains__, 
# щоб можна було перевіряти, чи знаходиться певна дата всередині інтервалу.

# from datetime import datetime

# class TimeInterval:

#     def __init__(self, start_date, end_date):
#         self.start_date = start_date
#         self.end_date = end_date
    
#     def __contains__(self, date):
#         self.date = date
#         return self.start_date <=date <=self.end_date

# time1 = TimeInterval(start_date=datetime(2023, 7, 28), end_date=datetime(2023,8,20))

# if datetime(2023, 10, 30) in time1:
#     print("It's there")
# else:
#     print("It's not there")

# Завдання 4: Клас "Студент"
# Створіть клас Student, який представляє студента. Кожен студент має атрибути: ім'я, курс та середній бал. Перепишіть магічний метод __lt__, 
# щоб студенти можна було порівнювати за середнім балом, а потім за ім'ям (у разі рівних балів).​

# class Student:
#     def __init__(self, name, year, average_score):
#         self.name = name
#         self.year = year
#         self.average_score = average_score
        
#     def __lt__ (self, other):
#         # if self.average_score == other.average_score:
#         #     self.name
#         return self.average_score < other.average_score
    



# Unit tests

import unittest
import unique_names
from unittest.mock import MagicMock



class TestUnique(unittest.TestCase):
    def test_unique_names(self):
        unique_names.get_names_from_file = MagicMock()
        unique_names.get_names_from_file.return_value = ['Jack', 'Ross', 'Mike', 'Jack', 'Tom', 'Kate', 'Ross']
        names = unique_names.get_unique_names("names.txt")
        self.assertEqual(names, ['Jack', 'Kate', 'Mike', 'Ross', 'Tom'])

if __name__ == "__main__":
    unittest.main()

    