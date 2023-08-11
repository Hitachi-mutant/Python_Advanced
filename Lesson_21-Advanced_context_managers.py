'''Home work for the lesson 20'''

'''Task 1 - File Context Manager class:
Create your own class, which can behave like a built-in function 'open'. 
Also, you need to extend its functionality with counter and logging. 
Pay special attention to the implementation of '__exit__' method, which has to cover 
all the requirements to context managers mentioned here '''

import logging

class FileHandler:

    file_counter = 0    # Keep track of how many times a file is opened

    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        FileHandler.file_counter += 1
        logging.info(f"Opened file '{self.filename}' in mode '{self.mode}'")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        FileHandler.file_counter -= 1
        logging.info(f"Closed file '{self.filename}'")
        if exc_type is not None:
            # Log any exceptions that occurred
            logging.error(f"An exception of type {exc_type} occurred: {exc_value}")
        if FileHandler.file_counter == 0:
            logging.info("All files are closed")


logging.basicConfig(level=logging.INFO)

with FileHandler("File_Context_Manager_class.txt", "w") as file:
    file.write("It's working!")

with FileHandler("File_Context_Manager_class.txt", "r") as file:
    content = file.read()
    print(content)

