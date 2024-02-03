import sys


def max_area_histogram(heights):
    stack = [-1]
    max_area = 0

    for i, h in enumerate(heights):
        while stack[-1] != -1 and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area

N = int(sys.stdin.readline())
h = [0] + [int(sys.stdin.readline()) for _ in range(N)] + [0]

print(max_area_histogram(h))