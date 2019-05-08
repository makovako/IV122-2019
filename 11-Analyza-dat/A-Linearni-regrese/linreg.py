import matplotlib.pyplot as plt
import random
import numpy as np
from numpy import arange

def mean(x):
    return sum(x)/len(x)

def read_data(filename):
    x = []
    y = []

    with open(filename,'r') as f:
        for line in f:
            line = line.split(' ')
            x.append(float(line[0]))
            y.append(float(line[1]))
    return(x,y)

# compute a and b based on formula in slides
def compute_analyt_solution(x, y):
    n = len(x)
    an = n * sum([a*b for a,b in zip(x,y)]) - sum(x)*sum(y) # numerator for a (citatel)
    ad = n * sum([a**2 for a in x]) - sum(x)**2 # denominator for a (menovatel)

    a = an/ad
    b = mean(y) - a * mean(x)

    return (a,b)

# x, y - lists of values
# orig = (a,b) - original a b values, from which x,y were generated, None if not known
# ax - plot from plt

def draw_solution(x, y, orig, ax):
    a,b = compute_analyt_solution(x,y)
    ax.plot(x,y,'bo')
    p1 = [min(x), a*min(x) + b] # left point of the line
    p2 = [max(x), a*max(x) + b] # right point of the line
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],'r',label='Computed linear regression') # red line - computed linear regression
    if orig is not None:
        a,b = orig
        p1 = [min(x), a*min(x) + b] # left point of the original line
        p2 = [max(x), a*max(x) + b] # right point of the original line
        ax.plot([p1[0],p2[0]],[p1[1],p2[1]],'g', label='Original line') # green line - original line
        ax.set_aspect('equal','datalim') # make the plot nice square with uniform aspect ratio


def generate_data(a,b,samples=20,error=0):
    x = [x for x in range(0-samples//2,0+samples//2+1,1)] # generate from 0-half of sample to 0+half of sample, +1 because of range function behavior
    y = [a*x+b + np.random.normal(0,error) for x in x] # generate y based on a, x and b, + some error from normal distribution
    return (x,y)

def square_sum(a,b,x,y):
    total = 0
    for i in range(len(x)):
        total += (y[i]-(a*x[i] + b))**2
    return total

def compute_grid_search(x,y,count_a, count_b,ax):
    min_y = min(y)
    max_y = max(y)
    delta_b = (max_y - min_y) / count_b
    b_set = [b for b in arange(min_y,max_y+delta_b,delta_b)]
    delta_a = (max_y - min_y) / count_a
    a_set = [a/2 for a in arange(min_y,max_y+delta_a,delta_a)] # /2 looked nicer
    ax.plot(x,y,'bo')
    # get current axes, so i can recreate them at the end
    min_x,max_x = ax.get_xlim()
    min_y,max_y = ax.get_ylim()
    lines = [] # [a, b, their sse]
    for b in b_set:
        for a in a_set:
            lines.append([a,b,square_sum(a,b,x,y)])
    max_sse = max([sse for _,_,sse in lines])
    for a,b,sse in lines:
        color = str(sse**(1/2) / (max_sse**(1/2))) # square root for smaller range of values
        ax.plot([min_x,max_x],[a*min_x + b,a*max_x + b],color=color,linewidth=1.0)
    ax.set_ylim([min_y,max_y])
    ax.set_xlim([min_x,max_x])


# filename_in - input file with points
# filename_out - output png file
def given_data_analyt(filename_in, filename_out):
    x,y = read_data(filename_in)
    fig,axs = plt.subplots(1,1)
    fig.suptitle("linreg.txt, analytical solution")
    fig.set_size_inches(10,10)
    draw_solution(x,y,None,axs)
    plt.legend()
    plt.savefig(filename_out)

def given_data_grid_search(filename_in,filename_out):
    x,y = read_data(filename_in)
    fig,axs = plt.subplots(1,1)
    fig.suptitle("linreg.txt, grid search")
    fig.set_size_inches(10,10)
    compute_grid_search(x,y,7,8,axs)
    plt.savefig(filename_out)



given_data_analyt("linreg.txt","given_data_analyt.png")
given_data_grid_search("linreg.txt","given_data_grid_search.png")

# simulate some graphs with different a
# b is the same, because there were no big difference between graphs with different b
# and it would create a lot of graphs
# samples - how many points to generate
for a in [-1,0,1]:
    for b in [1]:
        for sample in [20,50,100,200]:
            fig, axs = plt.subplots(2,2)
            fig.suptitle("a:{}, b:{}, samples:{}".format(a,b,sample))
            fig.set_size_inches(10,10)
            i = 0
            for error in [0,5,10,20]:
                ax = axs[i // 2][i % 2] # choose right subplot
                ax.set_title("error:{}".format(error))
                x,y = generate_data(a,b,sample,error)
                draw_solution(x,y,(a,b),ax)
                i += 1
            plt.legend(bbox_to_anchor=(1,0), loc="lower right", bbox_transform=fig.transFigure, ncol=2)
            plt.savefig("a-{}_b-{}_sample-{}_generated-data.png".format(a,b,sample))
