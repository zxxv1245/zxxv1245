# 개선된 데이크스트라

# 필수 : 시작 -> 정점
# 시작 -> 경유 -> 정점

'''
5 7
0 1 3
0 4 5
0 3 9
1 4 1
1 2 7
2 3 1
4 2 1
0 3           # 시작/도착
'''
# 0 -> 3 까지 최소 비용은?


# 1. 초기설정 result
# 2. heap 만들고 시작점을 첫번째 경유지로 놓기
# 2-1. heap이 없어질때까지 반복
# 3. heap 에서 비용이 가장 작은 것을 그다음 경유지로 선택
# 4. 시작 -> 도착 vs 시작 -> 경유 -> 도착 (비교 )
# 5. 경유지 들리는 것이 더 싸다면 heappush 후 result 갱신

import heapq
N,M = map(int,input().split())
arr = [[] for _ in range(N)]
for _ in range(M) :
    a,b,c = map(int,input().split())
    arr[a].append((c,b))

start,end = map(int,input().split())

result = [21e8]*N
result[start] = 0
heap = [(0,start)]

while heap :
    price,ky = heapq.heappop(heap)

    if price > result[ky] : continue

    for next_price,next in arr[ky] :
        baro=result[next]
        new_price = price + next_price

        if baro > new_price :
            result[next] = new_price
            heapq.heappush(heap,(new_price,next))

print(*result)