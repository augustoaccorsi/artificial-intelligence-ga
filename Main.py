def readFile():
    with open("instancias/TSP/berlin52.tsp.txt", 'r') as f:
        for line in f:
            print(line)

readFile()