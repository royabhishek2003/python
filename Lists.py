# There are 4 types of inbuilt data structure in python 
# 1. List
# 2. Tuple
# 3. Set
# 4. Dictionary


# List is a collection of items which are ordered and changeable.
# It allows duplicate members. List is defined by using square brackets [].
# Mutable -> we can change the elements of list after creating it.
# Duplicates-> List allows duplicate members.
# Ordered -> maintains the order of elements as they were added.unless we change the order by using some methods.
# Heterogeneous -> List can contain different types of data.


# list1= [1, 2, 3, 4, 5]
# list2= ["apple", "banana", "cherry"]
# list3= [1, "apple", 3.14, True]

# print(list1)
# print(list2)
# print(list3)

# print(type(list1))
# for i in list1:
#     print(i,end=" ")
# print("\n")

# for i in range(0,len(list3)):
#     print(list3[i], end=" ")
# print("\n")

a=['a',2,True,print(),len]
print(a)

# List has same slicing and indexing as strig 
print(a[0:5:1])  # a 2 True <built-in function print> <built-in function len>
print(a[0:5:2])  # a True <built-in function len>
print(a[1:5:2])  # 2 <built-in function print>
