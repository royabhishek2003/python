# Dunder methods => Double Underscore Methods => Magic Methods => Special Methods
#  They’re also called magic methods because they let you define how your objects behave with built-in Python operations.


# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Animal name is {self.name} and age is {self.age}"

#     def __add__(self, otherobj, otherobj2=None):
#         if otherobj2 is None:
#             return f" Total age is  : { self.age + otherobj.age}  "
#         else:
#             return f" Total age is  : { self.age + otherobj.age + otherobj2.age}  "

# animal1= Animal("Dog", 5)
# animal2= Animal("Cat", 3)
# animal3= Animal("Lion",7)

# print(animal1) # Animal name is Dog and age is 5 -> because we have defined the __str__ method in the Animal class to return a string representation of the object when we print the object.
# print(animal1 + animal2) # Total age is  : 8  -> because we have defined the __add__ method in the Animal class to return a string representation of the addition of two objects when we use the + operator between two objects of the class.
# # print(animal1 + animal2 + animal3) # because python tries it (animal1 + animal2) + animal 3 =>( total age is 8 + animal3)=> error because we have not defined the __add__ method to take three parameters but we can define the __add__ method to take three parameters to avoid this error and return the total age of three objects when we use the + operator between three objects of the class.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal name is {self.name} and age is {self.age}" 
    

    def __add__(self, other):
        
         # if other is a single Animal object
        if isinstance(other, Animal):
            return f"Total age is : {self.age + other.age}"
    
        # for toupe iterable of Animal objects 
        sum=0 
        for i in other:
            sum+= i.age
        return f" Total age is : {self.age + sum}"
            

animal1= Animal("Dog", 5)
animal2= Animal("Cat", 3)
animal3= Animal("Lion",7)

print(animal1) # Animal name is Dog and age is 5 -> because we have defined the __str__ method in the Animal class to return a string representation of the object when we print the object.
print(animal1 + (animal2)) # Total age is  : 8  -> because we have defined the __add__ method in the Animal class to return a string representation of the addition of two objects when we use the + operator between two objects of the class.
print(animal1 + (animal2 ,animal3)) # Total age is : 15
