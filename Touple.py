# Tuple -> Tuple is a collection of items which are ordered and unchangeable.
# It allows duplicate members. Tuple is defined by using parentheses ().
# Immutable -> we cannot change the elements of tuple after creating it. like strings 
# Duplicates-> Tuple allows duplicate members.
# Ordered -> maintains the order of elements as they were added.unless we change the order by using some methods.
# Heterogeneous -> Tuple can contain different types of data.

# a=(1, 2, 3, 4, 5, 5)
# b=("apple", "banana", "cherry")
# c=(1, "apple", 3.14, True) 
# print(a)
# print(b)
# print(c)
# print(type(a))

# for i in a:
#     print(i,end=" ")
    
# for i in range(0,len(c)):
#     print(c[i], end=" ")
    



# a=(1, 2, 3, 4, 5, 5)
# # Methods of tuple 
# a.count(5) # returns the number of times the specified element appears in the tuple
# print(a.count(5))
# a.index(5) # returns the index of the first occurrence of the specified element in the tuple
# print(a.index(5))

# only these two methods are available in tuple because tuple is immutable and we cannot change the elements of tuple after creating it. like strings

# Tuple packing and unpacking
# Tuple packing -> we can pack multiple values into a single tuple
# t= 1, 2, 3, 4, 5
# print(t)

# Touple unpacking -> we can unpack the values of a tuple into individual variables

# t= (1, 2, 3, 4, 5)
# a, b, c, d, e= t
# print(a)
# print(type(a))
# print(b)
# print(c)
# print(d)
# print(e)


a=(1)
print(type(a))  # <class 'int'> because 1 is unpacked and treated as an integer 
b=(1,)
print(type(b))  # <class 'tuple'> , tells the interpreter that this is a tuple with one element and other element might be added later. if we don't add comma then it will be treated as an integer and not a tuple. so we need to add comma to create a tuple with one element.








 

