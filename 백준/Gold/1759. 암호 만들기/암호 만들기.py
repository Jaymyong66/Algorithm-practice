from itertools import combinations

def condition(lst):
    vowels = [v for v in lst if v in vols]
    cons = [v for v in lst if v not in vols]

    return vowels, cons

def check(row):
    global vowels, cons

    if len([v for v in row if v in vowels]) >= 1 and len([v for v in row if v in cons]) >= 2:
        return True

    return False

vols = ['a', 'e', 'i', 'o', 'u']

L, C = list(map(int, input().split()))
strings = sorted(input().split())

vowels, cons = condition(strings)

for comb in combinations(strings, L):
    if check(comb):
        for u in comb:
            print(u, end='')
        print()