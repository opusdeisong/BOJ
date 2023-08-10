N = int(input())

votes = list(map(int, input().split()))

approve = votes.count(1)
reject = votes.count(-1)
abstain = votes.count(0)
if abstain > N/2:
    print("INVALID")
elif approve > reject:
    print("APPROVED")
else:
    print("REJECTED")
