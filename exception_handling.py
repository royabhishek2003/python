# Exception handling in python
# => Exception handling is a mechanism to handle runtime errors in a graceful manner. It allows us to write code that can handle errors without crashing the program. 
# In python, we can handle exceptions using try-except blocks.

# keywords used in exception handling

# try => we write the code that may raise an exception in the try block.
# except => we write the code that will be executed if an exception is raised in the try block 
# else => we write the code that will be executed if no exception is raised in the try block
# finally => we write the code that will be executed regardless of whether an exception is raised or not. it is used to clean up resources or perform any necessary finalization tasks.
# raise => we can raise an exception using the raise keyword. it is used to signal that an error has occurred and to provide information about the error.


# num= int(input("Enter a number: "))
# a=10
# try:
#    result= a//num
#    print(f"The Result is: {result}")
# except ZeroDivisionError:
#     print("Cannot divide by zero")

# some except class in python 

# ZeroDivisionError => raised when we try to divide a number by zero
# ValueError => raised when we try to convert a string to a number and the string is not a valid number
# TypeError => raised when we try to perform an operation on a data type that is not supported
# IndexError => raised when we try to access an index that is out of range
# KeyError => raised when we try to access a key that is not present in a dictionary
# FileNotFoundError => raised when we try to open a file that does not exist
# ImportError => raised when we try to import a module that does not exist
# AttributeError => raised when we try to access an attribute that is not present in an object
# NameError => raised when we try to access a variable that is not defined

    
    
# num= int(input("Enter a number: "))
# a=10
# try:
#    result= a//num
#    print(f"The Result is: {result}")
# except Exception as err:
#     print(f"An error occured: {err}")
# else:
#     print("No error occurred")
# finally:
#     print("This will always be executed")
    


age=int(input("Enter your age: "))

try:
    if age<0:
        raise ValueError("Age cannot be negative")
    elif age<18:
        raise ValueError("you are not eligible for vote")
    else:
        print("You are eligible for the vote")
except ValueError as err:
    print(f"An error occured: {err}")








