A, E1, E2 = map(int,input().split(" "))

def MaisProx(A,E1,E2):
    if E1 == E2 == 999:
        return 0
    elif E1 == 999:
        return 2
    elif E2 == 999:
        return 1
    if E1 == E2:
        return 1
    if abs(A - E1) == abs(A - E2):
        if max(E1, E2) == E2:
            return 2
        return 1
    elif abs(A - E1) > abs(A - E2):
        return 2
    return 1

print(MaisProx(A,E1,E2))