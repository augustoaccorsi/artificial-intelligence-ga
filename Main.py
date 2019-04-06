import re
from Point import Point

pointList = []

def buildPoints(line):
    line = line.split()
    point = Point(int(line[0]), int(line[1]), int(line[2]))
    pointList.append(point)

def readFile():
    with open("instancias/TSP/berlin52.tsp.txt", 'r') as f:
        for line in f:
            buildPoints(line)

readFile()
