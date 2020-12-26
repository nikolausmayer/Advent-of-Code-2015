import sys

shop = {
    'weapons': [
        [ 8, 4, 0],
        [10, 5, 0],
        [25, 6, 0],
        [40, 7, 0],
        [74, 8, 0]
    ],
    'armor': [
        [  0, 0, 0],
        [ 13, 0, 1],
        [ 31, 0, 2],
        [ 53, 0, 3],
        [ 75, 0, 4],
        [102, 0, 5]
    ],
    'rings': [
        [  0, 0, 0],
        [  0, 0, 0],
        [ 25, 1, 0],
        [ 50, 2, 0],
        [100, 3, 0],
        [ 20, 0, 1],
        [ 40, 0, 2],
        [ 80, 0, 3]
    ],
}

with open(sys.argv[1]) as f:
    boss_hitpoints = int(f.readline().strip().split(' ')[-1])
    boss_damage    = int(f.readline().strip().split(' ')[-1])
    boss_armor     = int(f.readline().strip().split(' ')[-1])
boss = [boss_hitpoints, boss_damage, boss_armor]

pc_hitpoints = 100
pc_damage = 0
pc_armor = 0

def play(pc, boss):
    while True:
        boss[0] -= max(1, pc[1]-boss[2])
        if boss[0] <= 0:
            return True
        pc[0] -= max(1, boss[1]-pc[2])
        if pc[0] <= 0:
            return False

maxbudget = None

for weapon in range(len(shop['weapons'])):
    for armor in range(len(shop['armor'])):
        for ring1 in range(len(shop['rings'])-1):
            for ring2 in range(ring1+1, len(shop['rings'])):
                budget = shop['weapons'][weapon][0] + \
                         shop['armor'][armor][0] + \
                         shop['rings'][ring1][0] + \
                         shop['rings'][ring2][0]
                if maxbudget is not None and budget < maxbudget:
                    continue

                pc = [100,
                      shop['weapons'][weapon][1] + \
                      shop['armor'][armor][1] + \
                      shop['rings'][ring1][1] + \
                      shop['rings'][ring2][1],
                      shop['weapons'][weapon][2] + \
                      shop['armor'][armor][2] + \
                      shop['rings'][ring1][2] + \
                      shop['rings'][ring2][2]]

                if not play(pc, boss[:]):
                    if maxbudget is None or budget > maxbudget:
                        maxbudget = budget

print(maxbudget)

