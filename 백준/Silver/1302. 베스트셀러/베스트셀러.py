import sys
N = int(sys.stdin.readline())
book = []
sell_record = []
ans = []
for _ in range(N):
    temp = input()
    if temp not in book:
        book.append(temp)
        sell_record.append(1)
    else:
        sell_record[book.index(temp)] += 1
for i in range(len(sell_record)):
    if sell_record[i] == max(sell_record):
        ans.append(book[i])

print(sorted(ans)[0])