import numpy as np

def generate(moveTable):
    length = len(moveTable)
    numMoves = len(moveTable[0])
    counter = 0
    pruningTable = np.empty(length)
    pruningTable.fill(-1)
    pruningTable[0] = 0
    depth = 0
    buffer = [0]    # Coordinates at current depth
    i = 1
    #while counter < length / 2 and counter < 9000:
    while counter < length / 4 and counter < 5000:
        temp = np.empty(numMoves ** i, dtype=np.uint16)
        j = 0
        for coord in buffer:
            for newCoord in moveTable[coord]:
                if pruningTable[newCoord] == -1:
                    pruningTable[newCoord] = depth + 1
                    counter += 1
                temp[j] = newCoord
                j += 1
        buffer = temp
        depth += 1
        i += 1
        print(counter, len(temp))

# This significantly speeds up pruning table creation
# but for some reason it makes all of the solutions longer
#    buffer = np.where(pruningTable < 0)[0]
#    while counter < length - 1:
#        for coord in buffer:
#            if pruningTable[coord] != -1:
#                continue
#            for newCoord in moveTable[coord]:
#                if pruningTable[newCoord] >= 0:
#                    pruningTable[coord] = pruningTable[newCoord] + 1
#                    counter += 1
#                    break

    buffer = np.where(pruningTable == -1)[0]
    done = np.zeros(buffer.size, dtype=np.bool_)
    while counter < length - 1:
        for i in range(len(buffer)):
            if done[i] == False:
                coord = buffer[i]
                for newCoord in moveTable[coord]:
                    if pruningTable[newCoord] >= 0:
                        pruningTable[coord] = pruningTable[newCoord] + 1
                        counter += 1
                        done[i] = True
                        break

    return pruningTable
