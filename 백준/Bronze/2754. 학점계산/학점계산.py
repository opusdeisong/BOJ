point = input()

if point[0] == "A":
    score = 4.0
    if point[1] == "+":
        score += 0.3
    elif point[1] == "-":
        score -= 0.3
elif point[0] == "B":
    score = 3.0
    if point[1] == "+":
        score += 0.3
    elif point[1] == "-":
        score -= 0.3
elif point[0] == "C":
    score = 2.0
    if point[1] == "+":
        score += 0.3
    elif point[1] == "-":
        score -= 0.3
elif point[0] == "D":
    score = 1.0
    if point[1] == "+":
        score += 0.3
    elif point[1] == "-":
        score -= 0.3
else:
    score = 0.0
print(score)
