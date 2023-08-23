'''Home work for the lesson 20'''

'''Task 1 - Unit tests:
Pick your solution to one of the exercises in this module. 
Design tests for this solution and write tests using unittest library. '''

import unittest
from datetime import datetime, timedelta

class Airport:
    def __init__(self, airport_name, airport_type, airport_operator, location, time_zone):
        self.airport_name = airport_name
        self.airport_type = airport_type
        self.airport_operator = airport_operator
        self.location = location
        self.time_zone = time_zone
    
    def airport_info(self):
        return f'{self.airport_name} is a {self.airport_type} airport. Located in {self.location}'
    
    def destination_point_time(self, departure_time, flight_duration, destination_time_zone):
        time_zone_difference = destination_time_zone - self.time_zone
        arrival_time = departure_time + flight_duration + time_zone_difference
        arrival_time_formatted = arrival_time.strftime("%H:%M")
        return arrival_time_formatted
    
class TestAirport(unittest.TestCase):
    
    def setUp(self):
        self.Dallas_Airport = Airport("Dallas Airport", "International", "Fort Worth International Airport Board", "Dallas, Texas, USA", timedelta(hours=-6))
        self.Miami_Airport = Airport("Miami International Airport", "International", "Miami-Dade Aviation Department", "Miami, Florida, USA", timedelta(hours=-5))
    
    def test_airport_info(self):
        self.assertEqual(self.Dallas_Airport.airport_info(), 'Dallas Airport is a International airport. Located in Dallas, Texas, USA')
        self.assertEqual(self.Miami_Airport.airport_info(), 'Miami International Airport is a International airport. Located in Miami, Florida, USA')
    
    def test_destination_point_time(self):
        self.assertEqual(self.Dallas_Airport.destination_point_time(datetime.strptime('16:00', '%H:%M'), timedelta(hours=3), timedelta(hours=-2)), '23:00')

if __name__ == '__main__':
    unittest.main()


'''Task 2 - Phonebook application testing: 
Write tests for the Phonebook application, which you have implemented in module 1. 
Design tests for this solution and write tests using unittest library'''


import json
import os
import unittest

def add_new_entry(phone_book_path, new_entry):
    # Add the new entry to the phone book
    with open(phone_book_path, "r") as json_file:
        read_json = json.load(json_file)
    
    read_json.append(new_entry)
    
    with open(phone_book_path, "w") as json_file:
        json.dump(read_json, json_file, indent=4)

    
def search_by_full_name(data, first_name, last_name):
    return [item for item in data if item['first_name'] == first_name and item['last_name'] == last_name]

def search_by_phone_number(data, phone_number):
    return [item for item in data if item['telephone_number'] == phone_number]

    

class TestPhoneBookAddEntry(unittest.TestCase):

    def setUp(self):
        # Create a temporary copy of the phone book JSON for testing
        self.phone_book_path = 'test_phone_book.json'
        self.original_phone_book = [
    {
        "first_name": "Olivia",
        "last_name": "Johnson",
        "telephone_number": "647-748-8602",
        "city": "Chicago",
        "state": "IL"
    },
    {
        "first_name": "David",
        "last_name": "Wilson",
        "telephone_number": "315-423-1326",
        "city": "Houston",
        "state": "TX"
    }
        ]
        
        with open(self.phone_book_path, 'w') as json_file:
            json.dump(self.original_phone_book, json_file, indent=4)

    def tearDown(self):
        # Remove the temporary phone book JSON after testing
        if os.path.exists(self.phone_book_path):
            os.remove(self.phone_book_path)

    def test_add_new_entry(self):
        new_entry = {
            "first_name": "Matthew",
            "last_name": "Brown",
            "telephone_number": "725-356-8421",
            "city": "Seattle",
            "state": "WA"
        }

        add_new_entry(self.phone_book_path, new_entry)

        # Check if the new entry is properly added
        with open(self.phone_book_path, 'r') as json_file:
            updated_phone_book = json.load(json_file)

        self.assertIn(new_entry, updated_phone_book)

    def test_search_by_full_name(self):  
        with open(self.phone_book_path, 'r') as json_file:
            updated_phone_book = json.load(json_file)
        search_result = search_by_full_name(updated_phone_book, "David", "Wilson")
        expected_result = [{
        "first_name": "David",
        "last_name": "Wilson",
        "telephone_number": "315-423-1326",
        "city": "Houston",
        "state": "TX"
        }]

        self.assertEqual(search_result, expected_result)

    def test_search_by_phone_number(self):
        with open(self.phone_book_path, 'r') as json_file:
            updated_phone_book = json.load(json_file)
        search_by_phone_number_result = search_by_phone_number(updated_phone_book, '647-748-8602')
        
        expected_result = [{
        "first_name": "Olivia",
        "last_name": "Johnson",
        "telephone_number": "647-748-8602",
        "city": "Chicago",
        "state": "IL"
        }]

        self.assertEqual(search_by_phone_number_result, expected_result)

    def test_delete_record(self):
        with open(self.phone_book_path, 'r') as json_file:
            current_phone_book = json.load(json_file)

        delete_record = [item for item in current_phone_book if item['first_name'] == 'Olivia' and item['last_name'] == 'Johnson']
        current_phone_book.remove(delete_record[0])
        with open(self.phone_book_path, "w") as json_file:
            json.dump(current_phone_book, json_file, indent=4)
            
        self.assertNotIn(delete_record, current_phone_book)


if __name__ == '__main__':
    unittest.main()
