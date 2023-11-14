Row, Col = map(int,input().split())
mat = [0] * Row
Gambo = 0
for i in range(Row):
    mat[i] = list(map(int,input().split()))


Shapes = [
[[0, 1, 0],
 [1, 1, 0],
 [0, 1, 1]],
[[1, 1, 0], 
 [0, 1, 1],
 [0, 1, 0]],
[[0, 0, 1],
 [1, 1, 1],
 [0, 1, 0]],
[[0, 1, 0],
 [1, 1, 1],
 [1, 0, 0]],
[[0, 1, 0],
 [0, 1, 1],
 [1, 1, 0]]]


def ShapeMatch(i,j,s):
    c = 0
    for k in range(3):
        for q in range(3):
            a = mat[i+k][j+q]
            b = Shapes[s][k][q]
            if a == 1:
                c += 1
                if a != b:
                    return False
    if c != 5:
        return False
    for x in range(3):
        if Shapes[s][0][x] == 1 and mat[i-1][j+x] == 1:
            return False
        if Shapes[s][2][x] == 1 and mat[i+3][j+x] == 1:
            return False
    for x in range(3):
        if Shapes[s][x][0] == 1 and mat[i+x][j-1] == 1:
            return False
        if Shapes[s][x][2] == 1 and mat[i+x][j+3] == 1:
            return False
    return True

def Pintar(i,j):
    for k in range(3):
        for q in range(3):
            mat[i+k][j+q] = 0

for i in range(1,Row-3):
    for j in range(1,Col-3):
        Encontrado = False
        s = 0
        while not Encontrado and s < 5:
            Encontrado = ShapeMatch(i,j,s)
            s += 1
        if Encontrado:
            Pintar(i,j)
            Gambo += 1
print(Gambo)