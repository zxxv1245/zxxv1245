def abc(k) :

    if k == N :
        print(*path)
        return

    for i in range(N) :
        if v[i] == 1 : continue
        v[i] = 1
        path[k] = lst[i]
        abc(k+1)
        v[i] = 0
N = int(input())

lst = list(range(1,N+1))

path = [0]*N
v = [0]*N

abc(0)