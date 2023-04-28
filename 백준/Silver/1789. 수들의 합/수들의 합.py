def calc(i):
    return (i * (i + 1)) // 2
num = int(input())
i = 1
while calc(i) < num:
    i += 1
if calc(i) == num:
    print(i)
else:
    print(i - 1)