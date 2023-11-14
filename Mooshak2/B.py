C, N = map(int,input().split())
R = C
for i in range(N):
    P = int(input())
    A = str(input())
    if P <= R:
        print(A)
        R -= P
print(C-R,R)