# lambda functions are anonymous functions that can take any number of arguments but can only have one expression.
# They are defined using the lambda keyword.

# def addition(a,b):
#     return a+b

# print(addition(5,10)) # 15


# Lambda function for addition of two numbers 

# num = lambda a,b : a+b
# print(num(5,10)) # 15

# # # complex lambda function 
# # # lambda function only allows a single expression
# # count = lambda str: for i in str: if i in "aeiouAEIOU": count+=1
# # # This is wrong this is not a single expression this is a block of code so we cannot use lambda function for this purpose we can use a normal function for this purpose

# # print(count("python"))


# iseven= lambda num: True if num%2==0 else False
# print(iseven(5)) # False


# Map function is used to apply a function to all the items in an iterable object.

# Map(function,iterables)
# a=[1,2,3,4,5]

# # using map function to square all the elements in the list
# squared= map(lambda x: x**2, a)
# def square(x):
#     return x**2

# squared2= map(square, a)

# print(type(squared)) # <class 'map'> -> because the map function returns a map object which is an iterator that yields the results of applying the function to the items of the iterable.
# print(list(squared))

# print(type(squared2)) # <class 'map'> -> because the map function returns a map object which is an iterator that yields the results of applying the function to the items of the iterable.
# print(list(squared2))




# Filter Function is used to filter the items in an iterable object based on a condition.
# Filter(function,iterable)

a=[1,2,3,4,5]
# using filter function to filter the even numbers from the list
even = filter(lambda x: x%2==0, a)
print(type(even)) # <class 'filter'> -> because the filter function returns a filter object which is an iterator that yields the items of the iterable for which the function returns true.
print(list(even)) # [2, 4] -> because the filter function returns a filter object which is an iterator that yields the items of the iterable for which the function returns true.

def iseven(x):
    return x%2==0

even2= filter(iseven, a)
print(type(even2)) # <class 'filter'> -> because the filter function returns a  filter object which is an iterator that yields the items of the iterable for which the function returns true.
print(list(even2)) # [2, 4] -> because the filter function returns a filter object which is an iterator that yields the items of the iterable for which the function returns true.

