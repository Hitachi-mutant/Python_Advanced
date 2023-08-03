'''Home work for the lesson 18'''

'''Task 1 - Email validator:
Create a class method named `validate`, which should be called from the `__init__` 
method to validate parameter email, passed to the constructor. 
The logic inside the `validate` method could be to check if the passed email 
parameter is a valid email string.'''

import re

class EmailValidator:
    def __init__(self, email):
        self.email = email
        self.validate()

    def validate(self):
        if not self.is_valid_email(self.email):
            raise ValueError("Invalid email format")

    @staticmethod
    def is_valid_email(email):
        email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_pattern, email)


try:
    valid_email = EmailValidator("example@example.com")
    print("Valid email:", valid_email.email)
except ValueError as error:
    print("Error:", error)

try:
    invalid_email = EmailValidator("invalid_email")
    print("Valid email:", invalid_email.email)
except ValueError as error:
    print("Error:", error)



'''Task 2 - Library:
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. 
Each Boss has a list of his own workers. You should implement a method that allows 
you to add workers to a Boss. You're not allowed to add instances of Boss class to 
workers list directly via access to attribute, use getters and setters instead!'''

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self._id = id_
        self._name = name
        self._company = company
        self._workers = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    @property
    def workers(self):
        return self._workers

    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self._workers.append(worker)
        else:
            raise ValueError("Only instances of Worker can be added as workers")

    def __str__(self):
        return f"Boss: ID={self.id}, Name={self.name}, Company={self.company}, Workers={len(self.workers)}"

    def remove_worker(self, worker):
        if worker in self._workers:
            self._workers.remove(worker)

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self._id = id_
        self._name = name
        self._company = company
        self._boss = None  
        self.boss = boss  

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def company(self):
        return self._company

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss class")

    def __str__(self):
        return f"Worker: ID={self.id}, Name={self.name}, Company={self.company}, Boss={self.boss.name}"

    @boss.setter
    def boss(self, new_boss):
        if isinstance(new_boss, Boss):
            if self._boss is not None:
                self._boss.remove_worker(self)
            self._boss = new_boss
            new_boss.add_worker(self)
        else:
            raise ValueError("Boss must be an instance of Boss class")

boss1 = Boss(1, "Boss1", "Company A")
boss2 = Boss(2, "Boss2", "Company B")
boss3 = Boss(3, "Boss3", "Company C")

worker1 = Worker(1, "Worker1", "Company A", boss1)
worker2 = Worker(2, "Worker2", "Company B", boss2)
worker3 = Worker(1, "Worker1", "Company A", boss1)

print(boss1)
print(boss2)
print(boss3)

worker1.boss = boss2
print(boss1)
print(boss2)
print(boss3)


'''Task 3 - Type conversion:
Write a class TypeDecorators which has several methods for converting results of functions to a specified type'''

from functools import wraps

class TypeDecorators:

    @classmethod
    def to_int(cls, func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return int(result)
            except ValueError:
                raise ValueError("Conversion to int failed")
        return wrapper

    @classmethod
    def to_str(cls, func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            return str(result)
        return wrapper

    @classmethod
    def to_bool(cls, func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            if result.lower() == 'true':
                return True
            elif result.lower() == 'false':
                return False
            else:
                raise ValueError("Conversion to bool failed")
        return wrapper

    @classmethod
    def to_float(cls, func):
        @wraps(func)
        def wrapper(*args):
            result = func(*args)
            try:
                return float(result)
            except ValueError:
                raise ValueError("Conversion to float failed")
        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string

@TypeDecorators.to_bool
def do_something(string: str):
    return string

print(do_nothing('25'), type(do_nothing('25')))
print(do_something('True'), type(do_something('True')))
