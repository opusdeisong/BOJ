score = list(map(int, input().split()))
ascending = sorted(score)
descending = sorted(score)
descending.reverse()

if score == ascending:
    print("ascending")
elif score == descending:
    print("descending")
else:
    print("mixed")