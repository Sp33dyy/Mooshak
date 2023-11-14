F, n= int(input()), int(input())
Min, Pass = 999, 0
for i in range(n):
    e = int(input())
    if e < F:
        Pass += 1
    if abs(F-e) <= abs(F-Min) and e <= F:
        Min = e

if Pass > 0:
    print(Min)
else:
    print("No free lunch")