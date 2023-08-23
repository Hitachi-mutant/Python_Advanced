'''Home work for the lesson 21'''

'''Task 1 - File Context Manager class:
Create your own class, which can behave like a built-in function 'open'. 
Also, you need to extend its functionality with counter and logging. 
Pay special attention to the implementation of '__exit__' method, which has to cover 
all the requirements to context managers mentioned here '''

import logging

class FileHandler_:

    file_counter = 0    # Keep track of how many files are opened

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    @classmethod
    def increment_counter(cls):
        cls.file_counter += 1

    @classmethod
    def decrement_counter(cls):
        cls.file_counter -= 1

# __enter__ method is called when the with block is entered
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        FileHandler_.increment_counter()
        logging.info(f"Opened file '{self.filename}' in mode '{self.mode}'")
        return self.file

# __exit__ method is called when the with block is exited
    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.file.close()
        FileHandler_.decrement_counter()
        logging.info(f"Closed file '{self.filename}'")
        if exc_type is not None:
            logging.error(f"An exception of type {exc_type} occurred: {exc_value}")
        if FileHandler_.file_counter == 0:
            logging.info("All files are closed")


logging.basicConfig(level=logging.INFO)

with FileHandler_("File_Context_Manager_class.txt", "w") as file:
    file.write("It's working!")

with FileHandler_("File_Context_Manager_class.txt", "r") as file:
    content = file.read()
    print(content)


# '''Task 2 - Writing tests for context manager
# Take your implementation of the context manager class from Task 1 and write tests for it. 
# Try to cover as many use cases as you can, positive ones when a file exists and everything works as designed. 
# And also, write tests when your class raises errors or you have errors in the runtime context suite.'''

import unittest
#import logging  # imported in the task 1

class TestFileHandler_(unittest.TestCase):

# test if the file is properly created
    def test_file_creation(self):
        with FileHandler_("test_file.txt", "w") as file:
            self.assertTrue(file is not None)
            # checking if file object created using the FileHandler_ class is an instance of the 
            # same type as an object created using the built-in open() function
            self.assertTrue(isinstance(file, type(open("test_file.txt", "w"))))

# test if error is logged
    def test_error_logging(self):
        with self.assertLogs(level=logging.ERROR):
            with FileHandler_("non_existent_file.txt", "r") as file:
                content = file.read()
            self.assertTrue(content is not None)

# test if counter is properly counting
    def test_file_counter(self):
        initial_counter = FileHandler_.file_counter

        with FileHandler_("test_counter_file1.txt", "w") as file1:
            self.assertEqual(FileHandler_.file_counter, initial_counter + 1)

        with FileHandler_("test_counter_file2.txt", "w") as file2:
            self.assertEqual(FileHandler_.file_counter, initial_counter + 2)

        with FileHandler_("test_counter_file3.txt", "w") as file3:
            self.assertEqual(FileHandler_.file_counter, initial_counter + 3)

        self.assertEqual(FileHandler_.file_counter, initial_counter)

if __name__ == '__main__':
    unittest.main()

'''Task 3 - Pytest fixtures with context manager
Create a simple function, which performs any logic of your choice with text data, 
which it obtains from a file object, passed to this function ( def test(file_obj) ). 

Create a test case for this function using pytest library (Full pytest documentation). 

Create pytest fixture, which uses your implementation of the context manager to return a file object, 
which could be used inside your function.'''

# See this task here
# The tested file: ~\Python\Python_Advanced\test\text_processing.py
# The file with the tests: ~\Python\Python_Advanced\test\test_my_module.py