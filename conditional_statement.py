#  conditional statament 
a=10

if a>5:
    print("a is greater than 5 ")

else:    print("a is less than or equal to 5")
#  mutiple conditions 
b=20
if a>5 and b>15:
    print("a is greater than 5 and b is greater than 15")
elif a>5 or b>15:
    print("a is less than or equal to 5 or b is less than or equal to 15")
elif not(a>5 and b>15):
    print("a is less than or equal to 5 and b is less than or equal to 15")
else:
    print("a is less than or equal to 5 and b is less than or equal to 15")
    
