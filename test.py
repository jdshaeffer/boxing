level = 10
hp = 4

print("Your hp:")
print("+", end="")
for _ in range(level):
    print("-", end="")
print("+")
print("|",end="")
for _ in range(hp):
    print("#", end="")
for _ in range(level-hp):
    print(" ", end="")
print("| ",hp,"/",level)
print("+", end="")
for _ in range(level):
    print("-", end="")
print("+")
