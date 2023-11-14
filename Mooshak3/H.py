Row, Col = map(int,input().split())
mat = [0] * Row
for i in range(Row):
    mat[i] = list(str(input()).upper())

k = int(input())

finais = []
iniciais = []
def EncontrarLetra(r,c,l,x,y):
    global mat, Encontrado
    if 0 > r or 0 > c or r >= Row or c >= Col:
        return
    if mat[r][c] != palavra[l]:
        return
    if l == (Tamanho-1) and mat[r][c] == palavra[Tamanho-1]:
        finais.append([r+1,c+1])
        Encontrado = True
        return
    return EncontrarLetra(r+x,c+y,l+1,x,y)

for _ in range(k):
    palavra = list(str(input()).upper())
    Tamanho = len(palavra)
    Encontrado = False
    for i in range(Row):
        if Encontrado == True:
            break
        for j in range(Col):
            if Encontrado == True:
                break
            if mat[i][j] == palavra[0]:
                EncontrarLetra(i,j,0,1,0)
                EncontrarLetra(i,j,0,0,1)
                EncontrarLetra(i,j,0,-1,0)
                EncontrarLetra(i,j,0,0,-1)
                EncontrarLetra(i,j,0,1,1)
                EncontrarLetra(i,j,0,1,-1)
                EncontrarLetra(i,j,0,-1,1)
                EncontrarLetra(i,j,0,-1,-1)
                if Encontrado == True:
                    iniciais.append([i+1,j+1])
                    break

for i in range(len(iniciais)):
    print(*iniciais[i], *finais[i])

