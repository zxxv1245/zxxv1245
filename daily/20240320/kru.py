k=int(input()) #정점의 개수
n=int(input()) #간선정보의 개수
lst=[list(input().split()) for _ in range(n)]
group=[0]*200

lst.sort(key=lambda x:int(x[2]))

def findboss(m):
    if group[ord(m)]==0:
        return m
    ret=findboss(group[ord(m)])
    #group[ord(m)]=ret
    return ret

def union(a,b,i):
    global total_cost,cnt
    aboss,bboss=findboss(a),findboss(b)
    if aboss==bboss:
        return
    total_cost+=int(lst[i][2])  # 그룹화 시킨후 드는 비용 더하기
    cnt+=1                      # 그룹화 시킨 갯수 1증가 (두 정점을 연결)
    group[ord(bboss)]=aboss

cnt=0                           # 두 정점을 연결 시킬 때(그룹화) 마다 1씩 증가
total_cost=0
for i in range(n):
    if cnt==k-1:                #선택할 간선의개수 = 정점의 개수 - 1개
        print(total_cost)
        break
    union(lst[i][0],lst[i][1],i)


'''
5
8
C D 1
A C 3
C E 5
A E 7
A B 9
B D 11
B C 14
A D 20
'''

