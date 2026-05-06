# Abstraction => Abstraction is the process of hiding the implementation details and showing only the functionality to the user. 
# It is one of the fundamental concepts of object-oriented programming (OOP). 
# Abstraction allows us to focus on what an object does instead of how it does it.
# In Python, we can achieve abstraction by using abstract classes and abstract methods.
# An abstract class is a class that cannot be instantiated and is meant to be subclassed.
# An abstract method is a method that is declared but contains no implementation.

# Basically ham agar chahte hai kisi class ho generlize karna ki wo class aise hi dikhe yahi sari peremeter  le apne aap me kuch impment na kare 

from abc import ABC, abstractmethod 


# class Abstract(ABC):
#     @abstractmethod
#     def show(self):
#         pass
    
# class Demo(Abstract):
#     def show(self):
#         print("This is an implementation of the abstract method")   
        
# obj= Demo()
# obj.show()  

class Abstract(ABC):
    
    @abstractmethod
    def square(self, side):
        pass
    
    @abstractmethod
    def perimeter(self, length, breadth):
        pass

class child(Abstract):
    def square(self, side):
        return side*side
    def perimeter(self, length, breadth):
        return 2*(length+breadth)
    
obj= child()
print(obj.square(5)) # 25 
print(obj.perimeter(5,10)) # 30  
   
# yaha koi bhi child class jo abstract class ko inherit kar rha hai usko sare abstract methd ko define karna padega having a same number of parameter as defined in the abstract class otherwise wo class bhi abstract class ban jayegi aur uska object nahi ban sakta hai.
