def generateCO(moveTable):
    counter = 0
    pruningTable = [-1 for i in range(2187)]
    pruningTable[0] = 0
    depth = 0
    buffer = [0]    # Coordinates at current depth
    while counter < 2187 / 2:
        temp = []
        for coord in buffer:
            for newCoord in moveTable[coord]:
                if pruningTable[newCoord] == -1:
                    pruningTable[newCoord] = depth + 1
                    counter += 1
                temp.append(newCoord)
        buffer = temp
        depth += 1

    buffer = [i for i in range(len(pruningTable)) if pruningTable[i] == -1]
    while counter < 2186:
        for coord in buffer:
            for newCoord in moveTable[coord]:
                if pruningTable[newCoord] >= 0:
                    pruningTable[coord] = pruningTable[newCoord] + 1
                    counter += 1
                    buffer.remove(coord)
                    break

    return pruningTable