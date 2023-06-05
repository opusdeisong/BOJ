import sys

N = int(sys.stdin.readline())
score = list(map(int, sys.stdin.readline().split()))
sum_score = 0
cont_score = 0
for s in score:
    if s == 1:
        cont_score += 1
        sum_score += cont_score
    else:
        cont_score = 0
print(sum_score)
