import sys


def max_people_on_train(people):
    current_people = 0
    max_people = 0

    for off, on in people:
        current_people = current_people - off + on
        if current_people > max_people:
            max_people = current_people

    return max_people

# test the function
people = [list(map(int, sys.stdin.readline().split())) for _ in range(4)]
print(max_people_on_train(people))
