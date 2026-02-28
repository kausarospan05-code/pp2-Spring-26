# Scope Accumulator Problem
# Beginner-level solution

# Step 1: Read number of commands
m = int(input())

# Step 2: Initialize variables
g = 0   # global
n = 0   # nonlocal

# Step 3: Process commands
for _ in range(m):
    scope, value = input().split()
    value = int(value)

    if scope == "global":
        g += value
    elif scope == "nonlocal":
        n += value
    elif scope == "local":
        # local changes are ignored
        pass

# Step 4: Print result
print(g, n)