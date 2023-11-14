qnt = int(input())

def Possivel(n,lis):
    index = -1
    PassA = False # encontrou A?
    constante = 1
    for i in range(n):
        if lis[i] != -1:
            index = i
            a = lis[i]
            PassA = True
            for j in range(i+1,n):
                if lis[j] != -1:
                    b = lis[j]
                    if b > a:
                        constante = (b-a)/(j-i) # existe A e B, e B > A
                        if constante != int(constante): 
                            return "Impossivel" # não é inteiro (inclui os menores que 1)
                    else:
                        return "Impossivel" # b < a, logo, impossível
            break
    if PassA == True:        
        aesq, adir = a, a
        for i in range(index,-1,-1): # todos os valores à esquerda de A
            if aesq < 0:
                return "Impossivel" # existem valores negativos
            aesq -= constante

        for i in range(index, n): # todos à direita de A
            if lis[i] != -1 and lis[i] != adir:
                return "Impossivel" # se for diferente de A * (i * Constante), impossível
            adir += constante
    return "Possivel"

for i in range(qnt):
    n = int(input())
    lis = list(map(int,input().split()))
    print(Possivel(n, lis))