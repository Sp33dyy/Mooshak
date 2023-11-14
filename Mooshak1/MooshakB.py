I1, D1, I2, D2 = map(int,input().split(" "))
T1 = float(I1 + D1/10)
T2 = float(I2 + D2/10)
def Febre(T1,T2):
    if T2 >= 37:
        if T2 > T1:
            return "FEBRE SUBIU"
        elif T2 < T1:
            return "FEBRE BAIXOU"   
        elif T1 == T2:
            return "FEBRE MANTEVE"
    else:
        return "NORMAL"
print(Febre(T1,T2))