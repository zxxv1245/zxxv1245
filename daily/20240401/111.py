def check(word) :
    a = 0
    for i in word :
        if int(i) < a :
            return 0
        elif int(i) >= a :
            a = int(i)
    return 1

T = int(input())
for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))
    maxV = -1
    for i in range(N-1) :
        for j in range(i+1,N) :
            word = str(lst[i]*lst[j])
            if check(word) :
                maxV = max(maxV,lst[i]*lst[j])
    print(f'#{Test} {maxV}')
