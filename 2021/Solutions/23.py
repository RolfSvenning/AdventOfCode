from functools import cache
import re

stringToDigit = {"A":"0", "B":"1", "C":"2", "D":"3", "#":"#", "\n":"\n", ".":".", " ":" "}
digitToString = {"0":"A", "1":"B", "2":"C", "3":"D", "#":"#", "\n":"\n", ".":".", " ":" "}

def part_one():
    print("Part one, solution by hand: ", 11608)

def part_two(verbose=False):
    inputAsDigits = "".join(stringToDigit[s] for s in open("2021/input/23.txt").read()).split("\n")
    coords = [[int(s) for s in re.findall("\d", l)] for l in inputAsDigits if len(re.findall("\d", l)) > 0]
    
    rooms = [[],[],[],[]]
    for cs in coords:
        for i,c in enumerate(cs):
            rooms[i].append(c)
    roomLength = len(rooms[0])
    roomsPartOne = tuple([tuple([room[0],room[-1]]) for room in rooms])
    rooms = tuple([tuple(room) for room in rooms])
    corridor = tuple([-1]*11)

    # SOLVING PART TWO HERE -----------------------------------------------
    states = bruteForce(rooms, corridor, roomLength)

    if verbose:
        for state in states:
            prettyPrinting(state, roomLength)
    
    print("Part one, minimum cost is: ", bruteForce(roomsPartOne, corridor, len(roomsPartOne[0]))[0][0])
    print("Part two, minimum cost is: ", states[0][0])

def canMoveFromRoomTo(start, end, corridor):
    canMove = True
    for i in range(min(start,end), max(start,end)+1):
        if corridor[i] != -1:
            canMove = False
            break
    return canMove

def canMoveCorridorToRoom(start, end, corridor):
    canMove = True
    assert start != end
    if start < end:
        for i in range(start + 1, end + 1):
            if corridor[i] != -1:
                canMove = False
                break
        return canMove
    else: # start > end
        for i in range(end, start):
            if corridor[i] != -1:
                canMove = False
                break
        return canMove

def isRoomDone(room,id, roomLength):
    return len(room) == roomLength and all([r == id for r in list(room)])

def isRoomReady(movingItem, room, roomID):
    if movingItem != roomID:
        return False
    if any([movingItem != r for r in room]):
        return False
    return True

def roomBaked(room,id):
    return all([r == id for r in list(room)])

def indexRoom(i):
    match i:
        case 0: return 2
        case 1: return 4
        case 2: return 6
        case 3: return 8
        case _: raise NotImplemented

def calcCost(numberOfMoves, element):
    match element:
        case 0: return 1 * numberOfMoves
        case 1: return 10 * numberOfMoves
        case 2: return 100 * numberOfMoves
        case 3: return 1000 * numberOfMoves
        case _: raise NotImplemented

def validCorridorIndices():
    return [0,1,3,5,7,9,10]

def prettyPrinting(state, roomLength):
    cost, rooms, corridor = state
    l1 = "#############"
    l2 = "#" + "".join([str(s) if s != -1 else "." for s in corridor]) + "#"

    roomsString = [["."] * (roomLength - len(rooms[i])) + [str(s) for s in rooms[i]] for i in range(4)]
    l3456 = ["#".join([roomsString[i][j] for i in range(4)]) for j in range(roomLength)]
    l3 = "###" + l3456[0] + "###"
    l456 = ["  #" + l + "#  " for l in l3456[1:]]
    l7 = "  #########"
    ss = "\n".join([l1, l2, l3] + l456 + [l7, ""])
    s = "".join([digitToString[s] for s in ss] + ["Budget is now: " + str(cost) + "\n"])
    print(s)

@cache
def bruteForce(rooms, corridor, roomLength):
    # FINISHED ----------------------------------------------------------------
    roomsDone = [isRoomDone(room, i, roomLength) for i,room in enumerate(rooms)]
    if all(roomsDone):
        return [(0, rooms, corridor)]
    newRooms = []

    # MOVE FROM ROOM TO ROOM --------------------------------------------------
    for i,roomI in enumerate(rooms):
        if len(roomI) == 0: # nothing to move
            continue

        if roomBaked(roomI, i):
            continue

        for j,roomJ in enumerate(rooms):
            if i == j: # not move to itself
                continue
            if not isRoomReady(roomI[0],roomJ,j): # wrong room or contains other items still
                continue

            if not canMoveFromRoomTo(indexRoom(i),indexRoom(j),corridor):
                continue
            else:
                movesCorridor = abs(indexRoom(j)-indexRoom(i)) + 1 
                movesRoomI = roomLength - len(roomI) # _,1
                movesRoomJ = roomLength - len(roomJ) # _,1
                totalMoves = movesCorridor + movesRoomI + movesRoomJ
                cost = calcCost(totalMoves, roomI[0])
                newRooms = list(rooms)
                newRooms[i] = roomI[1:]
                newRooms[j] = tuple([roomI[0]] + list(roomJ))
                newRooms = tuple(newRooms)
                statesRecursive = bruteForce(newRooms, corridor, roomLength)
                return [(cost + statesRecursive[0][0], rooms, corridor)] + statesRecursive

    # MOVE FROM CORRIDOR TO ROOM ----------------------------------------------
    for i in validCorridorIndices():
        if corridor[i] == -1:
            continue
        itemI = corridor[i]
        roomI = rooms[itemI]
        if isRoomReady(itemI, roomI, itemI) and canMoveCorridorToRoom(i,indexRoom(itemI),corridor):
            movesCorridor = abs(i - indexRoom(itemI))
            movesRoom = roomLength - len(roomI)
            totalMoves = movesCorridor + movesRoom
            cost = calcCost(totalMoves, itemI)
            newCorridor = list(corridor)
            newCorridor[i] = -1
            newCorridor = tuple(newCorridor)
            newRooms = list(rooms)
            newRooms[itemI] = tuple([itemI] + list(roomI))
            newRooms = tuple(newRooms)
            statesRecursive = bruteForce(newRooms, newCorridor, roomLength)
            return [(cost + statesRecursive[0][0], rooms, corridor)] + statesRecursive
    
    # MOVE FROM ROOM TO CORRIDOR ----------------------------------------------
    allStatesRecursive = []
    for roomID,roomI in enumerate(rooms):
        if len(roomI) == 0:
            continue
        itemI = roomI[0]
        if roomBaked(roomI,roomID):
            continue

        for j in validCorridorIndices():
            if corridor[j] != -1:
                continue
            if canMoveFromRoomTo(indexRoom(roomID), j, corridor):
                movesCorridor = abs(indexRoom(roomID) - j) + 1
                movesRoom = roomLength - len(roomI)
                totalMoves = movesCorridor + movesRoom
                cost = calcCost(totalMoves, itemI)
                newCorridor = list(corridor)
                newCorridor[j] = itemI
                newCorridor = tuple(newCorridor)
                newRooms = list(rooms)
                newRooms[roomID] = roomI[1:]
                newRooms=tuple(newRooms)
                statesRecursive = bruteForce(newRooms,newCorridor,roomLength)
                allStatesRecursive.append((cost + statesRecursive[0][0], statesRecursive))     
    if len(allStatesRecursive) == 0:
        return [(999999999, rooms, corridor)]
    bestIndex = allStatesRecursive.index(min(allStatesRecursive, key=lambda x: x[0]))
    return [(allStatesRecursive[bestIndex][0], rooms, corridor)] + allStatesRecursive[bestIndex][1]


if __name__ == '__main__':
    part_two(verbose=True)