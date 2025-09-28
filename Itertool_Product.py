# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute product
result = product(A, B)

# Print in one line, space-separated
print(*result)
