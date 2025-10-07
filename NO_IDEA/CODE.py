# Ask user for n and m
n, m = map(int, input("Enter n and m: ").split())
hapiness=0
# Ask for the array with n elements
array = list(map(int, input(f"Enter {n} numbers for the array: ").split()))
while len(array) != n:
    print(f"You must enter exactly {n} numbers.")
    array = list(map(int, input(f"Enter {n} numbers for the array: ").split()))

# Ask for set A with m elements
A = set(map(int, input(f"Enter {m} numbers for set A: ").split()))
while len(A) != m:
    print(f" You must enter exactly {m} numbers.")
    A = set(map(int, input(f"Enter {m} numbers for set A: ").split()))

# Ask for set B with m elements
B = set(map(int, input(f"Enter {m} numbers for set B: ").split()))
while len(B) != m:
    print(f"You must enter exactly {m} numbers.")
    B = set(map(int, input(f"Enter {m} numbers for set B: ").split()))

for  i  in array : 
    if i in A: 
        hapiness+=1 
    elif  i in B  :
        hapiness-=1 
print(hapiness) 
