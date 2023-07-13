while True:
    transaction = input().split()
    balance = int(transaction[0])
    action = transaction[1]
    amount = int(transaction[2])
    
    if balance == 0 and action == "W" and amount == 0:
        break

    if action == "D":
        balance += amount
    elif action == "W":
        if balance - amount < -200:
            print("Not allowed")
            continue
        else:
            balance -= amount

    print(balance)
