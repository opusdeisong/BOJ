def check_number(a):
	if a =="A" or a == "B" or a == "C":
		return 3
	elif a =="D" or  a == "E" or a == "F":
		return 4
	elif a =="G" or a == "H" or a == "I":
		return 5
	elif a =="J" or a == "K" or a == "L":
		return 6
	elif a =="M" or a == "N" or a == "O":
		return 7
	elif a =="P" or a == "Q" or a == "R" or a == "S":
		return 8
	elif a =="T" or a == "U" or a == "V":
		return 9
	elif a =="W" or a == "X" or a == "Y" or a == "Z":
		return 10
dial = input()
root = 0
for i in range(len(dial)):
	root += check_number(dial[i])
	
print(root)