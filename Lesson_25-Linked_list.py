'''Lesson 25 - practice'''

import array

my_array = array.array('u', ['a','b','c','d'])
print(my_array[1])


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_element(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next_node:
                current_node = current_node.next_node
            current_node.next_node = new_node

    def remove_element(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next_node
            return

        current_node = self.head
        while current_node.next_node:
            if current_node.next_node.data == data:
                current_node.next_node = current_node.next_node.next_node
                return 
            current_node = current_node.next_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next_node
        print("None")
        
    def display_reverse(self):
        current_node = self.head
        all_nodes = []
        while current_node:
            all_nodes.append(current_node.data)
            current_node = current_node.next_node
            
        while all_nodes:
            print(all_nodes.pop())
            
        print("None")    


my_linked_list = LinkedList()

my_linked_list.add_element(1)
my_linked_list.add_element(2)
my_linked_list.add_element(3)
my_linked_list.add_element(4)


print("Linked List:")
my_linked_list.display()

my_linked_list.remove_element(2)

print("Linked List after remove:")
my_linked_list.display()

print("Linked List reverce:")
my_linked_list.display_reverse()


'''Home work for the lesson 25'''

'''Task 1 - Implement append, index, pop, insert methods for UnorderedList. 
Also implement a slice method, which will take two parameters 'start' and 'stop', 
and return a copy of the list starting at the position and going up to but not including the stop position.'''


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class UnorderedList:
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_node(self, item):
        add_new_node = Node(item)
        add_new_node.next = self.head
        self.head = add_new_node
    
    def append(self, item):
        self.add_node(item)

    def remove_node(self, item):
            current_node = self.head
            previous_node = None
            found = False
            while not found:
                if current_node.data == item:
                    found = True
                else:
                    previous_node = current_node
                    current_node = current_node.next

            if previous_node is None:
                self.head = current_node.next
            else:
                previous_node.next = current_node.next

    def list_size(self):
        current_node = self.head
        count = 0
        while current_node is not None:
            count += 1
            current_node = current_node.next
        return count

    def search_item(self, item):
        current_node = self.head
        found = False
        while current_node is not None and not found:
            if current_node.data == item:
                found = True
            else:
                current_node = current_node.next
        return found

    
    def index(self, item):
        current_node = self.head
        index = 0
        found = False
        while current_node is not None and not found:
            if current_node.data == item:
                found = True
            else:
                current_node = current_node.next
                index += 1
        if found:
            return index
        else:
            raise ValueError(f"{item} not in list")

    def pop(self, pos=None):
        if self.is_empty():
            raise IndexError("pop from empty list")

        if pos is None:
            pos = self.list_size() - 1

        if pos < 0 or pos >= self.list_size():
            raise IndexError("pop index out of range")

        if pos == 0:
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item
        else:
            current = self.head
            previous = None
            index = 0
            while index < pos:
                previous = current
                current = current.next
                index += 1
            popped_item = current.data
            previous.next = current.next
            return popped_item

    def insert(self, pos, item):
        if pos < 0 or pos > self.list_size():
            raise IndexError("insert index out of range")

        if pos == 0:
            self.add_node(item)
        else:
            current = self.head
            previous = None
            index = 0
            while index < pos:
                previous = current
                current = current.next
                index += 1
            new_node = Node(item)
            new_node.next = current
            previous.next = new_node

    def slice_list(self, start_slice, stop_slice):
        if start_slice < 0 or stop_slice < 0 or start_slice >= stop_slice or stop_slice > self.list_size():
            raise ValueError("Invalid slice parameters")

        new_list = UnorderedList()
        current = self.head
        index = 0

        while index < start_slice:
            current = current.next
            index += 1

        while index < stop_slice:
            new_list.append(current.data)
            current = current.next
            index += 1

        return new_list



unordered_list = UnorderedList()

unordered_list.add_node(1)
unordered_list.add_node(2)
unordered_list.add_node(3)
unordered_list.add_node(4)
unordered_list.add_node(5)

unordered_list.append(6)
print('index(5): ', unordered_list.index(5))
print('pop(): ', unordered_list.pop())
print('List size: ', unordered_list.list_size())

unordered_list.insert(1, 2)
print('List size + insert(1, 2): ',unordered_list.list_size())

sliced_list = unordered_list.slice_list(1, 4)
print('List size + slice(1, 4)', sliced_list.list_size())
