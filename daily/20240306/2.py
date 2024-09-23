# 연습문제 2번
# ()()((())) case 1
# ((()((((()()((()())((()))))) case 2
# 여기 있는 case는 둘 다  '('가 먼저 나오기 때문에 ')' 가 먼저 나오는 경우는
# 고려하지 않았어, ')' 가 먼저 나오면 어떻게 해야할까 생각해봐


# case 1
lst = '()()((()))'
STACK = []  # 빈 STACK 리스트 생성
for i in lst : # 데이터(문자열)을 반복문으로 돌며
    if i == '(' : # 만약 '(' 여는 괄호라면
        STACK.append(i) # STACK에 넣음
    elif i == ')' : # 만약 ')' 닫는 괄호라면
        STACK.pop() # STACK에서 마지막에 있는 '('를 제거함
                    # 이유 : 앞에서 말했듯이 여기 있는 case들은
                    # '('가 먼저 나오기 때문에 ')'가 나오면 필연적으로 STACK에 '('가 있을 수 밖에 없음
# 위 반복문 진행 순서 : STACK = ['('] => STACK = [] => STACK = ['('] => STACK = [] =>
# STACK = ['('] => STACK = ['(','('] => STACK = ['(','(','('] => STACK = ['(','('] =>
# STACK = ['('] => STACK = []

if STACK :    # STACK = [] 이기 때문에  if문은 False 임(즉, 정상적인 괄호쌍임)
    print('비정상적인 괄호쌍입니다.')
else :
    print('정상적인 괄호쌍입니다.')

# case2 #위에 꺼랑 똑같은 논리니까 돌려보고

# lst = '((()((((()()((()())((())))))'
#
# st = []
#
# for i in lst :
#     if i == '(' :
#         st.append(i)
#     else :
#         st.pop()
#
# if st :
#     print('비정상')
# else :
#     print('정상')