# Exercise 1: Online Store Inventory Management
# Create a class hierarchy to represent an online store's inventory management system. 
#Start with a base class called Product and include attributes such as name, price, 
#and quantity. Create subclasses for specific types of products, such as Electronics, 
#Clothing, and Books. Each subclass should have additional attributes and methods specific to the 
#type of product. Implement methods for adding new products, updating quantities, and calculating total inventory value.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy_product(self):
        return f"You have bought {self.quantity} {self.name}, price = {self.price}$\n"

    def change_the_name(self, new_name):
        return f"The new name of the product {self.name} = {new_name}\n"

    def change_the_price(self, new_price):
        return f"The new price of product {self.name} = {new_price}\n"

    def change_the_quantity(self, new_quantity):
        return f"The new quantity of product {self.name} = {new_quantity}\n"


product = Product("tv", 100, 10)
print(product.change_the_name("blender"))
print(product.change_the_quantity(7))
print(product.change_the_price(15))


class Electronic(Product):
    def __init__(self, name, price, quantity, pc):
        super().__init__(name, price, quantity)
        self.pc = pc

    def add_guarantee(self):
        final_price = self.price * 1.05
        return f"The final price of your {self.name} is {final_price}\n"


electronic = Electronic("Asus", 20000, 6, "G7")
print(electronic.add_guarantee())


class Clothing(Product):
    def __init__(self, name, price, quantity, color):
        super().__init__(name, price, quantity)
        self.color = color

    def refund(self, refund_amount):
        if refund_amount == 1:
            return f"{refund_amount} of {self.color} {self.name} was returned\n"
        else:
            return f"{refund_amount} of {self.color} {self.name}s were returned\n"


clothes = Clothing("T-shirt", 10, 1, "blue")
print(clothes.buy_product())
print(clothes.refund(2))


class Books(Product):
    def __init__(self, name, price, quantity, rating):
        super().__init__(name, price, quantity)
        self.rating = rating

    def review(self):
        return f"The rating of a book {self.name} is {self.rating} / 10"


books = Books("Harry Pother", 10, 14, 9)
print(books.review())


# Exercise 2: Employee Management System
# Design a class hierarchy to represent an employee management system for a company. 
#Start with a base class called Employee and include attributes such as name, 
#position, and salary. Create subclasses for different types of employees, 
#such as Manager, Developer, and Salesperson. Each subclass should have additional 
#attributes and methods specific to the role of the employee. Implement methods for 
#calculating salary bonuses, tracking attendance, and generating employee reports.

class Employee:
    def __init__(self, name, position, salary, days_attended):
            self.name = name
            self.position = position
            self.salary = salary
            self.days_attended = days_attended

    def employee_reports(self):
        print(f'Name: {self.name} \nPosition: {self.position} \nSalary per year: {self.salary}')

    def tracking_attendance(self, days_attended):
        if days_attended < 20:
            print(f'{self.name} has low work attendance!')
        else:
            print(f'{self.name} has a great work attendance!')
    

class Manager(Employee):
    def __init__(self, name, position, salary, days_attended, current_projects):
        super().__init__(name, position, salary, days_attended)
        self.current_projects = current_projects

    def work_load(self):
        print(f'He currently has {self.current_projects} projects')

    def salary_bonuses(self):
        if self.current_projects > 3:
            salary_bonuse = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonuse}')


class Developer(Employee):
    def __init__(self, name, position, salary, days_attended, tech_stack):
        super().__init__(name, position, salary, days_attended)
        self.tech_stack = tech_stack

    def full_tech_stack(self):
        print(f'This is {self.name}, he is a {self.position}. His tech stack is:')
        for item in self.tech_stack:
            print(item)

    def salary_bonuses(self):
        if len(self.tech_stack) >= 5:
            salary_bonuse = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonuse}')

class Salesperson(Employee):
    def __init__(self, name, position, salary, days_attended, amount_of_leads, revenue):
        super().__init__(name, position, salary, days_attended)
        self.amount_of_leads = amount_of_leads
        self.revenue = revenue

    def avg_revenue_per_lead(self):
        avg_revenue = self.revenue / self.amount_of_leads
        print(f'For {self.name}: Avarage revenue per lead is {round(avg_revenue, 2)} $')

    def salary_bonuses(self):
        if self.revenue > 150000:
            salary_bonuse = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonuse}')

manager = Manager('Adam', 'PM', 71000, 25, 4)
manager.employee_reports()
manager.work_load()
manager.salary_bonuses()

developer = Developer('Tom', 'Python Developer', 92000, 23, ['HTML', 'CSS', 'AJAX', 'jQuery', 'Django'])
developer.employee_reports()
developer.full_tech_stack()
developer.salary_bonuses()

salesperson = Salesperson('John', 'Salesperson', 55000, 24, 18, 354000)
salesperson.employee_reports()
salesperson.avg_revenue_per_lead()
salesperson.salary_bonuses()

# Exercise 3: Library Management System
# Create a class hierarchy to represent a library management system. Start with a base class 
#called LibraryItem and include attributes such as title, author, and available. 
#Create subclasses for specific types of items, such as Book, DVD, and Magazine. 
#Each subclass should have additional attributes and methods specific to the type of item. 
#Implement methods for checking out and returning items, generating overdue item reports, 
#and searching for items by title or author.

class LibraryItem:
    def __init__(self, title, author, available):
            self.name = title
            self.position = author
            self.salary = available


    def employee_reports(self):
        print(f'Name: {self.name} \nPosition: {self.position} \nSalary per year: {self.salary}')

    def tracking_attendance(self, days_attended):
        if days_attended < 20:
            print(f'{self.name} has low work attendance!')
        else:
            print(f'{self.name} has a great work attendance!')
    

class Manager(LibraryItem):
    def __init__(self, name, position, salary, days_attended, current_projects):
        super().__init__(name, position, salary, days_attended)
        self.current_projects = current_projects

    def work_load(self):
        print(f'He currently has {self.current_projects} projects')

    def salary_bonuses(self):
        if self.current_projects > 3:
            salary_bonuse = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonuse}')


class Developer(LibraryItem):
    def __init__(self, name, position, salary, days_attended, tech_stack):
        super().__init__(name, position, salary, days_attended)
        self.tech_stack = tech_stack

    def full_tech_stack(self):
        print(f'This is {self.name}, he is a {self.position}. His tech stack is:')
        for item in self.tech_stack:
            print(item)

    def salary_bonuses(self):
        if len(self.tech_stack) >= 5:
            salary_bonuse = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonuse}')

class Salesperson(LibraryItem):
    def __init__(self, name, position, salary, days_attended, amount_of_leads, revenue):
        super().__init__(name, position, salary, days_attended)
        self.amount_of_leads = amount_of_leads
        self.revenue = revenue

    def avg_revenue_per_lead(self):
        avg_revenue = self.revenue / self.amount_of_leads
        print(f'For {self.name}: Avarage revenue per lead is {round(avg_revenue, 2)} $')

    def salary_bonuses(self):
        if self.revenue > 150000:
            salary_bonuse = self.salary * .5
            print(f'{self.name} salary_bonuses is: {salary_bonuse}')


# Exercise 4: Banking System
# Design a class hierarchy to represent a banking system. Start with a base class called Account 
#and include attributes such as account_number, balance, and interest_rate. 
#Create subclasses for different types of accounts, such as SavingsAccount, 
#CheckingAccount, and LoanAccount. Each subclass should have additional attributes and methods 
#specific to the type of account. Implement methods for depositing and withdrawing funds, 
#calculating interest, and generating account statements.

class Account:
    def __init__(self, account_number, balance, interest_rate):
        self.account_number = account_number
        self.balance = balance
        self.interest_rate = interest_rate

    def account_info(self):
        return self.account_number, self.balance


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate, saving_period):
        super().__init__(account_number, balance, interest_rate)
        self.saving_period = saving_period

    def calculate_profits(self):
        return f'This account has avarage monthly interest rate of {self.interest_rate}%. With the saving period of {self.saving_period} months a client will receive: {self.interest_rate * self.saving_period}$'


class CheckingAccount(Account):
    def __init__(self, account_number, balance, interest_rate, min_check):
        super().__init__(account_number, balance, interest_rate)
        self.min_check = min_check

    def check_validation(self, withdrawal_amount):
        if withdrawal_amount >= self.min_check and withdrawal_amount <= self.balance:
            return f'{withdrawal_amount}$ have been withdrawn from your accoun. Current account balance is - {self.balance - withdrawal_amount}$'
        else:
            return 'The withdrawal sum is either too small or too big'

class LoanAccount(Account):
    def __init__(self, account_number, balance, loan_interest_rate, loan_period):
        super().__init__(account_number, balance, interest_rate=0)
        self.loan_interest_rate = loan_interest_rate
        self.loan_period = loan_period

    def calculate_bank_profit(self, borrowed_amount):
        return f'On the loan of {borrowed_amount}$ for the period of {self.loan_period} months, the bank will receive {borrowed_amount * (self.loan_period * self.loan_interest_rate / 100)}$ of profit'

a = Account(1111, 1000, 10)
print(a.account_info())

b = SavingsAccount(2222, 2000, 5, 12)
print(b.calculate_profits())

c = CheckingAccount(33333, 3450, 7, 80)
print(c.check_validation(10))

d = LoanAccount(5555, 4500, 8, 5)
print(d.calculate_bank_profit(1500))

# Exercise 5: Flight Booking System
# Create a class hierarchy to represent a flight booking system for an airline. 
#Start with a base class called Flight and include attributes such as flight_number, 
#departure, and arrival. Create subclasses for different types of flights, 
#such as DomesticFlight and InternationalFlight. Each subclass should have additional 
#attributes and methods specific to the type of flight. Implement methods for booking seats, 
#checking flight availability, and generating passenger manifests.

class Flight:

    def __init__(self, flight_number, departure, arrival, number_of_seats, seat_availability):
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.number_of_seats = number_of_seats
        self.seat_availability = seat_availability

    def generating_passenger_manifests(self):
        return f'Flight number {self.flight_number} departure at {self.departure}, arrival at {self.arrival}'


class DomesticFlight(Flight):
    def __init__(self, flight_number, departure, arrival, number_of_seats, seat_availability):
        super().__init__(flight_number, departure, arrival, number_of_seats, seat_availability)

    available_domestic_airports = ['Miami', 'Houston', 'New York', 'Chicago']
    def get_domestic_airports(self, destination_city):
        if destination_city in self.available_domestic_airports:
            return f'You can book a ticket to the {destination_city}'
        else:
            return f'{destination_city} is not available as your destination point. Here is a list of available domestic airports: {self.available_domestic_airports}'



class InternationalFlight(Flight):
    def __init__(self, flight_number, departure, arrival, number_of_seats, seat_availability, baggage_fee):
        super().__init__(flight_number, departure, arrival, number_of_seats, seat_availability)
        self.baggage_fee = baggage_fee

    def calculate_baggage_fee(self, baggage_weight):
        if baggage_weight < 5:
            return 'No baggage fee applied'
        elif 5 <= baggage_weight <= 20:
            return f'Your baggage fee is: {self.baggage_fee}%'
        else:
            return 'Baggage weight limit is exceeded'



def checking_flight_availability(flight):
    return f'{flight.seat_availability} seats are still available.'


def booking_seats(flight):
    return 'You have successfully booked 1 seat' if flight.seat_availability > 0 else 'There are no available seats on this flight'


domestic_flight = DomesticFlight(1111, '12-00', '18-30', 42, 18)
international_flight = InternationalFlight(222, '9-00', '15-40', 32, 9, 3)

print(checking_flight_availability(domestic_flight))
print(booking_seats(international_flight))

print(domestic_flight.get_domestic_airports('Seattle'))
print(international_flight.calculate_baggage_fee(18))
