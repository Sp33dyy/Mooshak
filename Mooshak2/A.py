n = int(input())
def intersec(n):
    A, B = map(int,input().split())
    while B >= A:
        for i in range(n-1):
            C, D = map(int,input().split())
            if C > B or A > D or C > D:
                return "impossivel"
            else:
                A = max(A,C)
                B = min(B,D)
        if A == B:
            return A
        a = (A+B)//2
        return f"{a} e meia"
    return "impossivel"
print(intersec(n))