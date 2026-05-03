# sets => unordered collection of unique items
# sets are defined by using curly braces {} or the set() function.
# sets are mutable, but they cannot contain duplicate items.
# sets are unordered, which means that the items do not have a defined order and cannot be accessed by index.
# sets are heterogeneous, which means that they can contain different types of data.

# s= {1, 2, 3, 4, 5}
# print(s)
# print(type(s))

# Semi Heterogeneous -> we can just add number, string and touple but not everything 
# s= {1,2,3,4,5,5,5,"apple","banana","cherry",(1,2,3)}
# print(s) 

# how sets store the elements 
# sets are implemented as hash tables, which means that they use a hash function to 
# compute a hash value for each element in the set.
# The hash value is used to determine the index of the element in the 
# underlying array. When we add an element to the set, 
# the hash function is called to compute the hash value of the element, 
# and then the element is stored at the corresponding index in the array.
# If there is a collision (i.e., two elements have the same hash value), 
# then the set uses a technique called chaining to store both elements at the same index. 
# This allows sets to efficiently store and retrieve elements while maintaining uniqueness.

# s= {1, 2, 3, 4, 5, 5, 5, "apple", "banana", "cherry", (1, 2, 3)}
# for i in s:
#     print(i)


# Set methods 

# s= {1, 2, 3, 4, 5}
# s.add(6)  # adds an element to the set
# print(s)
# s.remove(3)  # removes the specified element from the set. raises a KeyError
# print(s)
# s.discard(4)  # removes the specified element from the set. does not raise a KeyError
# print(s)
# s.pop()  # removes and returns an arbitrary element from the set. raises a KeyError if the set is empty
# print(s)
# s.clear()  # removes all the elements from the set
# print(s)


# Methods to compare two sets 

s1={1,2,3,4,5}
s2={4,5,6,7,8}

# snew= s1.union(s2)  # returns a new set that contains all the elements from both sets
# same as snew= s1 | s2
# print(snew)

# snew= s1.intersection(s2) # returns a new set that contains only the elements that are present in both sets
# same as snew= s1 & s2
# print(snew)

# snew= s1.difference(s2) # returns a new set that contains only the elements that are present in the first set but not in the second set
# same as snew= s1 - s2
# print(snew)

# snew= s1.symmetric_difference(s2) # returns a new set that contains only the elements that are present in either set but not in both sets
# same as snew= s1 ^ s2
# print(snew)  



