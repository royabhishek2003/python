# Multilevel Inheritance -> When a class is derived from a class which is also derived from another class, it is called multilevel inheritance.
# The derived class inherits the features of the base class and also the features of the base class of the base class.

class Factory:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(f"factory name: {self.name}")
class Company(Factory):
    def __init__(self,name,company_name):
        super().__init__(name) # yeh Factory class ke constructor ko caal karega
        self.company_name=company_name
    def show(self):
        Factory.show(self)
        print(f"company name: {self.company_name}")

class Employee(Company):
    def __init__(self,name,company_name,employee_name):
        super().__init__(name,company_name) # yeh Company class ke constructor ko caal karega
        self.employee_name=employee_name
    def show(self):
        Company.show(self)
        print(f"employee name: {self.employee_name}")
        

e1= Employee("California","Google","Abhishek")
e1.show() # factory name: California company name: Google employee name: Abhishek


# Agar ham super() ka use karke parent construcor ko caal karenre toh no need to pass the self argument because super() automatically passes the self argument to the parent constructor.
# but agar ham direct parent class ke constructor ko caal karenre toh hame self argument ko pass karna padega.
# eg -> Factory.__init__self(self,name) yaha self ka use karna padega taki parent class ko pata chale ki kon sa child class ka onject hai jiska constructor ko caal karna hai.