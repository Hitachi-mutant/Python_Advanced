'''Home work for the lesson 26'''

'''Task 1 - Implement a binary search algorithm using recursion.
Read about Fibonacci search and implement it using Python. 
Define the complexity of the algorithm and compare it to binary search'''

# Binary search algorithm - Complexity: O(log n)
def binary_search_recursive(input_data, target, left, right):
    middle_index = (left + right) // 2
    if left > right:
        return 'not in the array'

    if input_data[middle_index] == target:
        return middle_index
    elif input_data[middle_index] < target:
        return binary_search_recursive(input_data, target, middle_index + 1, right)
    else:
        return binary_search_recursive(input_data, target, left, middle_index - 1)

input_data = [43, 16, 4, 87, 159, 4, 32]
target1 = 16
target2 = 8
result1 = binary_search_recursive(input_data, target1, 0, len(input_data) - 1)
print(f"Index of the element {target1} is {result1}")
result2 = binary_search_recursive(input_data, target2, 0, len(input_data) - 1)
print(f"Index of the element {target2} is {result2}")


# Fibonacci search using Python - Complexity: O(log n)
    
def fibonacci_search(input_data, target):
    n = len(input_data)
    def generate_fibonacci_sequence(n):
        fibonacci_sequence = [0, 1]
        while fibonacci_sequence[-1] < n:
            next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_fibonacci)
        return fibonacci_sequence

    fibonacci_sequence = generate_fibonacci_sequence(n)
    offset = -1
    
    while fibonacci_sequence[offset] >= 0:
        i = min(offset + fibonacci_sequence[offset], n - 1)

        if input_data[i] < target:
            offset -= 1
        elif input_data[i] > target:
            offset -= 2
        else:
            return i  

    return False 


input_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 10
result = fibonacci_search(input_data, target)

if result:
    print(f"Fibonacci search: Element {target} has index {result}")
else:
    print(f"Fibonacci search: Element {target} not found")
