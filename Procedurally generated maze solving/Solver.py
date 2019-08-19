import sys
from PIL import Image
#by Yusdel Lorenzo 2019
def AStar(start, goal, neighborNodes, distance, cost):
    def makePath(parentNode, currNode):
        path = []
        while currNode is not None:
            path.append(currNode)
            currNode = parentNode[currNode]
        return list(reversed(path))

    gScore = {start: 0}
    fScore = {start: gScore[start] + cost(start, goal)}
    openSet = {start}
    closedSet = set()
    parentNode = {start: None}

    while openSet:
        current = min(openSet, key=lambda x: fScore[x])
        if current == goal:
            return makePath(parentNode, goal)
        openSet.remove(current)
        closedSet.add(current)
        for neighbor in neighborNodes(current):
            if neighbor in closedSet:
                continue
            if neighbor not in openSet:
                openSet.add(neighbor)
            newScore = gScore[current] + distance(current, neighbor)
            if newScore >= gScore.get(neighbor, float('inf')):
                continue
            parentNode[neighbor] = current
            gScore[neighbor] = newScore
            fScore[neighbor] = newScore + cost(neighbor, goal)
    return []

def blocked(p):
    x,y = p
    pixel = path_pixels[x,y]
    if any(c < 225 for c in pixel):
        return True

def getNeighbors(Pixel):
    x, y = Pixel
    neighbors = [(x-1, y), (x, y-1), (x+1, y), (x, y+1)]
    return [Pixel for Pixel in neighbors if not blocked(Pixel)]

def manhattan(pixel1, pixel2):
    return abs(pixel1[0]-pixel2[0]) + abs(pixel1[1]-pixel2[1])

def crowFlies(pixel1, pixel2):
    return (pixel1[0]-pixel2[0])**2 + (pixel1[1]-pixel2[1])**2

start = (400, 984) #middle at the top
goal = (398, 25) #middle at the bottom
path_img = Image.open(sys.argv[1])
path_pixels = path_img.load()
distance = manhattan
heuristic = manhattan
path = AStar(start, goal, getNeighbors, distance, heuristic)
for position in path:
    x,y = position
    path_pixels[x,y] = (255,0,0) # red
path_img.save(sys.argv[2])
