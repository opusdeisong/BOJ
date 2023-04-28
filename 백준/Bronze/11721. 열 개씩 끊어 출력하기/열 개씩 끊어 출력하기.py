word = input()
for i in range(len(word)):
    print(word[i], end="")
    if i % 10 == 9:
        print("")