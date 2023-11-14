n1 = str(input()) # primeira
print(n1)
while n1 != "#":
    n2 = str(input()) # segundo
    n = "" # nova
    if n2 == "#":
        break
    if n1 == n2:
        print(n1)
    else:
        if "t" not in (n1,n2):
            print("t")
        elif "c" not in (n1,n2):
            print("c")
        else:
            print("a")
    n1 = n2