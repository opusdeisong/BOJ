def calculate_minutes(t, e, f):
    return t * 3 + e * 20 + f * 120

t1, e1, f1 = map(int, input().split())
t2, e2, f2 = map(int, input().split())

max_minutes = calculate_minutes(t1, e1, f1)
mel_minutes = calculate_minutes(t2, e2, f2)

if max_minutes > mel_minutes:
    print("Max")
elif max_minutes < mel_minutes:
    print("Mel")
else:
    print("Draw")
