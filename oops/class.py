# oops => Object Oriented Programming System
# class -> A class is a blueprint for creating objects.
# It defines a set of attributes and methods that the objects created from the class will have.

# object -> An object is an instance of a class. It is a real-world entity that

class Factory:
    a=12   #attribute of class 
    def hello(self):
        print("Hello how are you?")
    
    print("Hello how are you i am getting inialized")

factory1 = Factory()
print(factory1.a) # 12
factory1.hello() # Hello how are you?


# self => self is a reference to the current instance of the class.
# It is used to access the attributes and methods of the class in python. 
# It is a convention to use self as the name of the first parameter of the methods in a class,
# but you can use any name you want. However, it is recommended to use self for better readability and consistency.




    