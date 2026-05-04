# Inheritance => It is a fundamental concept in object-oriented programming (OOP) that allows 
# a new class (called a child or subclass) to inherit properties and behaviors (attributes and methods) from an existing class 
# (called a parent or superclass). This promotes code reusability and establishes a natural hierarchical relationship between classes.

# class Animal:
#     a="i am an animal"
#     def eat(self):
#         print("i can eat")
        
# class Dog(Animal):
#     # pass # pass is a keyword in python that is used to indicate that the block of code is empty. it is used when we want to create a class or a function but we don't want to write any code inside it. it is also used as a placeholder for future code. it does not do anything and it does not affect the execution of the program. it is just a way to avoid syntax errors when we want to create an empty block of code.
#     b="i am a dog"
#     def bark(self):
#         print("i can bark")

# class Cat(Dog):
#     c="i am a cat"
#     def meow(self):
#         print("i can meow")

# dog1= Dog()
# print(dog1.a) # i am an animal -> because dog class is inheriting the properties of animal class
# dog1.eat() # i can eat
# dog1.bark() # i can bark

# cat1= Cat()
# print(cat1.a) # i am an animal -> because cat class is inheriting the properties of animal class
# cat1.eat() # i can eat
# cat1.bark() # i can bark
# cat1.meow() # i can meow




# class A:
#     def __init__(self,name):
#         self.name=name
#     def show(self):
#         print(f"name: {self.name}")

# class B(A):
#     pass

# b1= B("Abhishek") # class B is inheriting also the constructor of class A because we have not defined any constructor in class B 
# # so it is using the constructor of class A to initialize the name attribute.
        
        
# b1.show() # name: Abhishek

class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def eat(self):  # we can call this method by using both object of Animal and object of Dog class because this method is defined in the Animal class and it is inherited by the Dog class. but we can not call this method using the object of Cat class because it is not inherited by the Cat class.
        print(f"name {self.name} , species {self.species}  can eat")
    def eat2(self):  # we can not call this function using the object of the Aninam class it can only be called by the object os Dog class becuse those have only breed attribute 
        print(f"name {self.name} , species {self.species} , breed {self.breed} can eat")

class Dog(Animal):
    def __init__(self,name,species,breed):  # if child class has an atrrbute common to parent class then we have to use super() function to call the constructor of parent class to initialize the common attribute.and the rest of the attributes will be initialized in the child class constructor
        super().__init__(name, species) # super() function is used to call the constructor of parent class to initialize the common attribute.
        self.breed=breed
    def bark(self):
        print(f"name {self.name} , species {self.species} , breed {self.breed} can bark")
        
# dog1= Dog("Tommy", "Dog", "Labrador")
# print(dog1.name) # Tommy
# print(dog1.species) # Dog
# print(dog1.breed) # Labrador
# dog1.eat() # name Tommy , species Dog , breed Labrador can eat
# dog1.bark() # name Tommy , species Dog , breed Labrador can bark

animal = Animal("Tommy", "Dog")
animal.eat() # name Tommy , species Dog , breed Labrador can eat -> this will give an error because the eat method is trying to access the breed attribute which is not defined in the Animal class, it is defined in the Dog class. so we cannot access the breed attribute using the object of the Animal class because it is not inherited by the Animal class. it is only inherited by the Dog class. so we have to create an object of the Dog class to access the breed attribute and call the eat method.




