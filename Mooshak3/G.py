Row, Col = map(int,input().split())
mat = [0] * Row
for i in range(Row):
    mat[i] = list(map(int,input().split()))
Start = mat[0][0]

r = 0
c = 0
resul = ""

def Direcao(i,j,dir=""):
    global Encontrado, c, r
    if 0 > i or 0 > j or i >= Row or j >= Col:
        return ""
    if mat[i][j] != Start:
        return ""
    Encontrado = True
    mat[r][c] = 0
    r = i
    c = j
    return dir


# (r,c) -> posição atual
# (i,j) -> posição da direção
while True:
    Encontrado = False
    resul += Direcao(r,c+1,"D")
    resul += Direcao(r,c-1,"E")
    resul += Direcao(r+1,c,"B")
    resul += Direcao(r-1,c,"C")
    if Encontrado == False:
        break



print(resul)
print(Start * (len(resul)+1))