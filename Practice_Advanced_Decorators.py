# 1. Реалізувати декоратор, який перевіряє, чи є аргумент функції числом 
#  та виводить повідомлення про помилку, якщо це не так.

# def decorator_to_check_args(our_function_to_check):
#     def wrapper_function(*args):
#         for element in args:
#             if isinstance(element, str) and element.isdigit():
#                 print(f"{element} is a digit.")
#             elif isinstance(element, int):
#                 print(f"{element} is a digit.")
#             else:
#                 print(f"{element} is not a digit.")
#         result = our_function_to_check(*args)
#         return result
#     return wrapper_function

# @decorator_to_check_args
# def func_with_the_numbers(*args):
#     return args

# output = func_with_the_numbers('a', 1, '2', 0, True, None)
# print(output)


# 2. Написати декоратор, який обмежує кількість разів виклику 
#  функції та видає помилку, якщо ліміт перевищено.

# def decorator(func):
#     calls = 0
#     def wrapper(*args):
#         nonlocal calls
#         calls += 1
#         if calls <= 3:
#             return func(*args)
#         else:
#             print("You can't call your function more than three times.")
#             return None  # Return None when the limit is exceeded

#     return wrapper

# @decorator
# def function(name_1, name_2):
#     return f"{name_1} and {name_2}\n"

# for _ in range(5):
#     result = function("A", "B")
#     print(result)


# 3. Створити декоратор, який змінює результат функції на протилежне значення (наприклад, з True на False).

# def change_func(func_as_arg):
#     def wrapper_function(*args):
#             result = func_as_arg(*args)
#             if result:
#                 return False
#             else: 
#                 return True
#     return wrapper_function

# @change_func
# def my_func(a):
#     if a > 0:
#         return True
#     else: return False

# print(my_func(0))


# 4. Напишіть декоратор, який перевіряє типи аргументів, переданих до функції, 
#  та виводить повідомлення про помилку, якщо типи не відповідають очікуваним.

# def check_arguments(func_as_arg):
#     def wrapper_function(*args):
#         lets_check = func_as_arg(*args)
#         valid_items = []
#         for item in lets_check:
#             if isinstance(item, (bool, int, str, float)):
#                 valid_items.append(item)
#             else:
#                 pass
#         return valid_items
#     return wrapper_function

# @check_arguments
# def function_with_logic(*args):
#     return args

# print_result = function_with_logic(None, True, 1, 's', 7.3, None, '')
# print(print_result)



# 5. Split the string and find the first letter of the word
# def split_str(your_string):
#     for item in your_string.split(" "):
#         print(f"The first letter of the word '{item}', is '{item[0]}'.")

# split_str("hello my name is max")


# 6. Реалізувати функцію, яка буде загорнута в декілька декораторів (декоратори потрібно написати самим)

def decorator_1(func_as_arg): # Remove elements that are > 10
    def wrapper_function(*args):
        filtered_args = tuple(item for item in args if item < 10)
        if filtered_args:
            return func_as_arg(*filtered_args)
        else:
            print("No elements less than 10 found.")
            return None
    return wrapper_function

def decorator_2(func_as_arg):   # Remove elements that are < 3
    def wrapper_function(*args):
        filtered_args = tuple(item for item in args if item > 3)
        if filtered_args:
            return func_as_arg(*filtered_args)
        else:
            print("No elements greater than 3 found.")
            return None
    return wrapper_function

@decorator_1
@decorator_2
def calculate_sum(*args):
    return sum(args)

print(calculate_sum(4, 11, 1, 20, 6))

# 6. Написати декоратор, який всередині буде відловлювати помилку (реалізувати try-except statement)



# 7. Напишіть декоратор, який записує в файл час, коли була викликана функція
