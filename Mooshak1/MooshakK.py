n1 = 0
c, cmax = 0, 0
while n1 != -1:
    n1, n2 = map(int,input().split())
    if n1 == n2 == 1:
        c += 1
    if n1 == 1 and n2 == 0:
        cmax = max(cmax, c)
        c = 0
        n1 = 0
        while n1 == 0:
            n1 = int(input())

cmax = max(cmax, c)
print(cmax)