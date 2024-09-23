T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int, input().split()))
    ret = 21e8
    for x in range(N-1) :
        minP = x
        for y in range(x+1, N) :
            if lst[minP] > lst[y] :
                minP = y
        lst[x],lst[minP] = lst[minP], lst[x]

    for i in range(N-2) :
        for j in range(i+1,N-1) :
            maxV = -21e8
            minV = 21e8
            arr = []
            arr.append(lst[:i+1])
            arr.append(lst[i+1:j+1])
            arr.append(lst[j+1:N])
            if len(arr[0]) <= N//2 and len(arr[1]) <= N//2 and len(arr[2]) <= N//2 :
                if lst[i] != lst[i+1] and lst[j] != lst[j+1] :
                    for a in arr :
                        if maxV < len(a) :
                            maxV = len(a)
                        if minV > len(a) :
                            minV = len(a)
                    if ret > (maxV-minV) :
                        ret = (maxV - minV)
    if ret == 21e8 :
        ret = -1
    print(f'#{Test} {ret}')

