def abc(k,start) :

    if k == L :
        cnt = 0
        for i in path :
            if i in ['a', 'e', 'i', 'o', 'u'] :
                cnt += 1
        if cnt == 0 or cnt > L-2 :
            return
        print(''.join(path))
        return


    for i in range(start,C) :
        if v[i] == 1 : continue
        v[i] = 1
        path[k] = lst[i]
        abc(k+1,i+1)
        v[i] = 0

L,C = map(int,input().split())

lst = sorted(list(input().split()))

path = [0]*L
v = [0]*C

abc(0,0)
