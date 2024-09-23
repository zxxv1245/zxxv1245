def abc(k,start) :
    global minV
    if k == N-1 :
        arr1 = []
        arr2 = []
        for i in range(N) :
            if v[i] == 1:
                arr1.append(i)
            elif v[i] == 0:
                arr2.append(i)
        ret1 = 0
        for a in range(k-1) :
            for b in range(a+1,k) :
                ret1 += lst[arr1[a]][arr1[b]] + lst[arr1[b]][arr1[a]]

        ret2 = 0

        value = abs(ret1 - ret2)
        if minV > value:
            minV = value
        return

    if k >= 1 :
        arr1 = []
        arr2 = []
        for i in range(N) :
            if v[i] == 1:
                arr1.append(i)
            elif v[i] == 0:
                arr2.append(i)
        ret1 = 0
        for a in range(k-1) :
            for b in range(a+1,k) :
                ret1 += lst[arr1[a]][arr1[b]] + lst[arr1[b]][arr1[a]]

        ret2 = 0
        for a in range(N-k-1):
            for b in range(a + 1, N-k):
                ret2 += lst[arr2[a]][arr2[b]] + lst[arr2[b]][arr2[a]]

        value = abs(ret1 - ret2)
        if minV > value:
            minV = value



    for j in range(start,N) :
        if v[j]== 1: continue
        v[j] = 1
        abc(k+1,j+1)
        v[j] = 0

N = int(input())

lst = [list(map(int,input().split())) for _ in range(N)]

v = [0]*N

minV = 21e8
abc(0,0)
print(minV)