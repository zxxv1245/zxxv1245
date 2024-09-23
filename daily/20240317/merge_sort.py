def merge_sort(arr) :
    global cnt
    if len(arr) < 2 :
        return arr

    mid = len(arr)//2

    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    if left[-1] > right[-1] :
        cnt += 1
    sorted_lst = []

    i = j = 0
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            sorted_lst.append(left[i])
            i += 1
        else :
            sorted_lst.append(right[j])
            j += 1

    sorted_lst += left[i:]
    sorted_lst += right[j:]
    return sorted_lst

T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    sorted_lst = merge_sort(lst)
    print(f'#{Test} {sorted_lst[N//2]} {cnt}')