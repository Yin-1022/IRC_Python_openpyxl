import random
import copy

WIDTH = 20
HEIGHT = 20
wholeMap = []

coordinates = [(1,3), (2,1), (3,1), (3,2), (3,3)]

for x in range(WIDTH):
    col = []

    for y in range(HEIGHT):
        #if random.randint(0, 1) == 0:
        #    col.append("O")
        #else:
        #    col.append(" ")
        if (x,y) in coordinates:
            col.append("O")
        else:
            col.append(" ")
    wholeMap.append(col)

for y in range(HEIGHT):
    for x in range(WIDTH):
        print(wholeMap[y][x], end=' ')
    print()


i=20

while(True):
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x-1) % WIDTH
            right = (x+1) % WIDTH
            above = (y+1) % HEIGHT
            below = (y-1) % HEIGHT

            numNeightbor = 0

            if wholeMap[left][above] == 'O':
                numNeightbor += 1
            if wholeMap[x][above] == 'O':
                numNeightbor += 1
            if wholeMap[right][above] == 'O':
                numNeightbor += 1
            if wholeMap[left][y] == 'O':
                numNeightbor += 1
            if wholeMap[x][y] == 'O':
                numNeightbor += 1
            if wholeMap[right][y] == 'O':
                numNeightbor += 1
            if wholeMap[left][below] == 'O':
                numNeightbor += 1
            if wholeMap[x][below] == 'O':
                numNeightbor += 1
            if wholeMap[right][below] == 'O':
                numNeightbor += 1

            while(i>0):
                if(wholeMap[x][y]=='O' and  (numNeightbor < 2)):
                    wholeMap[x][y]==' '
                elif(wholeMap[x][y]=='O' and  (numNeightbor == 2 or numNeightbor == 3)):
                    wholeMap[x][y]=='O'
                elif(wholeMap[x][y]=='O' and  (numNeightbor > 3)):
                    wholeMap[x][y]==' '
                elif(wholeMap[x][y]==' ' and  (numNeightbor > 3)):
                    wholeMap[x][y]=='O'
                i=i-1


