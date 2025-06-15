#------------------------------------------------------------------------------------|
# In this challenge, the user enters a string and a substring. You have to print     |
# the number of times that the substring occurs in the given string. String          |
# traversal will take place from left to right, not from right to left               |
#------------------------------------------------------------------------------------|



s = input("Enter the string s: ")  # ABCDCDC
sub = input("Enter the substring sub: ")  # CDC

count = 0
for i in range(len(s) - len(sub) + 1):  # loop through valid start positions
    if s[i:i+len(sub)] == sub:
        count += 1

print(count)






