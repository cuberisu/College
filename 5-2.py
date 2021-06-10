# 불리언 2nd

x = 3

#1
if x > 2:       #x가 2보다 클 때 Hello 출력  << if문에서는 조건 다음에 colon(:)을 꼭 붙이기
    print("Hello","\n")
  
#2
if x > 5:       #x가 5보다 크면 Hello
    print("Hello","\n")
else:           #아무것도 아니면 Hi  << else, elif는 들여쓰기 하면 xxxx 
    print("Hi","\n")
    
#3
if x > 5:       #x가 5보다 크면 Hello
    print("Hello","\n")
elif x == 3:    #(else if) 아니면 x = 3일 때 bye  << if문에서 equal 표시는 ==
    print("bye","\n")
else:           #아무것도 아니면 Hi
    print("Hi","\n")