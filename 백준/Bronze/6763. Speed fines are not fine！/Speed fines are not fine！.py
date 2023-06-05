import sys

speed_limit = int(sys.stdin.readline())
recorded_speed = int(sys.stdin.readline())

speed_diff = recorded_speed - speed_limit

if speed_diff <= 0:
    print("Congratulations, you are within the speed limit!")
elif speed_diff <= 20:
    print("You are speeding and your fine is $100.")
elif speed_diff <= 30:
    print("You are speeding and your fine is $270.")
else:
    print("You are speeding and your fine is $500.")