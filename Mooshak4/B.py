percursos, nos = map(int,input().split())
d = {}
for _ in range(percursos):
    p = list(map(int,input().split()))
    t = 0
    if p[0] == 0:
        break
    for i in range(1,(p[0]*2)-1,2):
        d[p[i],p[i+2]] = p[i+1]
        t += p[i+1]
    print(f"Trajeto {_+1}: {t}")

seen = []
for no,dist in d.copy().items():
    if (no[1],no[0]) in seen:
        d[nos+1,nos+1] = d.pop(no)
    else:
        seen.append(no)


for i in range(1,nos+1):
    c = 0
    for no in d.keys():
        if i in no:
            c += 1
    print(f"No {i}: {c}")
