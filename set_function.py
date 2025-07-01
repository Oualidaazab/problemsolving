# Enter your code here. Read input from STDIN. Print output to STDOUTj,;:
contry  =int(input("Enter the number of contryies : ")) 
list_chek=  []  
s=set()
for  i  in range(contry) : 
    name_contry = (input("Enter the  name of contry :")) 
    list_chek.append(name_contry)
for  j in list_chek : 
    if list_chek.count(j) != 2 :  
         s.add(j) 
print(s)
