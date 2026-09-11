data = []
words = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())
		words += len(line)
		if len(data) % 1000 == 0:
			print(len(data))
print('已經讀完檔案了,總共是', len(data), '筆')
print('留言平均長度為', words/len(data))