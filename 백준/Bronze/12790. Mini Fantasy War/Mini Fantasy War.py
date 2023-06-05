import sys

T = int(sys.stdin.readline())

for _ in range(T):
    hp, mp, attack, defense, hp_change, mp_change, attack_change, defense_change = map(int, sys.stdin.readline().split())

    hp += hp_change
    mp += mp_change
    attack += attack_change
    defense += defense_change

    if hp < 1:
        hp = 1
    if mp < 1:
        mp = 1
    if attack < 0:
        attack = 0

    combat_power = 1 * hp + 5 * mp + 2 * attack + 2 * defense

    print(combat_power)
