# 201201749 Tracey Houghton

# Defines the lists and main variables to be used
dataPoints = [(0,0),(1,0),(1,1),(0,1),(-1,0)]
centroid1 = [1,0]
cluster1 = list()
centroid2 = [1,1]
cluster2 = list()
finished = False

# Receives two tuples a and b, calculates the Euclidian distance between them
# according to the given formula and returns the distance as variable
# calculatedDistance as a float.
def calculateDistance(a,b):
    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]
    calculatedDistance = (((x2-x1)*(x2-x1))+((y2-y1)*(y2-y1)))**0.5
    return calculatedDistance

# Receives a list of tuples that may be considered x,y coordinates. Calculates
# the mean of all x coordinates in the list, and the mean of all y coordinates.
# Creates a tuple meanPoints as an x,y coordinate based on the means calculated.
def calculateMeanDatapoints(pointsList):
    xTotal = 0
    yTotal = 0
    # adds the "x values" together, and the "y values" together
    for points in pointsList:
        xTotal = xTotal + points[0]
        yTotal = yTotal + points[1]
    # Calculates the mean of the x values in pointsList
    xMean = xTotal/len(pointsList)
    # Calculates the mean of the y values in pointsList
    yMean = yTotal/len(pointsList)
    # Creates a tuple called meanPoints that may be considered an x,y coordinate
    # from the mean x values and the mean y values of pointsList
    meanPoints = ((xTotal/len(pointsList)),(yTotal/len(pointsList)))
    return meanPoints

# Main Program
# iterates until the mean datapoints in each cluster are equal to the
# centriod of that cluster. For the given dataset, this is two iterations.
while finished == False:
    # iterate through every datapoint in the list
    for point in dataPoints:
        # calculate the distance from centroid1
        c1Distance = calculateDistance(centroid1,point)
        # calculate the distance from centroid2
        c2Distance = calculateDistance(centroid2,point)
        # if the distance is closest to centroid1 then put it in cluster1 list
        if c1Distance < c2Distance:
            cluster1.append(point)
        # if the distance is closest to centroid2 then put it in cluster2 list
        elif c2Distance < c1Distance:
            cluster2.append(point)
        # if it's equidistant, assign to either cluster1 or cluster2 randomly.
        else:
            randomCentroid=randint(1,2)
            if randomCentroid == 1:
                cluster1.append(point)
            else:
                cluster2.append(point)
    # calculate the mean datapoint in cluster1 using a function
    meanCluster1 = calculateMeanDatapoints(cluster1)
    # calculate the mean datapoint in cluster2 using a function
    meanCluster2 = calculateMeanDatapoints(cluster2)
    # before updating the new centroid values, assign the values to a variable
    # to compare with the new values
    oldCentroid1 = centroid1
    oldCentroid2 = centroid2
    # update the centroid values with the mean datapoints of each cluster.
    centroid1 = meanCluster1
    centroid2 = meanCluster2
    # checks if the clusters are stable by comparing the old centriod values
    # if the clusters are stable, the program terminates
    if oldCentroid1 == centroid1 and oldCentroid2 == centroid2:
        print("Cluster 1 = ",cluster1,"around centroid",centroid1)
        print("Cluster 2 = ",cluster2,"around centroid",centroid2)
        finished = True
    else:
    # if the clusters are not stable, the cluster lists are cleared and the
    # progam iterates again with the new centroid values.
       cluster1.clear()
       cluster2.clear()
