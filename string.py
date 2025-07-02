number = int(input("Enter the number: "))

for i in range(1, number + 1):
    col1 = i
    col2 = i + 1
    col3 = hex(i)[2:].upper()  # Convert to hex and remove '0x'
    col4 = bin(i)[2:]          # Convert to binary and remove '0b'

    print(f"{col1:<5}{col2:<7}{col3:<5}{col4}")
print(f"{col1:<5}") 
