import re
from Node import Node

nodeList = []

def buildNode(line):
    line = line.split()
    node = Node(int(line[0]), int(line[1]), int(line[2]))
    nodeList.append(node)

def readFile():
    with open("instancias/TSP/berlin52.tsp.txt", 'r') as f:
        for line in f:
            buildNode(line)

readFile()