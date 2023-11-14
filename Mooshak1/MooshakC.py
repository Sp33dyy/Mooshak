R = int(input())
A, B = map(int,input().split(" "))
C, D = map(int,input().split(" "))

def Possiveis(R,Min,Max):
    if Min + R <= Max:
        m = Min
    else:
        return 0, 0
    for i in range(Max-Min):
        if Min + R <= Max:
            M = Min
            Min += 1
    return m, M

def Comuns(a,b):
    m = max(a[0],b[0])
    M = min(a[1],b[1])
    if M < m:
        return 0, 0
    return m, M

resultado = Comuns(Possiveis(R,A,B),Possiveis(R,C,D))
if resultado[0] == resultado[1]:
    if resultado[0] == 0:
        print("Impossivel")
    else:
        print(resultado[0])
else:
    print(resultado[0],resultado[1])