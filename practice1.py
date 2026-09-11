import random
min_num = int(input('請輸入最小整數'))
max_num = int(input('請輸入最大整數'))
ans = random.randint(min_num,max_num)
print(ans)
count = 0
while True:
	qes = int(input('請輸入一個整數'))
	count += 1
	print('第',count,'次')
	if ans == qes:
		print('終於猜對了')
		break
	elif ans > qes:
		print('比答案大')
	elif ans < qes:
		print('比答案小')