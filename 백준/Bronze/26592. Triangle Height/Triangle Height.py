T = int(input())
for _ in range(T):
    a, b = map(float, input().split())
    print(f"The height of the triangle is {a * 2 / b:.2f} units")