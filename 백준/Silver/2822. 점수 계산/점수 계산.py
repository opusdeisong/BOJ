T = 8
score = []
sort_score = []
rank =[]
for i in range(T):
    num = int(input())
    score.append(num)
sort_score = (sorted(score))
sort_score.reverse()
print(sum(sort_score[0:5]))
for i in sort_score[0:5]:
    rank.append(score.index(i) + 1)
rank.sort()
for i in rank:
    print(i, end=" ")