# You are asked to ensure that the first and last names of people begin
#with a capital letter in their passports. For example, 
#alison heck should be capitalised correctly as Alison Heck.   
# alison heck => Alison Heck  

def solve(s):
    return ' '.join(word.capitalize() for word in s.split())

print(solve(input("enter the name ! "))) 

