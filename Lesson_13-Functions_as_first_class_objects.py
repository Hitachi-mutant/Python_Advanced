'''Home work for the lesson 13'''

'''Task 1 - Write a Python program to detect the number of local variables declared in a function.'''

def local_variables_func(*args):    
    return print("Local variables:", locals())

local_variables_func('a', True, 8)


'''Task 2 - Write a Python program to access a function inside a function 
(Tips: use function, which returns another function)'''

def outer_function(*args):
    filter_args = [item for item in args if item % 2 == 0]
    def inner_function(arg):
        result_output = [item * arg for item in filter_args]
        return result_output
    return inner_function

variable_for_our_funcs = outer_function(3, 10, 7, 9, 4)
print(variable_for_our_funcs(5))

'''Task 3 - Write a function called "choose_func" which takes a list of nums and 2 callback functions. 
If all nums inside the list are positive, execute the first function on that list and return the result of it. 
Otherwise, return the result of the second one'''

def choose_func(nums: list, func1, func2):
    for num in nums:
            if num <= 0:
                return func2(nums)
    return func1(nums)

nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]

if choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]: 
    print(square_nums(nums1))
if choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]:
     print(remove_negatives(nums2))