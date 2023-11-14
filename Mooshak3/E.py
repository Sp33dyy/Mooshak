quatro = ["muuu","miao","auau","meemee"]
duas = ["piupiu","cocorocoo","cacaraca","quaqua","jaco"]

patas = 1
t, Min, Max = 0, 0, 0
while patas != 0:
    try:
        patas, barulho = map(str,input().split())
    except ValueError:
        break
    t += 1
    patas = int(patas)
    if patas == 4: # não foi o jaco
        pass
    else:
        Max += 1
        if "jaco" in barulho: # foi o jaco de certeza
            Min += 1
        elif any(x in barulho for x in quatro):
            Min += 1
        else:
            for x in duas:
                if x in barulho:
                    barulho = barulho.replace(x,"",1)
                    if len(barulho) > 0:
                        Min += 1
                        break

print(f"{t} {Min} {Max}")