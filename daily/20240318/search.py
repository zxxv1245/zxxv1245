# 이진 검색 반복문
# def search(k) :
#     left = 0
#     right = N-1
#
#     while left <= right :
#         mid = (left + right) // 2
#
#         if lst[mid] == k :
#             return 1
#         if lst[mid] > k :
#             right = mid -1
#         elif lst[mid] < k :
#             left = mid + 1
#
#     return 0
# 기저 조건
    # 다음 재귀 들어가기 전엔 무엇을 해야할까?
    # 다음 재귀 함수 호출(파라미터)
    # 재귀 함수에서 돌아왔을 때 뭘해야할까?
def bsearch(k,left,right,preP) :
    if left > right :
        return 0

    mid = (left+right) // 2
    if lst[mid] == k :
        return 1
    if lst[mid] > k and preP != 1 :
        return bsearch(k,left,mid-1,1)
    elif lst[mid] < k and preP != 2:
        return bsearch(k,mid+1,right,2)

    return 0



T = int(input())

for Test in range(1,T+1) :
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    arr = list(map(int,input().split()))
    cnt = 0
    lst.sort()
    for i in arr :
        if bsearch(i,0,N-1,0) :
            cnt += 1
    print(f'#{Test} {cnt}')
