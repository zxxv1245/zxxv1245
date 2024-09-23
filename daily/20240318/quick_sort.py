def quick_sort(arr) :
    if len(arr) < 2 :
        return arr

    p = arr[0]
    left = []
    right  = []
    for value in arr[1:] :
        if value < p :
            left.append(value)
        else :
            right.append(value)
    return quick_sort(left) + [p] + quick_sort(right)


T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))


    print(f'#{Test} {quick_sort(lst)[N//2]}')