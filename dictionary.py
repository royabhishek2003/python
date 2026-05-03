import copy

# dictionary => dictionary is a built-in data type in Python that allows you to store and manage data in key-value pairs.
# It is also known as an associative array or hash map in other programming languages.

# dict1={}
# print(type(dict1)) # <class 'dict'>


dict1={"name":"Abhishek", "age":23, 23:"Age"}
# print(dict1)

# print(dict1["name"]) # Abhishek
# print(dict1[23]) # Age
# print(dict1["age"])

# print(dict1.get("name")) # Abhishek
# print(dict1.get(23)) # Age
# print(dict1.get("age")) # 23

# dict1["name"]= "Abhi" # updates the value of the key "name" to "Abhi"
# print(dict1)

# # keys can be deleted but can notbe changed because keys are immutable but values can be changed because they are mutable.
# dict1["class"]="python" # adds a new key-value pair to the dictionary
# print(dict1)

# del dict1[23] # deletes the key-value pair with the key 23
# print(dict1)

# # Travrersing a dictionary

# for key in dict1:
#     print(key, end=" ") # name age class
    
# for key in dict1:
#     print(dict1[key], end=" ") # Abhi 23 python

# for i in dict1.items():
#     print(i, end=" ") # ('name', 'Abhi') ('age', 23) ('class', 'python')
    
# for i in dict1.values():
#     print(i, end=" ") # Abhi 23 python
    


# clonning of all built in data structures 
#  cloning in list


# a=[1, 2, 3, 4, 5 ]

# b=a # this is not a clone, this is just a reference to the same list. if we change a then b will also change because both a and b are pointing to the same list in memory.

# # # deep cloning of list
# c=a.copy() # Shallow copy → outer list copied, inner lists still shared
# d= a[:] # Shallow copy → outer list copied, inner lists still shared
# e= list(a) # Shallow copy → outer list copied, inner lists still shared
# f= copy.deepcopy(dict1) # Deep copy → entire structure copied, no shared references

# # cloning in dictionary

# dict2=dict1 # this is not a clone, this is just a reference to the same dictionary. if we change dict1 then dict2 will also change because both dict1 and dict2 are pointing to the same dictionary in memory.
# dict3=dict1.copy() # Shallow copy → outer dictionary copied, inner dictionaries still shared
# dict4= dict(dict1) # Shallow copy → outer dictionary copied, inner dictionaries still shared
# dict5= copy.deepcopy(dict1) # Deep copy → entire structure copied, no shared references

# Methods of dictionary 

dict1={"name":"Abhishek", "age":23, 23:"Age"}
# dict1.clear() # removes all the key-value pairs from the dictionary
# print(dict1)
# dict1.pop("name") # removes the key-value pair with the specified key and returns the value
# print(dict1)

# dict1.popitem() # removes and returns an arbitrary key-value pair from the dictionary. raises a KeyError if the dictionary is empty
# print(dict1)

# dict1.update({"name":"Abhi", "class":"python"}) # updates the dictionary with the key-value pairs from the specified dictionary. if the key already exists, it will update the value, otherwise it will add a new key-value pair to the dictionary.
# print(dict1)


# d1={10:20, 30:40}
# d2={50:60, 70:80}

# marge the two dictionary we can do this by using update() method also 
# for i in d2:
#     d1[i]=d2[i]

# print(d1) 

# d1.update(d2) # this will update the dictionary with itself, so it will not change anything because all the key-value pairs are already present in the dictionary.
# print(d1)

# count the frequency of each element in a list using dictionary

# a=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1

# print(freq)

# write program to merge two dictionaries and add the values of common keys

d1={10:20, 30:40, 50:60}
d2={50:60, 70:80}


for key in d2:
    if key in d1:
        d1[key]+=d2[key]
    else:
        d1[key]=d2[key]

print(d1)











    
    