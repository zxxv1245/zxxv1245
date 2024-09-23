def is_P(pnd) :
    N = len(pnd)//2

    for i in range(N) :
        if pnd[i] != pnd[-i-1] :
            return False
    return True

for Test in range(1,11) :
    T = int(input())
    lst = [input() for _ in range(100)]

    x = y = 0
    i = 0
    maxV = 0
    while x < 100 :
        i += 1
        pnd = lst[x][y:y+i]
        if is_P(pnd) == True:
            ret = len(pnd)

        if maxV < ret :
            maxV = ret
        if maxV > i :
            y +=1
            i = 0

        if y + i == 100  :
            i = 1
            y += 1

        if y == 99 :
            y= 0
            x += 1


    lst = list(map(list,zip(*lst)))
    x = y = 0
    i = 0
    while x < 100:
        i += 1
        pnd = lst[x][y:y+i]
        if is_P(pnd) == True:
            ret = len(pnd)

        if maxV < ret:
            maxV = ret
        if maxV > i:
            y += 1
            i = 0


        if y + i == 100 :
            i = 1
            y += 1

        if y == 99 :
            y = 0
            x += 1


    print(f'#{T} {maxV}')