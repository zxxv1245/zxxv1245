def abc(k) :

    if k == M :
        if M > 1  :
            for i in range(M-1) :
                if path[i] > path[i+1] :
                    return
        print(*path)
        return

    for i in range(N) :

        path[k] = lst[i]
        abc(k+1)

N,M =map(int,input().split())

lst = list(range(1,N+1))
path = [0]*M

abc(0)