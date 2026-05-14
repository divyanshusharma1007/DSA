n=5
for i in range(1, n + 1):
    print(" "*(n - i + 1)+ "*"*i)
    
print("".join(" "*(n - i + 1)+ "*"*i + "\n" for i in range(1, n + 1)))

print()

for i in range(1, n + 1):
    row = " "*(n - i + 1)+ "*"*i
    print(row)
print() 

print("\n".join(" "*(n - i + 1)+ "*"*i for i in range(1, n + 1)))
