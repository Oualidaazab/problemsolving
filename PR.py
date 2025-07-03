"""
import math  
R=int(input("Enter the rayon : ")) 
H=int(input("Enter the houteur : ")) 
S=(math.pi)*R*(math.sqrt(R**2+H**2))
print(S,round(3)) 

""" 
"""
print(5678//3600)
total_seconds =int(input("enter the secand  : "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f"{total_seconds} seconds is {hours} hour(s), {minutes} minute(s), {seconds} second(s)")
 # V =D/T  
distance  = float(input("enter the distance in  km  ")) 
V=distance/(total_seconds//3600) 
print(V) 
""" 

# while loops 
# EXERCICE 1 
"""  
numbers = str(input("Enter the numbers : ")).split()
numbers = [int(i) for i in numbers] 
for i  in numbers : 
    if  i%2==0 : 
        print(f"le nomber {i} est pair :") 
    else :  
        print(f'le nomber {i} est sont  impaire :') 
""" 
#EXERCICE 2  
"""
for  i in range(0,100) : 
    if i%3==0 : 
        print(i) 
    else: 
        pass 
""" 
#EXERCICE  3 
"""
user_number =int(input("Enter  a number : ")) 
for i in range(1,11) : 
    print(f' {user_number} * {i} => {i*user_number}') 
""" 
"""
import os 
print(dir(os)) 
print(os.system("ping 19"))
"""  
def factorielle(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result 
n=4
list=[int(i) for i in range(0,n+1)] 
for i  in list :
    print(sum(list))
     


