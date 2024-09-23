def merge_sort(arr) :
    global cnt
    if len(arr) < 2 :
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] > right[-1] :
        cnt += 1

    result = []

    i = j = 0
    while i < len(left) and j < len(right) :
        if left[i] < right[j] :
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

T = int(input())
for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    print(f'#{Test} {merge_sort(lst)[N//2]} {cnt}')