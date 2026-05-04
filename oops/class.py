# oops => Object Oriented Programming System
# class -> A class is a blueprint for creating objects.
# It defines a set of attributes and methods that the objects created from the class will have.

# object -> An object is an instance of a class. It is a real-world entity that

# class Factory:
#     a=12   #attribute of class 
#     def hello(self):
#         print("Hello how are you?")
    
#     print("Hello how are you i am getting inialized")  # this will be executed when the class is defined only one time when interpreter reaches it to the first tiime  and not when the object is created.

# factory1 = Factory()
# print(factory1.a) # 12
# factory1.hello() # Hello how are you?


# self => self is a reference to the current instance of the class.
# It is used to access the attributes and methods of the class in python. 
# It is a convention to use self as the name of the first parameter of the methods in a class,
# but you can use any name you want. However, it is recommended to use self for better readability and consistency.

# class Car:
#     def __init__(self, brand, model, year): # constructor ->here self is referencing  to the object like c1,c2 and others by using self python rembers which object is caliing right now and what are the values present inside that object using self.
#         self.brand= brand
#         self.model=model
#         self.year=year
#     def car_info(self):
#         print(f"car brand: {self.brand}, model: {self.model}, year: {self.year}")
       
       
 
# car1= Car("Toyota", "Camry", 2020)
# car1.car_info() # car brand: Toyota, model: Camry, year: 2020 
# car2= Car("Honda", "Civic", 2019)
# car2.car_info() # car brand: Honda, model: Civic, year: 2019


# class Person:
#     good=True  # class attribute -> it is shared by all the objects of the class and it is defined inside the class but outside the constructor.
#     def __init__(self,name,age):  #instance attribute -> it is unique to each object of the class and it is defined inside the constructor using self.
#         self.name=name
#         self.age=age
    
#     def show_info(self):  #instance method -> it is a method that is defined inside the class and it is used to perform some action on the objects of the class. it takes self as the first parameter to access the attributes of the class.
#         print(f"Name: {self.name}, Age: {self.age}")
    
# person1= Person("Abhishek", 23)
# person1.show_info() # Name: Abhishek, Age: 23
# print(person1.good) # True
# person2= Person("Rahul", 25)
# person2.show_info() # Name: Rahul, Age: 25
# print(person2.good) # True
    
    
# Class method -> it is a method that is defined inside the class and it is used to perform some action on the class itself. 
# it takes cls as the first parameter to access the attributes of the class.
# it can access only class attributes and not instance attributes because it is not associated with any object of the class.

# class Person:
#     good = True  # class attribute
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_info(self):
#         print(f"Name: {self.name}, Age: {self.age}")
#     @classmethod
#     def is_good(cls):
#      return cls.good
# person1 = Person("Abhishek", 23)
# print(person1.is_good()) # True 
# print(Person.is_good()) # True because class method can be called using class name also because it is not associated with any object of the class.
# # Person.show_info()  -> This will give an error because show_info is an instance method and it requires an object of the class to be called. it cannot be called using class name because it is associated with the object of the class and it needs to access the attributes of the object using self. 
    

# Static method -> it is a method that is defines inside the class and it is used to perform some action that is related to the class 
# but it does not access any attributes of the class. 
# it does not take self or cls as the first parameter because it is not associated with any object of the class or the class itself.

class Person:
    isgood= True # class attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
    @staticmethod
    def greet(): # this method is not associated with any object of the class or the class itself, it is just a regular function that is defined inside the class.  The class name or the object name can be used to call this method.
        print("Hello, welcome to the world of Python!")
person1 = Person("Abhishek", 23)
person1.greet()  # calling static method using object name

Person.greet() # calling static method using class name











    