import sys
from src.logger  import logging 
# sys is Python's System module.
# It helps us get detailed information about errors.
# Commonly used in custom exception handling to find
# the file name and line number where the error occurred.


def error_message_detail(error, error_detail: sys):
    # This function takes:
    # 1. error -> actual error message
    # 2. error_detail -> sys module containing error details

    # exc_info() returns 3 values:
    # 1. Error type
    # 2. Error value/message
    # 3. Traceback object
    _, _, exc_tb = error_detail.exc_info()

    # Get the file name where the error occurred
    file_name = exc_tb.tb_frame.f_code.co_filename

    # Create a detailed custom error message
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name,
        exc_tb.tb_lineno,
        str(error)
    )

    return error_message


# Create our own custom exception class
# Exception is Python's built-in error class.
# By writing (Exception), we tell Python that
# CustomException should behave like a normal error.
class CustomException(Exception):

    # Automatically runs whenever a CustomException object is created
    def __init__(self, error_message, error_detail: sys):

        # Call the parentclass constructor
        super().__init__(error_message)

        # Generate and store detailed error information
        self.error_message = error_message_detail(
            error_message,
            error_detail=error_detail
        )

    # Automatically runs when we print the exception
    def __str__(self):

        # Return the detailed error message
        return self.error_message


