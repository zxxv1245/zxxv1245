
T = int(input())

for _ in range(T) :
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    arr = []
    for idx,x in enumerate(lst) :
        arr.append((idx,x))
    i = 1
    ret = lst[M]
    while True :
        idx,x = arr.pop(0)
        if x == ret and idx == M :
            break
        for arrA in arr :
            if arrA[1] > x :
                arr.append((idx,x))
                idx = 0
                x = 0
                break

        i += 1
    print(i)