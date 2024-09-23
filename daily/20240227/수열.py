

N,K = map(int,input().split())
lst = list(map(int,input().split()))

maxV = -21e8
end = 0
sumV = 0
for start in range(N-K+1) :
    while end - start < K and end < N :
        sumV += lst[end]
        end += 1
    if maxV < sumV :
        maxV = sumV
    if end-start == K :
        sumV -= lst[start]

print(maxV)
