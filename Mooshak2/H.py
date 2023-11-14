TipoCadeira = []
QuantaCadeira = []
Pe = 0
CadeiraLivre = 0
for i in range(int(input())): # Quantos tipos
    TipoCadeira.append(int(input()))
    QuantaCadeira.append(int(input()))

def PodeSentar(lis):
    global Pe, QuantaCadeira
    for i in range(len(lis)):
        for j in range(len(TipoCadeira)):
            if lis[i] == TipoCadeira[j]: # Vê se ele se quer sentar em alguma cadeira
                if QuantaCadeira[j] > 0:
                    QuantaCadeira[j] -= 1 # Se houver, senta nela
                    return
    Pe += 1 # se sair do loop e não encontrar nenhuma cadeira, fica de pé

Numero_Habitantes = int(input())
for i in range(Numero_Habitantes):
    Habitante = []
    a = int(input()) # Quantos tipos?
    for i in range(a):
        Habitante.append(int(input()))
    PodeSentar(Habitante)

print(Pe)
Livre = 0
for i in range(len(QuantaCadeira)):
    while QuantaCadeira[i] > 0:
        Livre += 1
        QuantaCadeira[i] -= 1
print(Livre)