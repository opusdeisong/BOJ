def find_sum(A):
    list = []
    for i in range(2, A):
        if A % i == 0:
            list.append(i)
    if sum(list) + 1 != A:
        print(f"{A} is NOT perfect.", end="")
    else:
        print(f"{A} = 1 ", end="")
        for i in list:
            print(f"+ {i} ", end="")


while True:
    A = int(input())
    if A == -1:
        break
    else:
        find_sum(A)
        print("")