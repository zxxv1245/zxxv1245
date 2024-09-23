L = int(input())
cake = [0]*(L+1)
N = int(input())
maxC = -21e8
maxab = -21e8
for i in range(1,N+1) :
    S, E = map(int,input().split())
    cnt = 0
    ab = len(cake[S:E+1])
    if maxab < ab :
        maxab = ab
        maxaP = i
    for j in range(S,E+1) :
        if cake[j] == 0 :
            cake[j] = i
            cnt += 1
    if maxC < cnt :
        maxC = cnt
        maxP = i

print(maxaP)
print(maxP)