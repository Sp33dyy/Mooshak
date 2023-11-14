T, n = map(int,input().split())
c, cmax = 0, 0
for i in range(n):
    t = int(input())
    if abs(T - t) <= 2:
        c += 1
    else:
        cmax = max(c, cmax)
        c = 0
    if i == n-1:
        if c > cmax:
            cmax = c

if cmax == 1:
    print("Temperaturas moderadas apenas em dias isolados")
elif cmax > 1:
    print(f"Durante {cmax} dias consecutivos, temperaturas moderadas")
else:
    print("Sem registo de temperaturas moderadas")