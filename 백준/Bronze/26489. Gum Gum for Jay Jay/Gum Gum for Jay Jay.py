ans = 0
while True:
    try:
        temp = input()
        ans += 1
    except EOFError:
        break
print(ans)