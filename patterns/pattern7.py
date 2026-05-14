n = 5

# Way 1: Direct formula
for i in range(0, n + 1):
    print(" " * (n - i) + "*" * (2 * i + 1))
for i in range(1, n + 1):
    print(" " * i + "*" * (2 * (n - i) + 1))

print()

# Way 2: Store spaces and stars separately
for i in range(0, n + 1):
    spaces = " " * (n - i)
    stars = "*" * (2 * i + 1)
    print(spaces + stars)
for i in range(1, n + 1):
    spaces = " " * i
    stars = "*" * (2 * (n - i) + 1)
    print(spaces + stars)

print()

# Way 3: Store the whole row in a variable
for i in range(0, n + 1):
    row = " " * (n - i) + "*" * (2 * i + 1)
    print(row)
for i in range(1, n + 1):
    row = " " * i + "*" * (2 * (n - i) + 1)
    print(row)

print()

# Way 4: Using join
upper_part = [
    " " * (n - i) + "*" * (2 * i + 1)
    for i in range(0, n + 1)
]
lower_part = [
    " " * i + "*" * (2 * (n - i) + 1)
    for i in range(1, n + 1)
]
print("\n".join(upper_part + lower_part))

print()

# Way 5: Using center
width = 2 * n + 1
for i in range(0, n + 1):
    stars = "*" * (2 * i + 1)
    print(stars.center(width))
for i in range(1, n + 1):
    stars = "*" * (2 * (n - i) + 1)
    print(stars.center(width))

print()

# Way 6: Using a while loop
i = 0
while i <= n:
    print(" " * (n - i) + "*" * (2 * i + 1))
    i += 1

i = 1
while i <= n:
    print(" " * i + "*" * (2 * (n - i) + 1))
    i += 1

print()

# Way 7: Using nested loops
for i in range(0, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

for i in range(1, n + 1):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (n - i) + 1):
        print("*", end="")
    print()

print()

# Way 8: Using a function
def print_diamond(size):
    for i in range(0, size + 1):
        print(" " * (size - i) + "*" * (2 * i + 1))
    for i in range(1, size + 1):
        print(" " * i + "*" * (2 * (size - i) + 1))


print_diamond(n)

print()

# Way 9: Using levels
for level in range(-n, n + 1):
    spaces = abs(level)
    stars = 2 * (n - abs(level)) + 1
    print(" " * spaces + "*" * stars)
