import copy
import heapq
import sys

with open(sys.argv[1]) as f:
    boss_hitpoints = int(f.readline().strip().split(' ')[-1])
    boss_damage    = int(f.readline().strip().split(' ')[-1])

spells = ['magic missile', 'drain', 'shield', 'poison', 'recharge']


class State():
    def __init__(self):
        self.pc_hp = 50
        self.pc_mana = 500
        self.boss_hp = boss_hitpoints
        self.boss_dmg = boss_damage
        self.active_effects = {
            'shield': 0,
            'poison': 0,
            'recharge': 0
        }
        self.used_mana = 0
    
    def __str__(self):
        return "{%d}  (HP: %d, MP: %d) vs (HP: %d)  [S: %d, P: %d, R: %d]" % (self.used_mana, self.pc_hp, self.pc_mana, self.boss_hp, self.active_effects['shield'], self.active_effects['poison'], self.active_effects['recharge'])

    def __lt__(self, rhs):
        return self.used_mana < rhs.used_mana


heap = []
heapq.heappush(heap, State())

while heap:
    state = heapq.heappop(heap)

    ## Part 2 -->
    state.pc_hp -= 1
    if state.pc_hp <= 0:
        continue
    ## <-- Part 2

    ## Start of player turn: apply effects
    if state.active_effects['poison'] > 0:
        state.boss_hp -= 3
    if state.active_effects['recharge'] > 0:
        state.pc_mana += 101

    ## Decrease active effects' timers
    state.active_effects = {k:max(0,v-1) for [k,v] in state.active_effects.items()}

    if state.boss_hp <= 0:
        print(state.used_mana)
        #print("  Player wins!")
        break
    elif state.pc_hp <= 0:
        #print("  Player is dead!")
        continue

    ## Player loses if out of mana
    if state.pc_mana < 53:
        #print("  Out of mana!")
        continue

    ## Player chooses action: branching point
    new_states = []

    ## Magic missile
    if state.pc_mana >= 53:
        s = copy.deepcopy(state);
        s.boss_hp -= 4
        s.pc_mana -= 53
        s.used_mana += 53
        if s.boss_hp <= 0:
            print(s.used_mana)
            #print("  Player wins!")
            break
        new_states.append(s)

    ## Drain
    if state.pc_mana >= 73:
        s = copy.deepcopy(state);
        s.boss_hp -= 2
        s.pc_hp = min(s.pc_hp + 2, 50)
        #s.pc_hp += 2
        s.pc_mana -= 73
        s.used_mana += 73
        if s.boss_hp <= 0:
            print(s.used_mana)
            #print("  Player wins!")
            break
        new_states.append(s)

    ## Shield
    if state.pc_mana >= 113 and state.active_effects['shield'] == 0:
        s = copy.deepcopy(state);
        s.pc_mana -= 113
        s.used_mana += 113
        s.active_effects['shield'] = 6
        new_states.append(s)

    ## Poison
    if state.pc_mana >= 173 and state.active_effects['poison'] == 0:
        s = copy.deepcopy(state);
        s.pc_mana -= 173
        s.used_mana += 173
        s.active_effects['poison'] = 6
        new_states.append(s)

    ## Recharge
    if state.pc_mana >= 229 and state.active_effects['recharge'] == 0:
        s = copy.deepcopy(state);
        s.pc_mana -= 229
        s.used_mana += 229
        s.active_effects['recharge'] = 5
        new_states.append(s)


    for s in new_states:
        ## Start of boss turn: apply effects
        if s.active_effects['poison'] > 0:
            s.boss_hp -= 3
        if s.active_effects['recharge'] > 0:
            s.pc_mana += 101

        ## Decrease active effects' timers
        s.active_effects = {k:max(0,v-1) for [k,v] in s.active_effects.items()}

        if s.boss_hp <= 0:
            print(s.used_mana)
            #print("  Player wins!")
            exit(0)

        ## Boss attacks
        if s.active_effects['shield'] > 0:
            s.pc_hp -= max(1, s.boss_dmg - 7)
        else:
            s.pc_hp -= max(1, s.boss_dmg)

        heapq.heappush(heap, s)

