import sys

input = sys.stdin.readline

MAX = 10 ** 12
a = []


def d(a1, a2):  # 두 점 사이의 거리
    return (a1[0] - a2[0]) ** 2 + (a1[1] - a2[1]) ** 2


n = int(input())
for i in range(n):
    a.append(list(map(int, input().split())))

ans = [MAX, 0]  # [거리, 인덱스]
for i in range(n):  # 가장 가까운 편의시설: a[i]
    m = 0
    for j in range(n):  # 가장 먼 편의시설을 찾음
        if i == j: continue

        m = max(m, d(a[i], a[j]))
    if m < ans[0]:  # ans 갱신
        ans = [m, i]

print(a[ans[1]][0], a[ans[1]][1])