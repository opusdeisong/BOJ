import sys

def bmi_category(height, weight):
    bmi = weight / (height * height)
    if bmi > 25:
        return "Overweight"
    elif 18.5 <= bmi <= 25:
        return "Normal weight"
    else:
        return "Underweight"

weight = float(sys.stdin.readline())
height = float(sys.stdin.readline())

print(bmi_category(height, weight))
