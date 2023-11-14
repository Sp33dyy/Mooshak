Faro = ["ARCO DA VILA","MONTE DE FARO"]
Lisboa = ["GRACA","SENHORA DO MONTE","SAO PEDRO DE ALCANTARA","SANTA LUZIA","SANTA CATARINA",
          "MONTE AGUDO","PENHA DE FRANCA","SAO JORGE"]
Porto = ["SE CATEDRAL","IGREJA DOS GRILOS", "TORRE DOS CLERIGOS","SERRA DO PILAR","VITORIA",
         "JARDINS DO PALACIO DE CRISTAL"]

t = 0
inp = [[],[]]
resul = []
nome = str(input())
while nome != "FIM":
    t += 1
    if nome not in inp[0]:
        inp[0].append(nome)
        inp[1].append(1)
    else:
        inp[1][inp[0].index(nome)] += 1
    nome = str(input())

m = 0
for i in range(len(inp[1])):
    if inp[1][i] > m:
        m = inp[1][i]
        del resul[::]
        resul.append(inp[0][i])
    elif inp[1][i] == m:
        resul.append(inp[0][i])
print(t,m)
resul.sort()
for i in range(len(resul)):
    if resul[i] in Faro:
        print(resul[i],"Faro")
    elif resul[i] in Porto:
        print(resul[i],"Porto")
    else:
        print(resul[i],"Lisboa")