def mastermind():
    n = int(input())
    I, C = 0, 0
    g = list(map(int,input().split()))
    c = list(map(int,input().split()))
    for i in range(n):
        if g[i] == c[i]:
            I += 1
            if i == n-1 and g[i-1] == c[i-1]:
                I -= 1
                C += 1
            elif 0 < i < n-1 and (g[i+1] == c[i+1] or g[i-1] == c[i-1]):
                I -= 1
                C += 1
            elif i == 0 and g[i+1] == c[i+1]:
                I -= 1
                C += 1
    return f"{I+C}\n{I+C*3}"
print(mastermind())