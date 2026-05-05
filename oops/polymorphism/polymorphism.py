# Compile time polymorhism -> this is like method overloading but python does not suppport it but we can achieve it by using default arguments in the method.
# class A:
#     def show(self,a=None,b=None):
#         if a is not None and b is not None:
#             print(f"sum: {a+b}")
#         elif a is not None:
#             print(f"value of a: {a}")
#         else:
#             print("no arguments")
# a1= A()
# a1.show() # no arguments    
# a1.show(5) # value of a: 5
# a1.show(5,10) # sum: 15


# Run time polymorphism -> method overriding , operator overloading etc ,


# def hello():
#     print("Hello ji")

# def hello():
#     print("Hello World")

# hello() # Hello World because the second definition of hello() overrides the first one.


# class Animal:
    
#     def eat(self):
#         print("i can eat")

# class Dog(Animal):
#     def eat(self):  # eat method is going to override by the childs eat method 
#         print("i can eat dog food")
        
# dog1= Dog()
# dog1.eat() 
    
    
# Duck Typing -> it is a concept in python which is based on the principle of "if it looks like a duck and quacks like a duck then it is a duck". 
# it means that if an object has the same methods and properties as another object then they can be used interchangeably regardless of their actual type. 
# it is a way to achieve polymorphism in python without using inheritance.

class Duck:
    def quack(self):
        print("Quaclk Quack")

class Person:
    def quack(self):  #it does not take care of which class the object belong it only care about the method quack() is present in the class or not if it is present then it will call that method otherwise it will give an error.
        print("I am quacking like a duck")

def make_it_quack(duck):
    duck.quack()
    
    
duck1= Duck()
person1= Person()    

make_it_quack(duck1)
make_it_quack(person1)
