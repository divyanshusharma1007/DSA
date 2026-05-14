n = 5

# Approach 1: string multiplication inside a for loop
for i in range(1, n + 1):
    row = "*" * i
    print(row)

print()

# Approach 2: build rows first, then print with join
rows = []

for i in range(1, n + 1):
    row = "*" * i
    rows.append(row)

print("\n".join(rows))

print()

# Approach 3: nested loops
for i in range(1, n + 1):
    row = ""

    for j in range(1, i + 1):
        row += "*"

    print(row)

print()

# Approach 4: while loops
i = 1

while i <= n:
    j = 1
    row = ""

    while j <= i:
        row += "*"
        j += 1

    print(row)
    i += 1

print()
