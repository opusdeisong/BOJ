import sys

def find_min_ticket(N, sold_tickets):
    sold_tickets_set = set(sold_tickets)
    ticket_number = 1
    while ticket_number in sold_tickets_set:
        ticket_number += 1
    return ticket_number

N = int(sys.stdin.readline())
sold_tickets = list(map(int, sys.stdin.readline().split()))
sold_tickets_set = set(sold_tickets)
ticket_number = 1
while ticket_number in sold_tickets_set:
    ticket_number += 1
print(ticket_number)