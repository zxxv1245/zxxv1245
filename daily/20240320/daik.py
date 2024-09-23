# 다익스트라 알고리즘
# 최단경로 최소비용 구할 때 사용
# 최소 비용 : 다익스트라
# DFS, BFS으로도 풀 수 있음

# 다익스트라 조건, 시작점이 정해져 있어야 한다.
# 비용(cost)가 음수가 나오면 안된다.
# 시작점은 정해져있으나 간선의 정보에 음수가 있으면 => bellmanford (but음의 사이클이 존재하지 않아야한다.)
                                                            # 사이클을 돌았을 때 비용의 합이 음수면 벨만포드도 불가능

# if 시작점이 정해져있지 않다면 => floyd warshall  시간 복잡도 :O(N**3)
# (한 정점에서 다른 모든 정점까지의 최소비용)

# 다익스트라 2가지 방법(2개 원리는 같음)
# 오리지날   O(N**2)
# 개선된 다익스트라 O(NlogN)
# 차이점
# 1. 개선된 다익스트라는 경유지를 구할 때 우선순위 큐를 사용해서 더 빠른 속도를 낼 수 있음
# 2. 그래프를 인접행렬이 아닌 인접 리스트로 표현을 함

def select_ky() :
    minV = 21e8
    minP = 0
    for i in range(5) :
        if used[i] == 0 and minV > result[i]  :
            minV = result[i]
            minP = i
    return minV


name = 'ABCDE'
arr = []
used = [0]*5
used[0] = 1
result = [0,0,0,0,0] # 시작점에서 다른 정점 갱신 하는 리스트

def dijkstra() :
    # 경유지 선택
    for i in range(4) :   # 시작점 제외 하고 반복
        via = select_ky()    # 경유지 함수
        used[via] = 1
    # 시작 -> 도착  vs 시작 -> 경유 -> 도착 (비교 후 result에 갱신)
    # 바로 vs 경유

    for j in range(5) :
        baro = result[j]
        ky = result[ky]+arr[via][j]  # 시작 > 경우 + 경유  - > 다른 정점
        if baro > ky :
            result[j] = ky  # 경유지를 통해서 가는 비용으로
            # result 배열을 갱신
