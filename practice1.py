import random
ans = random.randint(1,100)
print(ans)
while True:
	qes = int(input('請輸入一個整數'))
	if ans == qes:
		print('終於猜對了')
		break
	elif ans > qes:
		print('比答案大')
	elif ans < qes:
		print('比答案小')