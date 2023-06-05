import sys

n = int(sys.stdin.readline())
cy_score, sd_score = 100, 100

for _ in range(n):
    cy, sd = map(int, sys.stdin.readline().split())
    if cy > sd:
        sd_score -= cy
    elif cy < sd:
        cy_score -= sd

print(cy_score)
print(sd_score)
