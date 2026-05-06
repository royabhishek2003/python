# Encapulation => Encapsulation means putting data and methds together in a single  unit caleed class and 
# hiding the data from ourside the world and only providing access to the data through methods of the class.
# it is one of the fundamental concepts of object oriented programming and it is used to achieve data hiding and abstraction in python. 
# it is achieved by using private and protected access modifiers in python.


# class A:
#     a=10
#     def show(self):
#         print(f"value of a: {self.a}")
# class B(A):
#     def show(self):
#         print(super().a)  
        
# b1= B()
# b1.show()  #10


# class A:
#     _a=10    #protected attribute (same as a public attribute can be accessed outside the class and inherited class also no use of this  ) 
#     def _show(self):
#         print(f"value of a: {self._a}")
# class B(A):
#     def show(self):
#         print(super()._a)  
        
# b1= B()
# b1.show()  #10
# print(A._a) #10 


# Private attribute => it can not be accessed outside the class and it can not be inherited by the child class.

# class A:
#     __a=10    #private attribute 
#     def __show(self): # private method 
#         print(f"This is a private method")

# obj= A()
# print(obj.__a)
# #  __a -> isko na aap bahar se acees kar sakte ho na hi change kar sakte ho 


# class demo:
#     def __init__(self):
#         self.name="Abhishek"
#         self._age=23
#         self.__salary=50000
#     def show(self):
#         print(f"name: {self.name}")
#         print(f"age: {self._age}")
#         print(f"salary: {self.__salary}")

# obj= demo()
# obj.show()
# print(obj.name) #Abhishek 
# print(obj._age) #23  (it is a protected attribute but we can access it outside the class but it is not recommended to access it outside the class)
# print(obj.__salary) #AttributeError: 'demo' object has no attribute '__salary'



