# Input format: two space-separated integers N and M
N, M = map(int, input().split())

# Top half of the mat
for i in range(N // 2):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))

# Middle line
print("WELCOME".center(M, "-"))

# Bottom half (mirror of the top)
for i in range(N // 2 - 1, -1, -1):
    pattern = ".|." * (2 * i + 1)
    print(pattern.center(M, "-"))



# output
"""
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

"""
