import sys

while True:
    weight_earth = float(sys.stdin.readline())
    if weight_earth < 0:
        break
    weight_moon = weight_earth * 0.167
    print('Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.'.format(weight_earth, weight_moon))
