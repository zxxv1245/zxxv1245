arr = [0]*200

def findboss(member) :
    global arr
    if arr[ord(member)] == 0 :
        return member

    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret

def UNION(a,b) :
    fa,fb = findboss(a),findboss(b) # 그룹화 시킬 a와 b의 보스를 찾기
    if fa==fb:  # 두 보스가 같다면 .. 이미 같은 그룹이라면
        return # 그룹화 중지( 의미 없음, 이미 같은 그룹이기 떄문에)
    arr[ord(fb)] = fa

# chr ( 아스키 > 문자열?)


UNION('A','B')
UNION('D','E')
UNION('B','E')
UNION('B','D')
UNION('E','F')

# 문자 2개 입력을 받으면
# 그 2문자가 서로 같은 그룹인지
# 다른 그룹인지 출력하기

