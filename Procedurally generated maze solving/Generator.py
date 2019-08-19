import random
#by Yusdel Lorenzo 2019
class Cell:
    wallComponents = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        self.x, self.y = x, y
        self.wall = {'N': True, 'S': True, 'E': True, 'W': True}

    def allWall(self):
        return all(self.wall.values())

    def deleteWall(self, other, wall):
        self.wall[wall] = False
        other.wall[Cell.wallComponents[wall]] = False
class Maze:
    def __init__(self, nx, ny, ix=0, iy=0):
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy
        self.Map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]

    def checkCell(self, x, y):
        return self.Map[x][y]

    def genSVG(self, file):
        ratio = self.nx / self.ny
        pad = 10
        height = 800
        width = 1008
        ry, rx = height / ny, width / nx

        def outWall(f, x1, y1, x2, y2):
            print('<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x1, y1, x2, y2), file=f)

        with open(file, 'w') as f:
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'.format(width+2*pad, height+2*pad,-pad, -pad, width+2*pad, height+2*pad),file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)
            for x in range(nx):
                for y in range(ny):
                    if maze.checkCell(x,y).wall['S']:
                        x1, y1, x2, y2 = x*rx, (y+1)*ry, (x+1)*rx, (y+1)*ry
                        outWall(f, x1, y1, x2, y2)
                    if maze.checkCell(x,y).wall['E']:
                        x1, y1, x2, y2 = (x+1)*rx, y*ry, (x+1)*rx, (y+1)*ry
                        outWall(f, x1, y1, x2, y2)
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height),file=f)
            print('</svg>', file=f)

    def checkNeighbours(self, cell):
        d = [('W', (-1,0)),('E', (1,0)),('S', (0,1)),('N', (0,-1))]
        neighbours = []
        for direction, (dx,dy) in d:
            x2, y2 = cell.x + dx, cell.y + dy
            if (0 <= x2 < nx) and (0 <= y2 < ny):
                neighbour = maze.checkCell(x2, y2)
                if neighbour.allWall():
                    neighbours.append((direction, neighbour))
        return neighbours

    def genMaze(self):
        n = self.nx * self.ny
        myStack = []
        currCell = self.checkCell(ix, iy)
        nv = 1
        while nv < n:
            neighbours = self.checkNeighbours(currCell)
            if not neighbours:
                currCell = myStack.pop()
                continue
            direction, next_cell = random.choice(neighbours)
            currCell.deleteWall(next_cell, direction)
            myStack.append(currCell)
            currCell = next_cell
            nv += 1

# Maze dimensions (ncols, nrows)
nx = int(input("Cols: "))
ny = int(input("Rows: "))
ix, iy = 0, 0

maze = Maze(nx, ny, ix, iy)
maze.genMaze()
maze.genSVG('maze.svg')
