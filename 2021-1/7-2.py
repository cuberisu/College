# 반복문 : for, while
# break, continue
print("철수: 안녕 영희야 뭐해?")
print("영희: 안녕 철수야, 숨만 쉬고 있어.")


# for~ range
for i in range(10):     #10번 반복
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")


# continue: 건너뛰기
i = 0
for i in range(5):          # 지금이 몇 번째인지 변수 i에 넣어라.  range(5)는 5번 반복해라.
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    
    if i == 1:
      continue              # i = 1일 때 뒤의 코드는 건너뛰고 바로 다음 루프로 간다.
    
    print("정수: 어이 친구들.. 안녕")  # i = 1일 때 출력되지 않는다.


# break: 루프 종료
i = 0
for i in range(100):
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1
        
    if i > 2 :  #i = 2가 최대값이 된다.
      break     #총 3번 출력하고 루프를 종료한다.

# while
i = 0
while i < 3:              # i 가 3보다 작으면
    print(i)  
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1

# 무한루프 [빠져나오기: Ctrl+C]
""" i = 0
while True:
    print(i)
    print("철수: 안녕 영희야 뭐해?")
    print("영희: 안녕 철수야, 그냥 있어.")
    i = i + 1 """
        
"""     if i > 2 :
      break """
