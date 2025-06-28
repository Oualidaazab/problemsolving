
# For top cone  
k= int(input("Enter the number for cone : "))
# symbole 
c="*" 
# git the whit of the pillairs  

G=int(input("Enter a number for pillairs  ! ")) 
# draw the tree using for  loop 
# first tree 
for j  in range(k) : 
    print((c*j).rjust(k-1)+c+(c*j).ljust(k-1))
# secand  loop  
for i  in range(k) : 
    print((c*i).rjust(k-1)+c+(c*i).ljust(k-1))  
#pillairs
for i  in range(G) : 
    print((c*4).center(k*2),end="\n")

