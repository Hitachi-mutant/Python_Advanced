'''Home work for the lesson 15'''

'''Task 1 - A Person class:
 Make a class called Person. Make the __init__() method take firstname, 
 lastname, and age as parameters and add them as attributes. 
 Make another method called talk() which makes prints a greeting from the person 
 containing, for example like this: "Hello, my name is Carl Johnson and I’m 26 years old".'''
class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old")
call_class = Person("Tony", "Soprano", 44)
call_class.talk()


'''Task 2 - Doggy age: 
Create a class Dog with class attribute 'age_factor' equals to 7. 
Make __init__() which takes values for a dog’s age. Then create a method `human_age` 
which returns the dog’s age in human equivalent.'''

class Dog:
    age_factor = 7
    def __init__(self, dogs_age):
        self.dogs_age = dogs_age
    def human_age(self):
        print(f'If your dog is {self.dogs_age} years old, it means that he/she is {self.dogs_age * self.age_factor} in dog-years')
call_class = Dog(4)
call_class.human_age()


'''Task 3 - TV controller:
Create a simple prototype of a TV controller in Python. It’ll use the following commands:'''
# first_channel() - turns on the first channel from the list.
# last_channel() - turns on the last channel from the list.
# turn_channel(N) - turns on the N channel. Pay attention that the channel numbers start from 1, not from 0.
# next_channel() - turns on the next channel. If the current channel is the last one, turns on the first channel.
# previous_channel() - turns on the previous channel. If the current channel is the first one, turns on the last channel.
# current_channel() - returns the name of the current channel.
# is_exist(N/'name') - gets 1 argument - the number N or the string 'name' and returns "Yes", 
# if the channel N or 'name' exists in the list, or "No" - in the other case.

default_channel = 1
class TVController:

    def __init__(self, CHANNELS):
        self.CHANNELS = CHANNELS

    def first_channel(self, CHANNELS):
        print(self.CHANNELS[0])

    def last_channel(self, CHANNELS):
        print(self.CHANNELS[-1])

    def turn_channel(self, n):
        print(self.CHANNELS[n-1])
    
    def next_channel(self, channel = default_channel):
        for ch in self.CHANNELS:
            if ch == self.CHANNELS[channel]:
                    print(ch)
                    break

    def previous_channel(self, channel = default_channel):
        for ch in self.CHANNELS:
            if ch == self.CHANNELS[channel - 1]:
                    print(ch)
                    break

    def current_channel(self, default_channel):
            print(self.CHANNELS[default_channel - 1])

    def is_exist(self, channel):
        if channel not in CHANNELS:
            print('No')
        for ch in self.CHANNELS:
            if ch == channel:
                    print('Yes')
                    break

CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

controller.first_channel(CHANNELS)
controller.last_channel(CHANNELS)
controller.turn_channel(1)
controller.next_channel(default_channel)
controller.previous_channel(default_channel)
controller.current_channel(default_channel)
controller.is_exist(4)
controller.is_exist("BBC")
