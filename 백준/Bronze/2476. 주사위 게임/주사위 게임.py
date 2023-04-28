T = int(input())
score = []
for i in range(T):
    A, B, C = map(int, input().split())
    if A == B == C:
        score.append(10000 + A * 1000)
    elif A == B or B == C:
        score.append(1000 + B * 100)
    elif A == C:
        score.append(1000 + A * 100)
    else:
        score.append(100 * max(A, B, C))
        
print(max(score))