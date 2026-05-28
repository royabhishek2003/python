import random as rn
import numpy as np

# random() method is used to generate a random number between 0 and 1.
print(rn.random()) # 0.123456789 -> this will generate a random number between 0 and 1 every time you run the code it will generate a different random number.

a= rn.randint(1,10) # this will generate a random integer between 1 and 10 inclusive.
print(a) # 5 -> this will generate a random integer between 1 and 10 every time you run the code it will generate a different random integer.
b= rn.choice([1,2,3,4,5]) # this will randomly select an element from the list.
print(b) # 3 -> this will randomly select an element from the list every time you run the code it will select a different element from the list.
c= rn.shuffle([1,2,3,4,5]) # this will randomly shuffle the elements in the list.
print(c) # None -> this will randomly shuffle the elements in the list every time you run the code it will shuffle the elements in a different way every time you run the code. The shuffle() method does not return anything it modifies the original list.
d= rn.sample([1,2,3,4,5], 3) # this will randomly select 3 elements from the list.
print(d) # [2, 4, 5] -> this will randomly select
# 3 elements from the list every time you run the code it will select different elements from the list.
e= np.random.rand(5) # this will generate an array of 5 random numbers between 0 and 1.
print(e) # [0.12345678 0.23456789 0.34567891 0.45678912 0.56789123]