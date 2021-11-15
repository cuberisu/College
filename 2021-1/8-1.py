# 자료구조 리스트, 튜플, 딕셔너리

#1
x = list()
y = []

print(x)
print(y,"\n")

#2
x = [1,2,3,4]
   # 0,1,2,3
y = ["Hello", "World"]
z = ["Bye", 1,2,3]

print(x)
print(y)
print(z)
print(x+y, "\n")    #합치기

#3
print(x[0])  # x의 0번째 자리 출력
print(x[3],"\n")

#4
x[3] = 10   #10 대입
print(x)  

# print(x[4])
# IndexError: list index out of range