N, K = map(int,input().split())
lst = list(map(int,input().split()))

sumV = 0
end = 0
maxV = -21e8
for start in range(N-K+1) :
    while end < start + K :
        sumV += lst[end]
        end += 1
    if maxV < sumV :
        maxV = sumV
    sumV -= lst[start]

print(maxV)