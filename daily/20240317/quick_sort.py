def quick_sort(lst) :
    if len(lst) <= 1 :
        return lst
    p = lst[0]
    low = []
    high = []
    for v in lst[1:] :
        if v < p :
            low.append(v)
        else :
            high.append(v)
    return quick_sort(low) + [p] + quick_sort(high)


T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))

    print(f'#{Test} {quick_sort(lst)[N//2]}')