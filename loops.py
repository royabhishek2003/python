# for loop 
# Range Function -> range(start, stop+1, step) default (0,stop+1, 1)


# for i in range(5):
#     print(i)

# for i in range(1, 10, 2):
#     print(i)
    
# for i in range (10, 0,-1):
#     print(i)
    
# for i in range(0, 11, 2):
#     print(i)

# a= range(1,10,2)

# for i in a:
#     print(i)


# for i in range(10, 0, -1):
#     print(i)


# Table of 5 
# for i in range(1,11,1):
#     print(f"5 * {i} = {5*i}")
    
# # Interate in strings 
# name="python"

# length= len(name)
# for i in range(length):
#     print(name[i], end="")

# print("\n")

# print("Using direct iteration in string")

# # for in loop in string
# for ch in name:
#     print(ch)

# for i in range(1,11):
#     if i%2==0: 
#         continue
#     print(i)

    
# for i in range(1,11):
#     if i==6: break
#     print(i)


#  else statement in loop

# for i in range(1,11):
#     if i==10:
#         print("Break statement is executed")
#         break
#     print(i)

# else: print("Break statment is not executed") # else block is executed only when the loop is exhausted without break statement 
# # if loop encounters break statement then else block will not be exexuted 
    

# string reverse 

# name="python"
# reverse_name=name[::-1]
# print(reverse_name)

# 2nd way to reverse string using for loop

# reverse_name=""
# for i in range(len(name)-1, -1, -1):
#     reverse_name+=name[i]
# print(reverse_name)

# Inplace reverse does not work here because string in python is imutable but we can do it in list
# i=0
# j=len(name)-1
# while i<j:
#     temp=name[i]
#     name[i]=name[j]
#     name[j]=temp
#     i+=1
#     j-=1

# print(name)


# [start : end : step]
# start → where to begin (included)
# end → where to stop (excluded)
# step → how much to jump

# example of slicing in string
# name="python"
# print(name[0:6:2]) # pto
# print(name[0:6:2]) # pto
# print(name[1:6:2]) # yhn
# print(name[:3:-1]) # 0 to 3 in reverse order -> oht
# print(name[5:2:-1]) # nht



#  Some famous string methods 

# name="python programming"
# print(name.upper()) # PYTHON PROGRAMMING (all characters are converted to uppercase)
# print(name.lower()) # python programming (all characters are converted to lowercase)
# print(name.title()) # Python Programming (first character of each word is capitalized)
# print(name.capitalize()) # Python programming (only first character is capitalized)
# print(name.strip()) # python programming (removes leading and trailing spaces)
# print(name.replace("python", "java")) # java programming (replaces all occurrences of "python" with "java")
# print(name.split()) # ['python', 'programming'] (splits the string into a list of words)
# print(name.find("python")) # 0 (returns the index of the first occurrence of "python"
# name.split("o") # ['pyth', 'n pr', 'gramming'] (splits the string at each occurrence of "o")
# name.split(" ") # ['python', 'programming'] (splits the string at each occurrence of space)
# name.find("o") # 4 (returns the index of the first occurrence of "o")


# #  some ismethods in string
# print(name.isalpha()) # False (returns True if all characters are alphabetic and there is at least one character, otherwise False)
# print(name.isdigit()) # False (returns True if all characters are digits and there is at least one character, otherwise False)
# print(name.isalnum()) # False (returns True if all characters are alphanumeric and there is at least one character, otherwise False)
# print(name.isspace()) # False (returns True if all characters are whitespace and there is at least one character, otherwise False)

# print("".isspace()) # True (returns True if all characters are whitespace and there is at least one character, otherwise False)


# a="23dfg785#$%^"
# for i in range(0, len(a)):
#     if( a[i].isalpha()):
#         print(f"{a[i]} is an alphabet")
#     elif (a[i].isdigit()):
#         print(f"{a[i]} is a digit")
#     elif (a[i].isspace()):
#         print(f"{a[i]} is a whitespace")
#     elif (a[i].isalnum()):
#         print(f"{a[i]} is an alphanumeric character")
#     else:
#         print(f"{a[i]} is a special character")





# While loop 

# i=1
# while i<=10:
#     print(i, end="")
#     i+=1

# check if a number is palindrome or not 

# num= int(input("Enter a number: "))
# x=num
# revnum=0
# while num>0:
#     revnum= revnum*10 + num%10
#     num = num // 10

# if(revnum==x):
#     print(f"{x} is a palindrome number")
# else:
#     print(f"{x} is not a palindrome number")
    


#  make a random guessing game 

import random

number= random.randint(1,100)

while True:
    guess= int(input("Enter your guess: "))
    if guess==number:
        print("Congratulations! You guessed the number correctly.")
        break
    elif guess<number:
        print("Your guess is too low. Try again.")
    else:
        print("Your guess is too high. Try again.")





