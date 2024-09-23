
def counting_sort() :
    arr = []
    for lstA in lst :
        arrA = []
        arrB = []
        for i in range(1,101) :
            if i in lstA :
                lstA_count =lstA.count(i)
                arrA.append([i,lstA_count])
        arrA.sort(key = lambda x:x[1])
        for l in arrA :
            arrB.extend(l)
        arr.append(arrB)
    maxV = -1
    for j in arr :
        if maxV < len(j) :
            maxV = len(j)

    for k in arr :
        if len(k) < maxV :
            while len(k) != maxV :
                k += [0]
    return arr
def check() :
    global lst
    col_count = len(lst[0])
    row_count = len(lst)
    arr = []

    if row_count >= col_count :
        return 'R'
    else :
        return 'C'

R,C,K = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(3)]
cnt = 0
while cnt != 100 :
    try :
        if lst[R-1][C-1] == K :
            break
    except :
        pass
    cnt += 1
    ck = check()
    if ck == 'R' :
        lst = counting_sort()
    elif ck == 'C' :
        lst = list(map(list, zip(*lst)))
        lst = counting_sort()
        lst = list(map(list, zip(*lst)))




if cnt != 100 :
    print(cnt)
else :
    try :
        if lst[R-1][C-1] == K :
            print(cnt)
        else :
            print(-1)
    except:
        print(-1)