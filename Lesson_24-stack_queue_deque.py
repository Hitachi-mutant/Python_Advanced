'''Home work for the lesson 24'''

'''Task 1 - Write a program that reads in a sequence of characters and 
prints them in reverse order, using your implementation of Stack. '''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

def reverse_string(input_string):
    stack = Stack()
    
    for char in input_string:
        stack.push(char)
    
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    
    return reversed_string

if __name__ == "__main__":
    user_input = input("Enter a sequence of characters: ")
    reversed_result = reverse_string(user_input)
    print("Reversed sequence:", reversed_result)



'''Task 2 - Write a program that reads in a sequence of characters, 
and determines whether it's parentheses, braces, and curly brackets are "balanced."'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

def are_parentheses_balanced(input_string):
    stack = Stack()
    
    for char in input_string:
        if char in "([{":
            stack.push(char)
        elif char in ")]}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if (char == ")" and top != "(") or \
               (char == "]" and top != "[") or \
               (char == "}" and top != "{"):
                return False
    
    return stack.is_empty()

if __name__ == "__main__":
    user_input = input("Enter a sequence of characters: ")
    if are_parentheses_balanced(user_input):
        print("Parentheses, braces, and curly brackets are balanced.")
    else:
        print("Parentheses, braces, and curly brackets are not balanced.")


'''Task 3 - Extend the Stack to include a method called get_from_stack that searches and returns an element e from a stack. 
Any other element must remain on the stack respecting their order. 
Consider the case in which the element is not found - raise ValueError with proper info Message'''

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def get_from_stack(self, target):
        temp_stack = Stack()
        found = False

        while not self.is_empty():
            item = self.pop()
            if item == target:
                found = True
                break
            temp_stack.push(item)

        while not temp_stack.is_empty():
            self.push(temp_stack.pop())

        if found:
            return target
        else:
            raise ValueError(f"{target} not found in the stack")

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    
    try:
        element = stack.get_from_stack(2)
        print(f"Element found and removed: {element}")
    except ValueError as e:
        print(e)
    
    try:
        element = stack.get_from_stack(4)  # Element not in the stack
        print(f"Element found and removed: {element}")
    except ValueError as e:
        print(e)
    
    print("Remaining elements in the stack:", stack.items)
