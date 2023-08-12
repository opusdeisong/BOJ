s = input()

pairs = s.count('RB') + s.count('BR')

if pairs % 2 == 1:
    print("Win")
else:
    print("Lose")
