import sys

T = int(sys.stdin.readline())
num_list = set()
for _ in range(T):
    func = sys.stdin.readline().split()
    if len(func) != 1:
        func, num = func[0], func[1]
        num = int(num)
    else:
        func = func[0]
    if func == "add":
        if num not in num_list: num_list.add(num)
    elif func == "remove":
        if num in num_list: num_list.remove(num)
    elif func == "check":
        if num in num_list: print(1)
        else: print(0)
    elif func == "toggle":
        if num in num_list: num_list.remove(num)
        else: num_list.add(num)
    elif func == "all": num_list = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    elif func == "empty": num_list.clear()