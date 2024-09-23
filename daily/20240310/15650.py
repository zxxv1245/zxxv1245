def abc(k,start) :

    if k == M :
        print(*path)
        return

    for i in range(start,N) :
        if v1[i] == 1 : continue
        v1[i] = 1
        path[k] = lst[i]
        abc(k+1,i+1)
        v1[i] = 0

N,M =map(int,input().split())

lst = list(range(1,N+1))
path = [0]*M
v1 = [0]*N
abc(0,0)