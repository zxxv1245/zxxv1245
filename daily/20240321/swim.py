T = int(input())

for Test in range(1,T+1) :
    d,m,tm,y = map(int,input().split())
    lst = list(map(int,input().split()))

    dp = [0]*13

    for i in range(1,13) :
        value = dp[i-1] + lst[i-1]*d
        value = min(value, dp[i-1]+m)
        if i>=3 :
            value = min(value, dp[i-3]+tm)
        if i==12 :
            value = min(value, dp[i-12]+y)
        dp[i] = value

    print(f'#{Test} {dp[12]}')