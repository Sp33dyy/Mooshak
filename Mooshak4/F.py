R, C = map(int,input().split())
partes = C

mat = [[0]*R]*C
for i in range(C):
    mat[i] = list(input())

while True:
    tamanho = int(C/partes)
    if tamanho > C//2:
        print(1)
        break
    def Pedaco(tamanho):
        mask = []
        for i in range(tamanho):
            mask.append(mat[i])
        for i in range(tamanho,C,tamanho):
            for j in range(tamanho):
                if mask[j] != mat[i+j]:
                    return 0
        return 1
    if Pedaco(tamanho) == 0:
        while C/(tamanho+1) != int(C/(tamanho+1)):
            tamanho += 1
        partes = C / (tamanho+1)
    else:
        print(int(partes))
        break