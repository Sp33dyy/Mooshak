n,tonto,sentido,graus,dir = int(input()),False,1,0,["S", "SE", "E", "NE", "N", "NW", "W", "SW"]
while n != -1:
    graus = (graus+(sentido*(n//45))) % 8
    if n > 720: tonto,sentido = True, -sentido
    else: tonto = False
    n = int(input())
print(f"({dir[graus]}, " + "CW, "*(sentido == -1) + "CCW, "*(sentido == 1) + "normal"*(not tonto) + "tonto"*(tonto) + ")")