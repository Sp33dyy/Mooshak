pessoas, origem, destino, comeco, fim = map(int,input().split())
problemas_minimos,mat,validos = -1,[],0
n = int(input())
for i in range(n):
    mat.append(list(map(int,input().split())))

k,h = map(int,input().split())
while (k!=0 or h!=0):
    rota = list(map(int,input().split()))
    duracao = h*60
    origem_flag = False
    destino_flag = False
    problemas_temp = 0
    for i in range(0,(k-1)*3,3): #lis[i],lis[i+3] = lis[i+1],lis[i+2]
        if (mat[rota[i]-1][rota[i+3]-1] == 1):
            problemas_temp += 1
        if (origem_flag or rota[i] == origem):
            if (origem_flag):
                duracao += rota[i+2]
            if (rota[i+1] < pessoas or duracao < comeco*60 or duracao > fim*60):
                break
            if (not origem_flag):
                duracao += rota[i+2]
                origem_flag = True
            if (rota[i+3] == destino):
                destino_flag = True
                break
        else:
            duracao += rota[i+2]
    if destino_flag:
        if (problemas_minimos == -1):
            validos += 1
            problemas_minimos = problemas_temp
        elif (problemas_minimos == problemas_temp):
            validos += 1
        elif (problemas_minimos > problemas_temp):
            problemas_minimos = problemas_temp
            validos = 1
    k,h = map(int,input().split())
if (validos == 0):
    print("Impossivel")
else:
    print(validos,problemas_minimos)
