# 우선순위 큐
# 언제 왜 사용하냐 ??
# 리스트 저장 - O(N)
# python  -> minheap default
import heapq

arr = []

heapq.heappush(arr,4)
heapq.heappush(arr,1)
heapq.heappush(arr,64)
heapq.heappush(arr,3)

print(arr)
for i in range(len(arr)) :
    print(heapq.heappop(arr),end = ' ')

# 리스트의 값을 heap 자료 구조로 바꾸기

arr = [32,21,6,4,1,4,3]
heap = []
# 방법 1
for i in range(len(arr)) :
    heapq.heappush(heap,arr[i])
    # arr 원본 보존하면서 우선순위 큐
for i in range(len(arr)) :
    print(heapq.heappop(heap))


# 방법 2 heapify (원본 -> heap)
heapq.heapify(arr)

for i in range(len(arr)) :
    print(heapq.heappop(arr))