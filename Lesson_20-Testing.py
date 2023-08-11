'''Home work for the lesson 20'''

'''Task 1 - Unit tests:
Pick your solution to one of the exercises in this module. 
Design tests for this solution and write tests using unittest library. '''

# import unittest
# from datetime import datetime, timedelta

# class Airport:
#     def __init__(self, airport_name, airport_type, airport_operator, location, time_zone):
#         self.airport_name = airport_name
#         self.airport_type = airport_type
#         self.airport_operator = airport_operator
#         self.location = location
#         self.time_zone = time_zone
    
#     def airport_info(self):
#         return f'{self.airport_name} is a {self.airport_type} airport. Located in {self.location}'
    
#     def destination_point_time(self, departure_time, flight_duration, destination_time_zone):
#         time_zone_difference = destination_time_zone - self.time_zone
#         arrival_time = departure_time + flight_duration + time_zone_difference
#         arrival_time_formatted = arrival_time.strftime("%H:%M")
#         return arrival_time_formatted
    
# class TestAirport(unittest.TestCase):
    
#     def setUp(self):
#         self.Dallas_Airport = Airport("Dallas Airport", "International", "Fort Worth International Airport Board", "Dallas, Texas, USA", timedelta(hours=-6))
#         self.Miami_Airport = Airport("Miami International Airport", "International", "Miami-Dade Aviation Department", "Miami, Florida, USA", timedelta(hours=-5))
    
#     def test_airport_info(self):
#         self.assertEqual(self.Dallas_Airport.airport_info(), 'Dallas Airport is a International airport. Located in Dallas, Texas, USA')
#         self.assertEqual(self.Miami_Airport.airport_info(), 'Miami International Airport is a International airport. Located in Miami, Florida, USA')
    
#     def test_destination_point_time(self):
#         self.assertEqual(self.Dallas_Airport.destination_point_time(datetime.strptime('16:00', '%H:%M'), timedelta(hours=3), timedelta(hours=-2)), '23:00')

# if __name__ == '__main__':
#     unittest.main()


'''Task 2 - Phonebook application testing: 
Write tests for the Phonebook application, which you have implemented in module 1. 
Design tests for this solution and write tests using unittest library'''

import unittest    # already imported in the first task
import json
from Lesson_11_Working_with_files import add_new_entry, search_by_first_name, search_by_last_name, search_by_full_name

class TestPhoneBook(unittest.TestCase):

    def setUp(self):
        # Load a sample phone book JSON
        self.phone_book_path = 'Lesson_11_Working_with_files/phone_book.json'
        with open(self.phone_book_path, "r") as json_file:
            self.sample_phone_book = json.load(json_file)
    
    def test_add_new_entry(self):
        initial_length = len(self.sample_phone_book)
        
        new_entry = {
            "first_name": "Test",
            "last_name": "User",
            "telephone_number": "123-456-7890",
            "city": "Testville",
            "state": "TS"
        }
        
        add_new_entry(self.phone_book_path, new_entry)
        
        with open(self.phone_book_path, "r") as json_file:
            updated_phone_book = json.load(json_file)
        
        updated_length = len(updated_phone_book)
        
        self.assertEqual(updated_length, initial_length + 1)
    
    def test_search_by_first_name(self):
        search_result = search_by_first_name(self.sample_phone_book, "Andrew")
        self.assertTrue(all(entry["first_name"] == "Andrew" for entry in search_result))
    
    def test_search_by_last_name(self):
        search_result = search_by_last_name(self.sample_phone_book, "Taylor")
        self.assertTrue(all(entry["last_name"] == "Taylor" for entry in search_result))

if __name__ == '__main__':
    unittest.main()
