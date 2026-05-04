# Multiple Inheritance -> When a class is derived from more than one base class, it is called multiple inheritance. The derived class inherits the features of all the base classes.

# example of multiple inheritance


# class A:
#     name1="Abhishek"
# class B:
#     name2="Rahul"
# class C(A,B):
#     pass
# c1= C()
# print(c1.name1) # Abhishek -> because class C is inheriting the properties of class A and class B so it can access the name1 attribute of class A and name2 attribute of class B.
# print(c1.name2) # Rahul -> because class C is inheriting the properties of class






class A:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"name: {self.name}")

class B:
    def __init__(self,age):
        self.age=age
    def show(self):
        print(f"age: {self.age}")

class C(A,B):  #MRO(method resolution order) -> it is the order in which the methods are inherited from the base classes. in this case the method show() is defined in both class A and class B so when we call the show() method using the object of class C it will first look for the show() method in class C if it is not found then it will look for the show() method in class A because class A is the first base class of class C and if it is not found then it will look for the show() method in class B because class B is the second base class of class C. so the order of inheritance is C -> A -> B.
    def __init__(self,name,age):
        # super().__init__(name) # yeh A class ke constructor ko caal karega agar B ka constructor ko caal karna hai toh B ko pehle likhna padega 
        # ham alag alag bhi dono ke contructor ko caal kar sakte hai 
        B.__init__(self,age) # yeh B class ke constructor ko caal karega
        A.__init__(self,name) # yeh A class ke constructor ko caal karega
    def show(self):
        
        A.show(self)
        B.show(self)
        
        
c1= C("Abhishek", 23)
c1.show() # name: Abhishek age: 23


        