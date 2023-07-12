'''Home work for the lesson 14'''

'''Task 1 - Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!'''

def print_the_function(original_function):
    def wrapper_func(*args):
        return print(f"Calling function '{original_function.__name__}' with arguments: {args}")
    return wrapper_func

@print_the_function
def working_function(*args):
    return sum(args)

@print_the_function
def square_all(*args):
    return [arg ** 2 for arg in args]

working_function('a','b','c')
square_all(2,3,4)


'''Task 2 - Write a decorator that takes a list of stop words and replaces them with * inside the decorated function'''

def stop_words(words: list):
    def outer_function(original_function):
        def wrapper(string_arg):
                result = original_function(string_arg)
                for word in words:
                    result = result.replace(word, "*")
                return result
        return wrapper
    return outer_function
 
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

print(create_slogan("Steve"))


'''Task 3 - Write a decorator "arg_rules" that validates arguments passed to the function.'''
# max_length: 15
# type_: str
# contains: [] - list of symbols that an argument should contain

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator_func(original_func):
        def wrapper(string_arg): 
            if type(string_arg) == type_ and len(string_arg) < max_length and all(item in string_arg for item in contains):
                execute_func = original_func(string_arg)
                print(execute_func)
                return execute_func
            else: 
                print(False)
                return False
        return wrapper
    return decorator_func

@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

#assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
create_slogan('S@SH05')
#assert create_slogan('johndoe05@gmail.com') is False
create_slogan('johndoe05@gmail.com')
