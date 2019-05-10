import matplotlib.pyplot as plt
from heapq import nsmallest
import numpy as np

def read_data(filename):
    x = []
    y = []

    with open(filename,'r') as f:
        for line in f:
            line = line.split(' ')
            x.append(float(line[0]))
            y.append(float(line[1]))
    return(x,y)

def distance(p1,p2):
    return ((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)**(1/2)

def plot_kmeans(points,centroids,k,foldername,counter):
    color = ["ro","go","bo","yo","co","mo"]
    for x,y,c in points:
            plt.plot(x,y,color[c])
    for x,y,c in centroids:
        plt.plot(x,y,"ko")
    plt.title("k={}, step={}".format(k,"init" if counter == 0 else counter))
    plt.savefig("{}/plot{}.png".format(foldername,counter))
    plt.clf() # clear figure

# x,y - lists of points coordinates
# k - number of clusters
# foldername - folder where the plots should be saved
def kmeans(x,y,k,foldername):
    points = [[x[i],y[i],0] for i in range(len(x))]
    centroids = [points[i][:2]+[i] for i in range(k)] # choose first k points as centroids
    counter = 0 # step of kmeans algorithm
    plot_kmeans(points,centroids,k,foldername,counter)
    counter += 1
    while True:
        changed = False
        for point in points:
            distances = [0] * k
            for centroid in centroids:
                distances[centroid[2]] = distance(point,centroid)
            index = distances.index(min(distances))
            if point[2] != index: # if cluster for given point changed, update it and must do another iteration of kmeans - changed = True
                point[2] = index
                changed = True
        centroids = [[] for _ in range(k)] # delete old centroids
        for i in range(k): # compute new centroids
            cluster_points = list(filter(lambda point: point[2] == i, points))
            c_x = sum([j for j,_,_ in cluster_points])/len(cluster_points)
            c_y = sum([j for _,j,_ in cluster_points])/len(cluster_points)
            centroids[i] = [c_x,c_y,i]
        plot_kmeans(points,centroids,k,foldername,counter)
        counter += 1
        if not changed:
            break

# sort points based on distance from point
def worsen_centroids(x,y,point):
    points = list(zip(x,y)) # make list of pairs
    points.sort(key = lambda p: (p[0] - point[0])**2 + (p[1] - point[1])**2) # distance as function for sort, no sqrt because it doesn't change solution
    return (list(p) for p in zip(*points)) # make tuple of lists back from list of points
    
def normalize_data(x,y):
    avg_x = sum(x)/len(x)
    avg_y = sum(y)/len(y)
    return [x/avg_x for x in x],[y/avg_y for y in y]

# points - where the clusters should be located (centroids from which to generate) (list of lists)
# error - number for normal distribution error
# samples - how meny points per cluster
def generate_data(points, error, samples):
    out = []
    for point in points:
        out.append(point)
        for _ in range(samples):
            out.append([point[0] + np.random.normal(0,error), point[1] + np.random.normal(0,error)]) # store point witch adjustment
    return (list(p) for p in zip(*out))


# default runs

#if you want to create pictures, uncomment for loop generating them
# and crete directories for pictures in advance

x,y = read_data("faithful.txt")
x,y = normalize_data(x,y)
# for i in range(1,6):
    # kmeans(x,y,i,"faithful-k-{}".format(i))

# worsen runs - when centroid are next to each other
x,y = read_data("faithful.txt")
# get left most vertex
index = x.index(min(x))
x,y = worsen_centroids(x,y,(x[index],y[index]))
x,y = normalize_data(x,y)
# for i in range(1,6):
#     kmeans(x,y,i,"faithful-worsen-k-{}".format(i))

# generate different number of clusters for different k values
# centroids in k means algorithm will be close to each other, so its worsen case
# generate 2 clusters

centroids = [
    [10,10],
    [50,50]
]
x,y = generate_data(centroids, 5, 30)
x,y = normalize_data(x,y)
# for i in range(1,6):
#     kmeans(x,y,i,"generated-2-k-{}".format(i))

#generate 3 clusters
centroids = [
    [10,10],
    [50,10],
    [25,50]
]
x,y = generate_data(centroids, 5, 30)
x,y = normalize_data(x,y)
# for i in range(1,6):
#     kmeans(x,y,i,"generated-3-k-{}".format(i))

# generate 4 clusters
centroids = [
    [10,10],
    [10,50],
    [50,50],
    [50,10]
]

x,y = generate_data(centroids, 5, 30)
x,y = normalize_data(x,y)
# for i in range(1,6):
#     kmeans(x,y,i,"generated-4-k-{}".format(i))

# generate 5 clusters

centroids = [
    [10,10],
    [10,50],
    [50,50],
    [50,10],
    [25,25]
]
x,y = generate_data(centroids, 5, 30)
x,y = normalize_data(x,y)
# for i in range(1,6):
#     kmeans(x,y,i,"generated-5-k-{}".format(i))

