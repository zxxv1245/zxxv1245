# 연습문제 1번

lst = [1,2,3]  # 3개의 데이터 리스트

STACK = [] # 빈 스택(STACK) 리스트 생성

for i in lst :   # 리스트를 반복문으로 돌면서
    STACK.append(i)   # 하나씩 STACK에 집어넣음 ex) STACK = [1]  => STACK = [1,2]  => STACK = [1,2,3]

while STACK :   # STACK에 데이터가 들어 있는 동안 반복문을 돔(STACK 이 []가 될 때까지)
    a = STACK.pop() # STACK에서 하나씩 pop
    # 시작이 STACK = [1,2,3]이 였으니까 pop 하면 뒤에서 하나 빼서 a = 3 이 되고 STACK은 [1,2]가 됨
    # 다음은 a = 2 , STACK = [1]
    # 다음은 a = 1 , STACK = []
    print(a) # 출력 결과 3 2 1
    # STACK = [] 이므로 반복문 종료