import time
from math import pi,sqrt
from statistics import mean
import random

def leibniz(sec):
    start = time.time()
    time.clock()
    elapsed = 0
    k = 0
    loc_pi = (-1)**k / (2*k + 1)
    while elapsed < sec:
        elapsed = time.time() - start
        k +=1
        loc_pi = loc_pi + (-1)**k / (2*k + 1)
    return 4*loc_pi

def archim(sec):
    start = time.time()
    time.clock()
    elapsed = 0
    an = 2*sqrt(3)
    bn = 3
    while elapsed < sec:
        elapsed = time.time() - start
        an = (2*an*bn) / (an + bn)
        bn = (sqrt(an*bn))
    return (an,bn)

def monte_carlo(sec):
    start = time.time()
    time.clock()
    elapsed = 0
    n = m = 0
    while elapsed < sec:
        elapsed = time.time() - start
        if (random.random()*100)**2 + (random.random()*100)**2 <= 100**2:
            m += 1
        n += 1
    return 4*m / n

delta = ([],[],[],[])

for i in range(10):
    pi_leibnitz = leibniz(1)
    delta_leibnitz = abs(pi - pi_leibnitz)
    delta[0].append(delta_leibnitz)

    pi_archim = archim(1)
    delta_archim = (abs(pi - pi_archim[0]),abs(pi - pi_archim[1]))
    delta[1].append(delta_archim[0])
    delta[2].append(delta_archim[1])

    pi_monte_carlo = monte_carlo(1)
    delta_monte_carlo = abs(pi - pi_monte_carlo)
    delta[3].append(delta_monte_carlo)

    print("Pi leibnitz {}, pokus {} / 10 , 1 sekunda, rozdiel oproti math pi {}".format(pi_leibnitz,i+1,delta_leibnitz))
    print("Pi archim an {}, pokus {} / 10, 1 sekunda, rozdiel oproti math pi {}".format(pi_archim[0],i+1, delta_archim[0]))
    print("Pi archim bn {}, pokus {} / 10, 1 sekunda, rozdiel oproti math pi {}".format(pi_archim[1],i+1,delta_archim[1]))
    print("Pi monte carlo {}, pokus {} / 10, 1 sekunda, rozdiel oproti math pi {}".format(pi_monte_carlo,i+1,delta_monte_carlo))

names = ["leibnitz","archim (an)","archim (bn)", "monte carlo"]
average_delta = []
for i in range(4):
    average_delta.append(mean(delta[i]))
    print("Priemerny rozdiel pre metodu {} je {}".format(names[i],average_delta[i]))
    
print("Najlepsia metoda je",names[average_delta.index(min(average_delta))])
print("Na mojom pocitaci vysla archimedova rada")
