n = int(input())
s = 0
for i in range(n):
    if i == 0:
        primeiro = int(input())
        continue
    elif i == 1:
        segundo = int(input())
        continue
    a = int(input())
    if a != primeiro and a != segundo:
        if a > primeiro:
            s += a
            continue
        if segundo > a:
            if segundo % a == 0:
                s += a
        if a >= segundo:
            if a % segundo == 0:
                s += a

if s > 0:
    print(f"Resposta G - soma: {s}")
else:
    print("Resposta G - nenhum valor satisfaz")