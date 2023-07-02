rotation = 0

for _ in range(10):
    ti = int(input())
    if ti == 1:
        rotation += 1
    elif ti == 2:
        rotation += 2
    elif ti == 3:
        rotation -= 1

final_rotation = rotation % 4

if final_rotation == 0:
    print("N")
elif final_rotation == 1:
    print("E")
elif final_rotation == 2:
    print("S")
else:
    print("W")
