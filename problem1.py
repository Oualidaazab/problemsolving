#------------------------------------------------------------------------------------------------------------
# Task                                                                                                       |               
# The provided code stub reads an integer,n, from STDIN. For all non-negative integers i<n , print i²        |             
#  Example                                                                                                   |
# n=3                                                                                                        |
# The list of non-negative integers that are less than is n=3 is [0,1,2]                                     | 
#  Print the square of each number on a separate line.                                                       | 
#  0                                                                                                         |
#  1                                                                                                         |
#  4                                                                                                         |                                                                                                                                    
#  From Hacker Rank                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
#------------------------------------------------------------------------------------------------------------

# PYHTON COD 

n = int(input("Enter a number : ")) 
for i in  range(n): 
    print(i**2)  
