n = 5

# Way 1: Direct formula
for i in range(0, n + 1):
    print(" " * (n - i) + "*" * (2 * i + 1))

print()

# Way 2: Store spaces and stars separately
for i in range(0, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)

print()

# Way 3: Store the whole row in a variable
for i in range(0, n + 1):
    row = " " * (n - i) + "*" * (2 * i + 1)
    print(row)

print()

# Way 4: Using join
print("\n".join(" " * (n - i) + "*" * (2 * i + 1) for i in range(0, n + 1)))

print()

# Way 5: Using center
width = 2 * n + 1
for i in range(0, n + 1):
    print(("*" * (2 * i + 1)).center(width))

print()

# Way 6: Using a while loop
i = 0
while i <= n:
    print(" " * (n - i) + "*" * (2 * i + 1))
    i += 1

print()

# Way 7: Using nested loops
for i in range(0, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
