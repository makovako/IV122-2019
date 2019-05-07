import random

def run(n,x,k):
    dices = [False] * (n)
    dices[random.randint(0,n-1)] = True # True is the unfair dice

    all_six = 0
    all_six_fair_dice = 0

    while True:
        dice = dices[random.randint(0,n-1)]
        six = 0
        for _ in range(x):
            if dice: # if its unfair
                six += 1
            elif random.randint(1,6) == 6:
                six += 1
        if six == x:
            all_six += 1
            if not dice:
                all_six_fair_dice += 1
        if all_six == k:
            break
    return all_six_fair_dice/all_six

n = 10
x = 5
k = 100000
print("p={}".format(run(n,x,k)))


n = 100
x = 3
k = 100000
print("p={}".format(run(n,x,k)))

n = 1000
x = 5
k = 10000
print("p={}".format(run(n,x,k)))