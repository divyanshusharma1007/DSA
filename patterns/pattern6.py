n = 5

# Way 1: Direct formula
for i in range(1, n + 1):
    print(" " * i + "*" * (2 * (n - i) + 1))

print()

# Way 2: Store spaces and stars separately
for i in range(1, n + 1):
    spaces = " " * i
    stars = "*" * (2 * (n - i) + 1)
    print(spaces + stars)

print()

# Way 3: Store the whole row in a variable
for i in range(1, n + 1):
    row = " " * i + "*" * (2 * (n - i) + 1)
    print(row)

print()

# Way 4: Using join
print("\n".join(" " * i + "*" * (2 * (n - i) + 1) for i in range(1, n + 1)))

print()

# Way 5: Using center
width = 2 * n + 1
for i in range(1, n + 1):
    print(("*" * (2 * (n - i) + 1)).center(width))

print()

# Way 6: Using a while loop
i = 1
while i <= n:
    print(" " * i + "*" * (2 * (n - i) + 1))
    i += 1

print()

# Way 7: Using nested loops
for i in range(1, n + 1):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (n - i) + 1):
        print("*", end="")
    print()

print()

# Way 8: Using reverse star levels
for stars in range(2 * n - 1, 0, -2):
    spaces = " " * ((2 * n + 1 - stars) // 2)
    print(spaces + "*" * stars)
