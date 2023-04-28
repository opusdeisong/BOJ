import sys

input = sys.stdin.readline

N, M = map(int, input().split())
list = list(map(int, input().split()))

start = 1
end = sum(list)
answer = 0


def Search():
    global start, end, answer
    mid = (start + end) // 2
    total_length = mid
    cnt = 1

    for length in (list):
        if length > mid:
            start = mid + 1
            return
        elif total_length - length < 0:
            total_length = mid
            cnt += 1
        total_length -= length

    if cnt > M:
        start = mid + 1
    elif cnt <= M:
        end = mid - 1
        answer = mid


while start <= end:
    Search()

print(answer)