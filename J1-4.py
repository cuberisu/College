""" rate=1150
switch_money=50000
c=rate*switch_money
 """

won=int(input("원화 금액 입력: "))
exchange_rate=int(input("환율 입력: "))
tran_rate=int(won/exchange_rate)
print("환산 금액:",tran_rate,"달러")
