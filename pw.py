pw = 'a123456'
count = 3
while True:
	entry = input('請輸入密碼')
	if entry == pw:
		print('登入成功')
		break
	else:
		count = count - 1
		if count > 0:
			print('密碼錯誤！還有',count,'次機會')
		else:
			break