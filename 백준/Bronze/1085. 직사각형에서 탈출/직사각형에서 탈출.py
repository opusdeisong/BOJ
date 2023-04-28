x, y, w, h = map(int, input().split())
distance = []
distance. append(abs(0 - x))
distance. append(abs(w - x))
distance. append(abs(0 - y))
distance. append(abs(h - y))
print(min(distance))