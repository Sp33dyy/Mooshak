n = int(input())
lis = []
resul = []
Pos = 0
while n != 0:
    lis.append(n)
    n = int(input())

while Pos < len(lis):
    a = lis[Pos]
    resul.append(a)
    for j in range(Pos+1,len(lis)):
        if a == lis[j]:
            Pos = j
    Pos += 1


for i in range(len(resul)):
    print(resul[i])