def quick_sort(start,end) :
    if start >= end :
        return
    p = start
    i = p + 1
    j = end
    while True :
        while i <= end and lst[i] <= lst[p] :
            i += 1
        while j >= 0 and lst[j] > lst[p] :
            j -= 1
        if i > j: break
        lst[i],lst[j] = lst[j],lst[i]

    lst[j],lst[p] = lst[p],lst[j]

    quick_sort(start,j-1)
    quick_sort(j+1,end)

T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))
    quick_sort(0, N - 1)
    print(f'#{Test} {lst[N//2]}')