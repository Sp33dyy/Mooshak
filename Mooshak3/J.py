inp = input()
abertura = [[],[]] # 0 = ( ; 1 = pos
fecho = [[],[]]
symbols = [["(","[","{"],[")","]","}"]]
resul = []

for i in range(len(inp)):
    if inp[i] in symbols[0]:
        abertura[0].append(inp[i])
        abertura[1].append(i)
    if inp[i] in symbols[1]:
        fecho[0].append(inp[i])
        fecho[1].append(i)

if abertura[0].count("(") != fecho[0].count(")") or abertura[0].count("[") != fecho[0].count("]") or abertura[0].count("{") != fecho[0].count("}"):
    print("Pares mal formados")
elif (len(abertura[0]) == 0 and len(fecho[0]) == 0):
    print("Sem noivos para casar")
else:
    for i in fecho[1]:
        minimo = 1001
        pos = 0
        for j in abertura[1]:
            if (i - j > 0 and i - j < minimo):
                minimo = i-j
                pos = j
        print(abertura[0][abertura[1].index(pos)]+fecho[0][fecho[1].index(i)],pos,i)
        del abertura[0][abertura[1].index(pos)], abertura[1][abertura[1].index(pos)]