# MST = 최소신장트리
# 섬에 다리 건설, 광케이블 설치 등등
# Kruskal 알고리즘


# 최소 필요 간선 갯수 : 정점 갯수 - 1
# 사이클 발생하면 안됨... (그룹화 후 보스가 같으면 안됨 ?)

def findboss(m) :
    if not group[ord(m)] :
        return m
    ret = findboss(group[ord(m)])
    #group[ord(m)] = ret
    return ret
def union(a,b,i) :
    global cost,cnt
    aboss,bboss = findboss(a),findboss(b)
    if aboss == bboss :
        return
    cost += int(lst[i][2])  #그룹화 시킨 후 드는 비용 더하기
    cnt += 1 #그룹화 시킨 갯수 1증가
    group[ord(bboss)] = aboss

k = int(input()) # 정점의 개수
N = int(input()) # 간선의 갯수

lst = [list(map(int,input().split())) for _ in range(n)]

group= [0]*200

lst.sort(key = lambda x : int(x[2]))
cnt = 0
cost = 0
for i in range(n) :
    if cnt == k-1 : # 선택할 간선의 개수 = 정점의 개수 - 1
        print(cost)
        break
    union(lst[i][0],lst[i][1],i)


# 월말평가
# 명제 역 이 대우
# 비트연산 (2진수 => 16진수)
# 시간복잡도