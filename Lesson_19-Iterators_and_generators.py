'''Home work for the lesson 19'''

'''Task 1 - Built-in function enumerate:
 Create your own implementation of a built-in function enumerate, named 'with_index', 
 which takes two parameters: 'iterable' and 'start', default is 0.'''

def with_index(iterable, start=0):
    for i, value in enumerate(iterable, start):
        yield i, value

cars = ['Volvo', 'BMW', 'Toyota', 'Ferrari']

for index, car in with_index(cars, start=1):
    print(f"{index}: {car}")


'''Task 2 - Built-in function range: 
Create your own implementation of a built-in function range, named in_range(), 
which takes three parameters: 'start', 'end', and optional step.'''

def in_range(start, end, step=1):
    current_position = start
    while current_position < end if step > 0 else current_position > end:
        yield current_position
        current_position += step

for i in in_range(1, 10, 2):
    print(i)


'''Task 3 - Custom iterable:
Create your own implementation of an iterable, which could be used inside for-in loop. 
Also, add logic for retrieving elements using square brackets syntax.'''

class MyIterable:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.data):
            value = self.data[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

    def __getitem__(self, index):
        return self.data[index]


my_iterable = MyIterable([6, 17, 32, 189])

for item in my_iterable:
    print(item)

print(my_iterable[1])
print(my_iterable[3])
