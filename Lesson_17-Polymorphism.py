'''Home work for the lesson 17'''

'''Task 1 - Method overloading:
Create a base class named Animal with a method called talk and then create two subclasses: Dog and Cat, 
and make their own implementation of the method talk be different. For instance, 
Dog’s can be to print ‘woof woof’, while Cat’s can be to print ‘meow’.'''

class Animal:
    def talk(self, sound):
        return sound

class Dog(Animal):
    def talk_dog(self, dog_sound):
        return super().talk(dog_sound)

class Cat(Animal):
    def talk_cat(self, cat_sound):
        return super().talk(cat_sound)

dog = Dog()
cat = Cat()

print(dog.talk_dog("Woof!"))
print(cat.talk_cat("Meow!"))


'''Task 2 - Library:
Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []
Library class Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book class and 
adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year
All 3 classes must have a readable __repr__ and __str__ methods.
Also, the book class should have a class variable which holds the amount of all existing books'''

class Library:
    def __init__(self, book_name, all_lib_books = [], authors = []):
        self.book_name = book_name
        self.books = all_lib_books
        self.authors = authors


class Book(Library):
    def __init__(self, book_name, year, author):
        super().__init__(book_name)
        self.year = year
        self.author = author



class Author(Library):
    def __init__(self, authors_name, country, birthday, authors_books = []):
        self.authors_name = authors_name
        self.country = country
        self.birthday = birthday
        self.authors_books = authors_books


'''Task 3 - Fraction:
Створіть клас Fraction, який буде представляти всю базову арифметичну логіку для дробів (+, -, /, *) 
з належною перевіркою й обробкою помилок. Потрібно додати магічні методи для математичних 
операцій та операції порівняння між об'єктами класу Fraction'''

class Fraction:
    def __init__(self, numerator=0, denominator=1):
        if denominator == 0:
            raise ValueError('Denominator cannot be zero.')
        gcd_value = self._gcd(numerator, denominator)
        self.numerator = numerator // gcd_value
        self.denominator = denominator // gcd_value

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        else:
            return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError('Unsupported operand type for "+"')
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError('Unsupported operand type for "-"')
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError('Unsupported operand type for "*"')
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError('Unsupported operand type for "/"')
        if other.numerator == 0:
            raise ValueError("Division by zero is not allowed.")
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            return False
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, int):
            other = Fraction(other, 1)
        if not isinstance(other, Fraction):
            raise TypeError('Unsupported operand type for "<"')
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return not self.__lt__(other)

    # calculating greatest common divisor
    def _gcd(self, a, b): 
        while b != 0:
            a, b = b, a % b
        return a


# if __name__ == "__main__": # This block is in the condition of the task. IDK what for.
x = Fraction(1, 2)
y = Fraction(1, 4)

print(x + y)   # Output: 3/4
print(x - y)   # Output: 1/4
print(x * y)   # Output: 1/8
print(x / y)   # Output: 2/1
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x < y)   # Output: False
print(x <= y)  # Output: False
print(x > y)   # Output: True
print(x >= y)  # Output: True
