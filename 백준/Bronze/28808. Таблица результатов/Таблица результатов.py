n, m = map(int, input().split())

solved_tasks = 0

for _ in range(n):
    task_results = input().strip()
    if '+' in task_results:
        solved_tasks += 1

print(solved_tasks)
