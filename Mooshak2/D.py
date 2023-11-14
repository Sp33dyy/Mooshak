m = int(input())
M = list(map(int,input().split()))
A, B, j= 0, 0, 0
for i in range(m):
    if i % 2 == 0: # Alex plays
        if M[0] > M[-1]:
            A += M.pop(0)
        else:
            A += M.pop(-1)
    else: #Bela plays
        if j % 2 == 0:
            if M[0] > M[-1]:
                B += M.pop(-1)
            else:
                B += M.pop(0)
        else:
            if M[0] > M[-1]:
                B += M.pop(0)
            else:
                B += M.pop(-1)
        j += 1
if B > A:
    print(f"Bela ganha com {B} contra {A}")
elif A > B:
    print(f"Alex ganha com {A} contra {B}")
else:
    print(f"Alex e Bela empatam a {A}")