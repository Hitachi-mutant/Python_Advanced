'''Home work for the lesson 23'''

from typing import List, Tuple



'''Task 1 - Match big O complexities with the code snippets below'''

# We assume that all lists passed to functions are the same length N
# answers 
# 1 - n
# 2 - 1
# 3 - n^2
# 4 - n
# 5 - n^2
# 6 - log n


# Matching
def question1(first_list: List[int], second_list: List[int]) -> List[int]: # O(n^2) 
    res: List[int] = []
    for el_first_list in first_list: # loop that iterates through the first_list and performs a lookup operation in second_list.
        if el_first_list in second_list:
            res.append(el_first_list)
    return res

def question2(n: int) -> int: # O(1)
	for _ in range(10): # loop that performs a constant number of operations (raising n to the power of 3) 
		n **= 3
	return n

def question3(first_list: List[int], second_list: List[int])-> List[int]: # O(n^2) 
   temp: List[int] = first_list[:]
   for el_second_list in second_list: # nested loops
      flag = False
      for check in temp:
         if el_second_list == check:
            flag = True
            break
      if not flag:
         temp.append(second_list)
   return temp


def question4(input_list: List[int]) -> int: # O(n)
  res: int = 0
  for el in input_list: # loop that iterates through input_list once, finding the maximum element.
    if el > res:
      res = el
  return res
 

def question5(n: int) -> List[Tuple[int, int]]: # O(n^2) 
    res: List[Tuple[int, int]] = []
    for i in range(n): # outer loop iterates n times, and for each iteration, the inner loop also iterates n times. 
        for j in range(n):
            res.append((i, j))
    return res


def question6(n: int) -> int: # O(log n)
    while n > 1: # number of iterations required is proportional to the logarithm of n
        n /= 2
    return n