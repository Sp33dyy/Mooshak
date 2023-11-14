N, M = map(int,input().split())
mat = [0] * N
resul = [0] * M
for i in range(N):
    mat[i] = list(map(int,input()))

for i in range(M):
    for j in range(N):
        resul[i] += mat[j][i] # frequência de cada bit

for i in range(M):
    if resul[i] > int(N/2):
        resul[i] = 1
    else:
        resul[i] = 0    

s = ""
for i in resul:
    s += str(i)
print(s)