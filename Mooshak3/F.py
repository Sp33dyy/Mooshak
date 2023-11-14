n = int(input())
i = 0
n1 = str(input())
if n1 == "#":
    i += 1
for _ in range(n-1):
    n2 = str(input())
    if n2 == "#" and n1 == "#":
        i += 1
    n1 = n2
print(i)