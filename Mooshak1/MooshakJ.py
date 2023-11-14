n = int(input())
s = 0
for i in range(n):
    if i == 0:
        n2 = int(input())
        continue
    elif i == 1:
        n1 = int(input())
        continue
    e = int(input())
    if n1 > n2*2 and n1 > e*2:
        s += 1
    n2 = n1
    n1 = e

print(s)