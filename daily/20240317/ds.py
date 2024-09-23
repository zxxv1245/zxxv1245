def merge(left,right) :
    global cnt

    if left[-1] > right[-1] :
        cnt += 1

    result = []

    left_N = len(left)
    right_N = len(right)
    l=r=0

    while l < left_N or r < right_N :
        if l < left_N and r < right_N :
            if left[l] <= right[r] :
                result.append(left[l])
                l += 1
            else :
                result.append(right[r])
                r += 1
        elif l < left_N :
            result.append(left[l])
            l += 1
        elif r < right_N :
            result.append(right[r])
            r += 1
    return result
def merge_sort(arr) :
    if len(arr) < 2 :
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))

    cnt = 0
    ret = merge_sort(lst)
    print(f'#{Test} {ret[N//2]} {cnt}')