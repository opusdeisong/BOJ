import sys

def judgement(m):
    if m >= 8:
        return "satisfactory"
    else:
        return "unsatisfactory"

m, n = map(int, sys.stdin.readline().split())
clauses = []
for _ in range(m):
    clause = list(map(int, input().split()))

if m >= 8:
    print("satisfactory")
else:
    print("unsatisfactory")