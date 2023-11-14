mat = [0] * 6
Colunas = 7
Linhas = 6
Cheio = True
for i in range(6):
    mat[i] = list(map(str,input()))

for i in range(6):
    for j in range(7):
        if mat[i][j] == ".":
            mat[i][j] = 0
            Cheio = False
        elif mat[i][j] == "X":
            mat[i][j] = 1
        else:
            mat[i][j] = 2

def Ganhou(mat,n):
    #Horizontais
    for c in range(Colunas):
        for r in range(Linhas):
            try:
                if mat[r][c] == n and mat[r][c+1] == n and mat[r][c+2] == n and mat[r][c+3] == n:
                    return True
            except IndexError:
                next
    #Verticais
    for c in range(Colunas):
        for r in range(Linhas):
            try:
                if mat[r][c] == n and mat[r+1][c] == n and mat[r+2][c] == n and mat[r+3][c] == n:
                    return True
            except IndexError:
                next
    #Diagonal /
    for c in range(Colunas-3):
        for r in range(3,Linhas):
            if mat[r][c] == n and mat[r-1][c+1] == n and mat[r-2][c+2] == n and mat[r-3][c+3] == n:
                return True
    #Diagonal \
    for c in range(3,Colunas):
        for r in range(3,Linhas):
            if mat[r][c] == n and mat[r-1][c-1] == n and mat[r-2][c-2] == n and mat[r-3][c-3] == n:
                return True
    return False

X = Ganhou(mat,1)
O = Ganhou(mat,2)


if X == True:
    print("GANHOU X")
elif O == True:
    print("GANHOU O")
elif Cheio == True:
    print("EMPATE")
else:
    print("JOGANDO")