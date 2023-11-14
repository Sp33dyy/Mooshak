dict = {}
percursos, nos = map(int,input().split())
for _ in range(nos):
    a,b,c,d = map(int,input().split())
    dict[(a,b)] = c

while True:
    p = list(map(int,input().split()))
    m, M = 50, -50
    if p[0] == 0:
        break
    for i in range(1,p[0]):
        for no,temp in dict.items():
            if p[i] in no and p[i+1] in no:
                M = max(M,temp)
                m = min(m,temp)
    print(m,M)