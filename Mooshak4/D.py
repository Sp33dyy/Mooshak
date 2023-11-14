n, r = map(int,input().split())
lig = {}

for i in range(r):
    a,b,c,d = map(int,input().split())
    lig[a,b] = [c,d]

def Output(reserva):
    def FixLugares(reserva,i):
        for j in range(2,i+1):
            pos = (reserva[j],reserva[j+1])
            lig[pos][0] += reserva[0]
    t = 0
    for i in range(2,len(reserva)-1):
        pos = (reserva[i],reserva[i+1])
        if pos not in lig:
            FixLugares(reserva,i-1) # i-1 pq o ultimo n existe
            return f"({reserva[i]},{reserva[i+1]}) inexistente"
        t += lig[pos][1] * reserva[0]
        lig[pos][0] -= reserva[0]
        if lig[pos][0] < 0:
            FixLugares(reserva,i)
            return f"Sem lugares suficientes em ({reserva[i]},{reserva[i+1]})"
    return f"Total a pagar: {t}"

for _ in range(int(input())):
    print(Output(list(map(int,input().split()))))