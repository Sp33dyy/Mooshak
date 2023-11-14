Disponiveis = list(map(int,input().split()))
Index = [200,100,50,20,10,5]
Totais, R, Retido = 0, 0, 0

def Update(n): # poe as moedas na maquina
    for i in range(6):
        if n == Index[i]:
            Disponiveis[i] += 1
            break

def Inserido(n): # converte a moeda para cêntimos
    inserido = 0
    if n == 2 or n == 1:
        inserido += n * 100
    else:
        inserido += n
    return inserido

def Troco(Devolver):
    global Index, Disponiveis, R, Retido
    for i in range(0, 6):
            while Disponiveis[i] > 0:
                if Devolver - Index[i] >= 0:
                    Disponiveis[i] -= 1
                    Devolver -= Index[i]
                else:
                    break
    if Devolver > 0:
        Retido += Devolver
        R += 1

n1, n2 = map(int,input().split())
while (n1+n2) > 0: # n1 > 0 and n2 > 0
    Totais += 1
    Pagar = n1 * 100 + n2 # O que temos de pagar
    Balanço = 0 # Quanto temos para pagar
    n = int(input())
    while n != 0:
        Update(Inserido(n)) # Atualizar as moedas disponiveis
        Balanço += Inserido(n) # Sempre que inserimos uma moeda temos de converter para centimos
        n = int(input())
    if (Balanço - Pagar) > 0: #Temos suficiente para pagar?
        Troco(Balanço - Pagar)
    n1, n2 = map(int,input().split())

print(Retido//100,Retido%100)
print(f"{R}/{Totais}")