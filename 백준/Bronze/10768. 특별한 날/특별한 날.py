mon = int(input())
date = int(input())
if mon < 2:
    print("Before")    
elif mon == 2:
    if date == 18: 
        print("Special")
    elif date < 18: 
        print("Before")
    else: 
        print("After")        
else: 
    print("After")