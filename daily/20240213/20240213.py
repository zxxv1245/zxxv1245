testcase=int(input())

def abc(level):
    global ans
    if level==n:
        ans+=1
        return
    for i in range(n):
        if used[i]==1: continue # 같은 열에 체크
        if RUP[level+i]==1 or RDOWN[i-level+n]==1: continue # 대각선 방향 체크

        used[i],RUP[level+i],RDOWN[i-level+n]=1,1,1
        abc(level+1)
        used[i],RUP[level+i],RDOWN[i-level+n]=0,0,0


for tc in range(1,testcase+1):
    ans=0
    n=int(input())
    used=[0]*n # 열 체크하는 배열
    RUP=[0]*(2*n) # 우상향 대각선 체크하는 배열
    RDOWN=[0]*(2*n) # 우하향 대각선 체크하는 배열

    abc(0)
    print(f'#{tc} {ans}')