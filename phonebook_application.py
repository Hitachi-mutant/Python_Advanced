
import json

# Add new entries
phone_book_path = 'Lesson_11_Working_with_files/phone_book.json'

with open(phone_book_path, "r") as json_file:
    read_json = json.load(json_file)

add_new_entry = {
    "first_name": "Matthew",
    "last_name": "Brown",
    "telephone_number": "725-356-8421",
    "city": "Seattle",
    "state": "WA"
}
read_json.append(add_new_entry)

with open(phone_book_path, "w") as json_file:
    json.dump(read_json, json_file, indent=4)

# Search by first name
first_name = 'Andrew'
first_name_search_result = [item for item in read_json if item['first_name'] == first_name]
print('Search by first name: ' + str(first_name_search_result))

# Search by last name
last_name = 'Taylor'
last_name_search_result = [item for item in read_json if item['last_name'] == last_name]
print('Search by last name: ' + str(last_name_search_result))

# Search by full name
first_name = 'David'
last_name = 'Wilson'

full_name_search_result = [item for item in read_json if item['first_name'] == first_name and item['last_name'] == last_name]
print('Search by full name: ' + str(full_name_search_result))

# Search by telephone number
telephone_number = '727-542-4572'
telephone_number_search_result = [item for item in read_json if item['telephone_number'] == telephone_number]
print('Search by telephone number: ' + str(telephone_number_search_result))

# Search by city or state
city = 'San Antonio'
state = 'TX'

city_state_search_result = [item for item in read_json if item['city'] == city or item['state'] == state]
print('Search by city or state: ' + str(city_state_search_result))

# Delete a record for a given telephone number
first_name = 'Sarah'
last_name = 'Davis'

try:
    delete_record = [item for item in read_json if item['first_name'] == first_name and item['last_name'] == last_name]
    read_json.remove(delete_record[0])
    with open(phone_book_path, "w") as json_file:
        json.dump(read_json, json_file, indent=4)
    print('Deleted record: ' + str(delete_record))

except IndexError:
    print('There is no such record in the phone book')

# Update a record for a given telephone number

old_telephone_number = '437-978-8599'
new_telephone_number = '999-999-9999'

for item in read_json:
    if item['telephone_number'] == old_telephone_number:
        item['telephone_number'] = new_telephone_number
        break 


with open(phone_book_path, "w") as json_file:
        json.dump(read_json, json_file, indent=4)

# An option to exit the program
exit_program = input('Would you like to exit the program (y/n)? ')

if exit_program == 'y':
    json_file.close()
else:
    pass