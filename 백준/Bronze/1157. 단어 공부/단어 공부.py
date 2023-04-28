W = input().upper()
word = list(set(W))

cnt = []
for i in word:
	count = W.count
	cnt.append(count(i))
	
if cnt.count(max(cnt)) > 1:
	print("?")
else:
	print(word[(cnt.index(max(cnt)))])
