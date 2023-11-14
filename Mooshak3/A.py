a = input()
c = 0
for i in range(len(a)):
    if a[i] == "P" or a[i] == "p":
        c += 1
    if a[i] == "\n":
        break
print(c)