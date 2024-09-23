D,K = map(int,input().split())

def check(D,K) :
    for i in range(1,K-1) :
        for j in range(i,K) :
            if i == 2 and j == 25 :
                a = i
            DP = [0]*(D+1)
            DP[1] = i
            DP[2] = j
            for a in range(3,D+1) :
                DP[a] = DP[a-1]+DP[a-2]
            if DP[D] == K :
                return i,j

i,j = check(D,K)

print(i)
print(j)