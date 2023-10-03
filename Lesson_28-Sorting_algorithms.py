'''Home work for the lesson 28'''

'''Task 1 - Підготуйте 2 масиви даних різної довжини. Можете скористатися бібліотекою random 
для генерування елементів списків. Застосуйте 3 на вибір алгоритми сортування на 
кожен з масивів і порівняйте час виконання. Результати можете також помістити в якийсь текстовий файл.'''

import random
import time

def generate_random_array(length):
    return [random.randint(1, 10000) for _ in range(length)]

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key



array1 = generate_random_array(1000)
array2 = generate_random_array(3000)

# Run Bubble Sort
start_time = time.time()
bubble_sort(array1.copy())
end_time = time.time()
bubble_sort_time_1 = end_time - start_time

start_time = time.time()
bubble_sort(array2.copy())
end_time = time.time()
bubble_sort_time_2 = end_time - start_time

# Run Merge Sort 
start_time = time.time()
merge_sort(array1.copy())
end_time = time.time()
merge_sort_time_1 = end_time - start_time

start_time = time.time()
merge_sort(array2.copy())
end_time = time.time()
merge_sort_time_2 = end_time - start_time

# Run Insertion Sort
start_time = time.time()
insertion_sort(array1.copy())
end_time = time.time()
insertion_sort_time_1 = end_time - start_time

start_time = time.time()
insertion_sort(array2.copy())
end_time = time.time()
insertion_sort_time_2 = end_time - start_time

# Записуємо результати у текстовий файл
with open("compare_results.txt", "w") as file:
    file.write("Bubble Sort:\n")
    file.write(f"Array 1 (1000 elements): {bubble_sort_time_1} seconds\n")
    file.write(f"Array 2 (3000 elements): {bubble_sort_time_2} seconds\n")

    file.write("\nMerge Sort:\n")
    file.write(f"Array 1 (1000 elements): {merge_sort_time_1} seconds\n")
    file.write(f"Array 2 (3000 elements): {merge_sort_time_2} seconds\n")

    file.write("\nInsertion Sort:\n")
    file.write(f"Array 1 (1000 elements): {insertion_sort_time_1} seconds\n")
    file.write(f"Array 2 (3000 elements): {insertion_sort_time_2} seconds\n")

print("Результати збережено у файлі compare_results.txt")


'''Task 2 - Дослідіть, які алгоритми застосовані в пайтонівських функціях min(), max() i index().'''

# this is optimized algorithm for min(). Time complexity is O(n)
def min_algorithm(arr):
    if not arr:
        raise ValueError("Iterable is empty")
    
    min_val = arr[0]  # Assume the first element is the minimum
    
    for item in arr:
        if item < min_val:
            min_val = item
    
    return min_val

# this is optimized algorithm for max(). Time complexity is O(n) 
def max_algorithm(arr):
    if not arr:
        raise ValueError("Iterable is empty")
    
    max_val = arr[0]  # Assume the first element is the maximum
    
    for item in arr:
        if item > max_val:
            max_val = item
    
    return max_val

# linear search algorithm similar to what list.index(). Time complexity is O(n)
def custom_index(arr, x):
    for i, item in enumerate(arr):
        if item == x:
            return i
    raise ValueError(f"{x} is not in list")

# Example usage:
my_list = [5, 2, 9, 1, 7, 3]
search_value = 9
try:
    index = custom_index(my_list, search_value)
    print(f"The index of {search_value} in the list is: {index}")
except ValueError as e:
    print(e)
