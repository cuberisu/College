nums = [100, 200, 300, 400, 500]
del nums[3] #0~4번째 원소 중 3번째, 즉 400을 없애라
# del nums[4] 에러발생! 3번째 값을 지웠기 때문에 이제 4번째 값이 없어진 상태가 되었기 때문이다.
print(nums)