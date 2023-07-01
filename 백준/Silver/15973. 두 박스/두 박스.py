x1, y1, x2, y2 = map(int, input().split())
_x1, _y1, _x2, _y2 = map(int, input().split())

if x1 > _x1:
    x1, _x1 = _x1, x1
    y1, _y1 = _y1, y1
    x2, _x2 = _x2, x2
    y2, _y2 = _y2, y2

if x2 == _x1:
    if y2 == _y1 or y1 == _y2:
        print("POINT")
    else:
        print("LINE")
elif x2 > _x1:
    if y2 < _y1 or y1 > _y2:
        print("NULL")
    elif y2 == _y1 or y1 == _y2:
        print("LINE")
    # If boxes overlap
    else:
        print("FACE")
elif x2 < _x1:
    print("NULL")
