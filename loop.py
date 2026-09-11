data = []
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())
		if len(data) % 1000 == 0:
			print(len(data))
print(data[0])
print(data[1])