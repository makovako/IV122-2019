import random
import matplotlib.pyplot as plt

Ka = [] # Higher number, higher probability
for i in range(1,7):
    for j in range(i):
        Ka.append(i)

Kb = [] # Lower number, lower probability
for i in range(1,7):
    for j in range(i):
        Kb.append(j+1)
Kb.sort()

# always choose Ka
def method1(n):
    total = 0
    for _ in range(n):
        total += random.choice(Ka)
    return total/n

# Each throw choose random dice
def method2(n):
    total = 0
    for _ in range(n):
        if random.choice([True,False]):
            total += random.choice(Ka)
        else:
            total += random.choice(Kb)
    return total/n

# Choose dice and throw n-times
def method3(n):
    total = 0
    K = []
    if random.choice([True,False]):
        K = Ka[:]
    else:
        K = Kb[:]
    for _ in range(n):
        total += random.choice(K)
    return total/n

# throw n times with a dice and calculate average
# repeat k times, get k averages
def simulate(n,k,method):
    averages = []
    for _ in range(k):
        averages.append(method(n))
    return averages

# Try different values for n and k, create histograms for different methods
for k in [10,100,1000]:
    for n in [10,1000,100000]:
        fig, axs = plt.subplots(1,3)
        fig.suptitle("n:{}, k:{}".format(n,k))
        fig.set_size_inches((12,6))
        axs[0].set_title("method1")
        axs[0].hist(simulate(n,k,method1),12,(1,6))
        axs[1].set_title("method2")
        axs[1].hist(simulate(n,k,method2),12,(1,6))
        axs[2].set_title("method3")
        axs[2].hist(simulate(n,k,method3),12,(1,6))

        plt.savefig("n-{}_k-{}.png".format(n,k))
