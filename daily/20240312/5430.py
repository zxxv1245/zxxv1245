from collections import deque

T = int(input())

for Test in range(1,T+1) :
    arr = list(input().strip())
    N = int(input())
    lst = input().rstrip()[1:-1].split(',')
    numlst = deque()
    ret = 0
    zxx = 0
    for i in lst :
        if i.isdigit() :
            numlst.append(i)

    for a in arr :
        if a == 'R' :
            zxx += 1
        elif a == 'D' and numlst and zxx% 2 == 1 :
            numlst.pop()
        elif a == 'D' and numlst and zxx% 2 == 0 :
            numlst.popleft()
        else :
            ret = 1
            break

    if zxx % 2 == 1 :
        numlst.reverse()
    if ret == 0 :
        if numlst :
            print('[',end = '')
            for i in range(len(numlst)-1) :
                print(numlst[i],end = ',')
            print(numlst[-1],end = '')
            print(']')
        else :
            print('[]')
    else :
        print('error')
