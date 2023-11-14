H1, M1 = map(int,input().split())
T1 = 60*H1+M1
H2, M2 = map(int,input().split())
T2 = 60*H2+M2
T = T2 - T1
if T > 60:
    THoras = T // 60
    TMin = T % 60
elif T == 60:
    THoras = 1
    TMin = 0
else:
    THoras = 0
    TMin = T

Pessoa2 = "Queres dizer, "
if THoras > 1:
    Pessoa2 += f"{THoras} horas"
    if TMin > 1:
        Pessoa2 += f" e {TMin} minutos"
    elif TMin == 1:
        Pessoa2 += " e 1 minuto"
    Pessoa2 += "?!"
elif THoras == 1:
    Pessoa2 += "1 hora"
    if TMin > 1:
        Pessoa2 += f" e {TMin} minutos"
    elif TMin == 1:
        Pessoa2 += " e 1 minuto"
    Pessoa2 += "?!"
else:
    Pessoa2 = "De facto!"

Pessoa1 = ""
if T == 1:
    Pessoa1 += "Passou apenas 1 minuto!"
else:
    Pessoa1 += f"Passaram apenas {T} minutos!"

print(Pessoa1)
print(Pessoa2)