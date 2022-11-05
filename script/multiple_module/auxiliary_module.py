import logging

# create_logger
# that inherit the spam_application logger
module_logger = logging.getLogger('spam_application.auxiliary')
# this actually work
# calling the main module using the same as the logger configured in the main.module

class Auxiliary():
    def __init__(self):
        self.logger = logging.getLogger('class.Auxiliary')
        self.logger.info('creating an instance of Auxiliary')
    
    def do_something(self):
        self.logger.info('doing something')
        # do smthing
        self.logger.info('done doing something')

def some_function():
    module_logger.info('received a call to "some_function"')
