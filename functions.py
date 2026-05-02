import math
# def hello():
#     print("Ki  hall hai???")

# hello()

# def isprime(n):
#     if(n<=1):
#         return False
#     for i in range(2,int(math.sqrt(n))+1):
#         if(n%i==0):
#             return False
#     return True

# print(isprime(11))


# 3 types of parameters in python
# 1. Positional parameters
# 2. Default parameters
# 3. Keyword parameters

# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old")

# greet("Abhishek", 23)  # Positional parameters

# def greet(name, age=18):
#     print(f"Hello {name}, you are {age} years old")

# greet("Abhishek")  # Default parameters

# def greet(name, age=18):
#     print(f"Hello {name}, you are {age} years old")

# greet(age=23, name="Abhishek")  # Keyword parameters



# def ispalindrome(s):
#     s= s.replace(" ","")
#     s= s.lower()
#     return s==s[::-1]

# print(ispalindrome("A man a plan a canal Panama"))

# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# ans= factorial(5)
# print(ans)


# def fibonacci(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(5))



# def power(base, exp):
#     if exp==0:
#         return 1
#     elif exp<0:
#         return 1/power(base, -exp)
#     else:
#         return base*power(base, exp-1)

# print(power(2,-3))

# Binary exponentiation 

# def power(base, exp):
#     if exp==0:
#         return 1
#     elif exp<0:
#         return 1/power(base, -exp)
#     elif exp%2==0:
#         half_power= power(base, exp//2)
#         return half_power*half_power
#     else:
#         half_power= power(base, exp//2)
#         return half_power*half_power*base

# print(power(2,10))

# def gcd(a,b):
#     if b==0:
#         return a
#     else:
#         return gcd(b, a%b)
    
# print(gcd(48,18))


