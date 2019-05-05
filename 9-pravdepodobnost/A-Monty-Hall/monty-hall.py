import random

def play(strategy): # 0 - change, 1 - not change, 2 - random
    game = random.choice([(True,False,False),(False,True,False),(False,False,True)])
    choice = random.randint(0,2)
    other_doors = [0,1,2]
    other_doors.remove(choice)
    door1 = other_doors[0]
    door2 = other_doors[1]
    opened = 0
    if game[door1]:
        opened = door2
    elif game[door2]:
        opened = door1
    else:
        opened = random.choice(other_doors)
    if strategy == 0: # change
        l = [0,1,2]
        l.remove(opened)
        l.remove(choice)
        return game[l[0]]
    if strategy == 1: # not change
        return game[choice]
    if strategy == 2: # random
        l = [0,1,2]
        l.remove(opened)
        l.remove(choice)
        return game[choice] if random.choice([True,False]) else game[l[0]]

def test(strategy, tries):
    wins = 0
    for _ in range(tries):
        if play(strategy):
            wins += 1
    return wins/tries

strategies = ['change', 'not change', 'random']
tries = [100, 1000, 100000, 1000000]
for j in tries:
    print("Tries: {}".format(j))
    for strategy in range(3):
        print('For strategy {}, number of tries {}, success rate {}'.format(strategies[strategy],j,str(test(strategy,j))))