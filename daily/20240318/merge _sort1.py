def merge_sort(start,end) :
    global cnt

    mid = (start+end) // 2
    if (start+end) % 2 == 0 : # 길이가 홀수 일 때  mid 값 조정
        mid -= 1

    if start == end : #기저조건
        return

    merge_sort(start,mid)   #left
    merge_sort(mid+1,end)   #right 라고 생각하자

    if lst[mid] > lst[end] : #왼쪽의 끝값 mid, 오른쪽의 끝값 end ?
        cnt += 1

    i = start    # 양쪽 시작 값
    j = mid + 1   # 상동
    result = []

    while True :
        if i > mid and j > end :  # 각각의 끝값보다 크면? 종료
            break
        if i > mid :
            result.append(lst[j])
            j += 1
        elif j > end :
            result.append(lst[i])
            i += 1
        elif lst[i] <= lst[j] :
            result.append(lst[i])
            i += 1
        elif lst[i] > lst[j] :
            result.append(lst[j])
            j += 1
    for i in range(len(result)):  # 하나로 합쳐진 result 배열의 값을 arr 배열로 옮기기
        lst[start + i] = result[i]



T = int(input())

for Test in range(1,T+1) :
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0
    merge_sort(0,N-1)
    print(f'#{Test} {lst[N//2]} {cnt}')