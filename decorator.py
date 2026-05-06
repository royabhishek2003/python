
# class Animal:
#     @property
#     def show(self):
#         print("Hello how are you doing ")
        
# animal1= Animal()

# print(animal1.show) # Hello how are you doing  -> because we have defined the show method as a property method using the @property decorator, so we can call this method using the object name without parentheses. it is used to access the method as an attribute of the class. it is also used to define getter and setter methods in python to access and modify the private attributes of the class.

# Decorator => decorator is just a function that modifies another function without changing 
# its actual code 

# For creating a decorator you first have to create a decorator function 
# and then inside that will create a wrapper function that will modify the behavior of the original function and then return the wrapper function from the decorator function.
# A decorator is a function that adds extra behavior to another function without changing its original code.

# def decorator(func):  # func->Hello method 
#     def wrapper():
#         print("This is a decorator function")
#         func()
        
#     return wrapper



# @decorator
# def hello():
#     print("Hello welcome to the world of Abhishek")
    

# # @decorator  means: => hello = decorator(hello)

# hello()



# def decorator(func):
#     def wrapper(*args, **kargs):
#        print("This is a decorator before calling the function")
#        func(*args, **kargs)
    
#     return wrapper
# @decorator
# def addition(a,b):
#     print(f"The sum of {a} and {b} is {a+b}")

# addition(5,10)


# positional arguments d=> depens of position *args
# keyword arguments => depends on the name of the parameter **kwargs
# Here in this example *arge= {5,10} and **kwargs={}



# *args => tuple that stores the positional arguments
# def Addition(*arg):
#     sum=0
#     for i in arg:
#         sum+=i
#     print(f"The sum of {arg} is {sum}")

# Addition(5,10,15) # The sum of (5, 10, 15) is 30



# **kargs => dictionary that stores the keyword argiuments 

# def addition(**kargs):
#     sum=0
#     for i in kargs.values():
#         sum+=i
#     print(f"The sum of {kargs} is {sum}")
    
# addition(a=5,b=10,c=15) # The sum of {'a': 5, 'b': 10, 'c': 15} is 30



# def addition(*arg, **kargs):
#     sum=0
#     for i in arg:
#         sum+=i
#     for i in kargs.values():
#         sum+=i
#     print(f"The sum of {arg} and {kargs} is {sum}")
    
# addition(5,10,15,a=20,b=25) # The sum of (5, 10, 15) and {'a': 20, 'b': 25} is 75
    
    
