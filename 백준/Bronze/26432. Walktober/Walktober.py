import sys

T = int(sys.stdin.readline())

for t in range(1, T + 1):
    M, N, P = map(int, sys.stdin.readline().split())
    steps = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

    total_additional_steps = 0

    for day in range(N):
        max_steps = 0
        johns_steps = steps[P - 1][day]

        for participant in range(M):
            max_steps = max(max_steps, steps[participant][day])

        total_additional_steps += max(0, max_steps - johns_steps)

    print(f'Case #{t}: {total_additional_steps}')
