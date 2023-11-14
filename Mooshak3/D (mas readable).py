s1 = str(input()).upper()
s2 = str(input()).upper()

s1 = ''.join(filter(str.isalpha, s1))
s2 = ''.join(filter(str.isalpha, s2))

if (sorted(s1) == sorted(s2)):
    print("yes")
else:
    print("no")
