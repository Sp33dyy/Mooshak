a = int(input())
azul, amarelo, verde = 0,0,0
while a != -1:
    if 1 <= a <= 10:
        azul += 1
    elif 11 <= a <= 23:
        verde += 1
    elif 24 <= a <= 40:
        amarelo += 1
    a = int(input())
print(f"azul: {azul}\namarelo: {amarelo}\nverde: {verde}")