name="Abhishek"
age=23


print("My name is ",name, " and my age is ",age)

# formatted string 
print (f"My name is {name} ans my age is {age}")
# raw string 
print( r"My name is {name} and my age is {age}") 
#  difference between raw string and formatted string is that in raw string the variables are not evaluated and are treated as normal string whereas in formatted string the variables are evaluated and their values are printed.

# Input from user 
name= input("Enter you name: ");
print(name)
#  default data type of input is string 
age = int(input("Enter your age: "))
print(age)
