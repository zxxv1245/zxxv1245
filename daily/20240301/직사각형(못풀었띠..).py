
for _ in range(4) :
    lst = list(map(int,input().split()))

    if lst[2] == lst[4] or lst[0]== lst[6] :
        if lst[3] == lst[5] or lst[1] == lst[7] :
            print('c')
            continue
        else :
            print('b')
            continue
    elif lst[3] == lst[5] or lst[2] == lst[4] :
        print('b')
        continue
