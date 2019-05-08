import matplotlib.pyplot as plt
from heapq import nsmallest

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
        
        



x,y = read_data("faithful.txt")
# normalize data
avg_x = sum(x)/len(x)
avg_y = sum(y)/len(y)
x = [x/avg_x for x in x]
y = [y/avg_y for y in y]
# for i in range(1,6):
    # kmeans(x,y,i,"faithful-k-{}".format(i))

# TODO create bad first centroids
# put points with smallest x's to the front of the list