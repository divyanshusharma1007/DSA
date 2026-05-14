n = 5

# Way 1: Direct formula
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)

print()

# Way 2: Store the row in a variable
for i in range(1, n + 1):
    row = "*" * i
    print(row)
for i in range(n - 1, 0, -1):
    row = "*" * i
    print(row)

print()

# Way 3: Using join
upper_part = ["*" * i for i in range(1, n + 1)]
lower_part = ["*" * i for i in range(n - 1, 0, -1)]
print("\n".join(upper_part + lower_part))

print()

# Way 4: Using a while loop
i = 1
while i <= n:
    print("*" * i)
    i += 1

i = n - 1
while i >= 1:
    print("*" * i)
    i -= 1

print()

# Way 5: Using nested loops
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

# Way 6: Using a function
def print_half_diamond(size):
    for i in range(1, size + 1):
        print("*" * i)
    for i in range(size - 1, 0, -1):
        print("*" * i)


print_half_diamond(n)

print()

# Way 7: Using levels
for level in range(1, 2 * n):
    stars = level if level <= n else 2 * n - level
    print("*" * stars)

print()

# Way 8: Using a single loop and abs
for i in range(1, 2 * n):
    stars = n - abs(n - i)
    print("*" * stars)

print()

# Way 9: Using list comprehension with print
rows = ["*" * (i if i <= n else 2 * n - i) for i in range(1, 2 * n)]
for row in rows:
    print(row)
