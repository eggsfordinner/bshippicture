import random
import numpy as np
from PIL import Image
from load_board import load_board

carrier = 5
battle = 4
sub = 3
cruise = 3
small = 2

# 0 - Nothing
# 1 - Ship
# 2 - Miss
# 3 - Hit
nothing = 0
ship = 1
miss = 2
hit = 3
destroyed = 4

alpha = {'A': 0, 'B': 1,'C': 2, 'D': 3,'E': 4, 'F': 5,'G': 6, 'H': 7,'I': 8, 'J': 9}
numeric = {0: 'A', 1: 'B', 2: 'C', 3:'D', 4:'E', 5:'F', 6:'G', 7: 'H', 8: 'I', 9:'J'}

possible_range = list(range(0,20))

def clearBoard():
    board = np.zeros((10, 10))
    return board

def checkPoints(new_points, used_points):
    for p in new_points:
        if p in used_points:
            return False
    return True

def placeCarrier(board, picture):
    used_points = []

    # Place Carrier / Size 5
    start = random.randrange(0, 20)
    if start >= 10:
        col = start - 10
        row = random.randrange(0, 5)
        board[row:row+5, col] = ship;

        for r in range(row,row+5):
            used_points.append((r, col))
            picture = updatePicture(picture, numeric[r] + str(col + 1), ship)

    elif start < 10:
        row = start
        col = random.randrange(0, 5)
        board[row, col:col+5] = ship;

        for c in range(col,col+5):
            used_points.append((row, c))
            picture = updatePicture(picture, numeric[row] + str(c + 1), ship)

    return board, used_points, picture

def placeBattleShip(board, used_points, picture):
    # Place Battleship / Size 4
    successful = False

    while(not successful):

        start = random.randrange(0, 20)

        if start >= 10:
            col = start - 10
            row = random.randrange(0, 6)

            new_points = []
            for i in range(row, row+4):
                print(i)
                new_points.append((i,col))

            if checkPoints(new_points, used_points):

                successful = True
                board[row:row+4, col] = ship;
                for r in range(row,row+4):
                    used_points.append((r, col))
                    picture = updatePicture(picture, numeric[r] + str(col + 1), ship)
        elif start < 10:
            row = start
            col = random.randrange(0, 6)

            new_points = []
            for i in range(col, col+4):
                new_points.append((row,i))

            if checkPoints(new_points, used_points):

                successful = True
                board[row, col:col+4] = ship;
                for c in range(col,col+4):
                    used_points.append((row, c))
                    picture = updatePicture(picture, numeric[row] + str(c + 1), ship)

    return board, used_points, picture

def placeCruise(board, used_points, picture):
    # Place Cruise / Size 3
    successful = False

    while(not successful):

        start = random.randrange(0, 20)

        if start >= 10:
            col = start - 10
            row = random.randrange(0, 7)

            new_points = []
            for i in range(row, row+3):
                new_points.append((i,col))

            if checkPoints(new_points, used_points):

                successful = True
                board[row:row+3, col] = ship;
                for r in range(row,row+3):
                    used_points.append((r, col))
                    picture = updatePicture(picture, numeric[r] + str(col + 1), ship)

        elif start < 10:
            row = start
            col = random.randrange(0, 7)

            new_points = []
            for i in range(col, col+3):
                new_points.append((row,i))

            if checkPoints(new_points, used_points):

                successful = True
                board[row, col:col+3] = ship;
                for c in range(col,col+3):
                    used_points.append((row, c))
                    picture = updatePicture(picture, numeric[row] + str(c + 1), ship)
    return board, used_points, picture

def placeSub(board, used_points, picture):
    # Place Cruise / Size 3
    successful = False

    while(not successful):

        start = random.randrange(0, 20)

        if start >= 10:
            col = start - 10
            row = random.randrange(0, 7)

            new_points = []
            for i in range(row, row+3):
                new_points.append((i,col))

            if checkPoints(new_points, used_points):

                successful = True
                board[row:row+3, col] = ship;
                for r in range(row,row+3):
                    used_points.append((r, col))
                    picture = updatePicture(picture, numeric[r] + str(col + 1), ship)

        elif start < 10:
            row = start
            col = random.randrange(0, 7)

            new_points = []
            for i in range(col, col+3):
                new_points.append((row,i))

            if checkPoints(new_points, used_points):

                successful = True
                board[row, col:col+3] = ship;
                for c in range(col,col+3):
                    used_points.append((row, c))
                    picture = updatePicture(picture, numeric[row] + str(c + 1), ship)

    return board, used_points, picture

def placeSmall(board, used_points, picture):
    # Place Cruise / Size 2
    successful = False

    while(not successful):

        start = random.randrange(0, 20)

        if start >= 10:
            col = start - 10
            row = random.randrange(0, 8)

            new_points = []
            for i in range(row, row+2):
                new_points.append((i,col))

            if checkPoints(new_points, used_points):
                successful = True
                board[row:row+2, col] = ship;
                for r in range(row,row+2):
                    used_points.append((r, col))
                    picture = updatePicture(picture, numeric[r] + str(col + 1), ship)

        elif start < 10:
            row = start
            col = random.randrange(0, 8)

            new_points = []
            for i in range(col, col+2):
                new_points.append((row,i))

            if checkPoints(new_points, used_points):
                successful = True
                board[row, col:col+2] = ship;
                for c in range(col,col+2):
                    used_points.append((row, c))
                    picture = updatePicture(picture, numeric[row] + str(c + 1), ship)
    return board, used_points, picture

def placeShips(board, picture, ship_locations):

    board, used_points, picture = placeCarrier(board, picture)
    board, used_points, picture = placeBattleShip(board, used_points, picture)
    board, used_points, picture = placeCruise(board, used_points, picture)
    board, used_points, picture = placeSub(board, used_points, picture)
    board, used_points, picture = placeSmall(board, used_points, picture)

    ship_locations["Carrier"] = used_points[0:5]
    ship_locations["Battleship"] = used_points[5:9]
    ship_locations["Cruiser"] = used_points[9:12]
    ship_locations["Submarine"] = used_points[12:15]
    ship_locations["Destroyer"] = used_points[15:17]

    return board, picture, ship_locations

def placeShot(board, position, prev_moves):
    type = 0
    if position not in prev_moves:

        row = alpha[position[0]]
        if len(position) > 2: col = int(position[1])*10 + int(position[2]) - 1
        else: col = int(position[1]) - 1

        if board[row, col] == ship:
            print("hit")
            board[row, col] = hit
            type = hit
        elif board[row,col] == nothing:
            print("miss")
            board[row, col] = miss
            type = miss
        prev_moves.append(position)
    else:
        print("Already made that move")

    return board, prev_moves, type

def isShipDestroyed(board, ships, picture1, picture2):
    hit_points = []
    for r in range(10):
        for c in range(10):
            if board[r, c] == hit:
                hit_points.append((r, c))

    if len(hit_points) > 0:
        for ship in ships.keys():

            print(hit_points, ships[ship])
            #if ships[ship] in hit_points:
            if all(item in hit_points for item in ships[ship]):
                print("You sunk their", ship)

                for point in ships[ship]:
                    board[point[0], point[1]] = destroyed
                    picture1 = updatePicture(picture1, numeric[point[0]] + str(point[1] + 1), destroyed)
                    picture2 = updatePicture(picture2, numeric[point[0]] + str(point[1] + 1), destroyed)

    return board, picture1, picture2

def updatePicture(picture, position, type):

    row_c = (alpha[position[0]]) * 30 + 25
    if len(position) > 2: col_c = (int(position[1])*10 + int(position[2]) - 1) * 30 + 50
    else: col_c = (int(position[1]) - 1) * 30 + 50

    if type == hit:
        picture[row_c-10:row_c+10, col_c-10:col_c+10] = [255, 0, 0]

    elif type == miss:
        picture[row_c-10:row_c+10, col_c-10:col_c+10] = [0, 0, 0]

    elif type == ship:
        picture[row_c-10:row_c+10, col_c-10:col_c+10] = [0, 255, 0]

    elif type == destroyed:
        picture[row_c-10:row_c+10, col_c-10:col_c+10] = [0, 0, 255]

    return picture

def Battleship():

    picture_p1_ships = load_board()
    picture_p1_target = load_board()

    picture_p2_ships = load_board()
    picture_p2_target = load_board()

    ship_locations1 = {}
    ship_locations2 = {}

    board1, picture_p1_ships, ship_locations1 = placeShips(clearBoard(), picture_p1_ships, ship_locations1)
    board2, picture_p2_ships, ship_locations2 = placeShips(clearBoard(), picture_p2_ships, ship_locations2)

    prev_moves1 = []
    prev_moves2 = []

    print(board1)
    print(board2)

    Image.fromarray(picture_p1_target.astype('uint8'), 'RGB').save("target1.png")
    Image.fromarray(picture_p2_ships.astype('uint8'), 'RGB').save("ships2.png")
    Image.fromarray(picture_p2_target.astype('uint8'), 'RGB').save("target2.png")
    Image.fromarray(picture_p1_ships.astype('uint8'), 'RGB').save("ships1.png")

    while(1):
        inp1 = input('P1')
        board2, prev_moves1, type = placeShot(board2, inp1, prev_moves1)
        picture_p1_target = updatePicture(picture_p1_target, inp1, type)
        picture_p2_ships = updatePicture(picture_p2_ships, inp1, type)

        board2, picture_p1_target, picture_p2_ships = isShipDestroyed(board2, ship_locations2, picture_p1_target, picture_p2_ships)

        print(inp1 + " -> " + str(type))
        Image.fromarray(picture_p1_target.astype('uint8'), 'RGB').save("target1.png")
        Image.fromarray(picture_p2_ships.astype('uint8'), 'RGB').save("ships2.png")

        inp2 = input('P2')
        board1, prev_moves2, type = placeShot(board1, inp2, prev_moves2)
        picture_p2_target = updatePicture(picture_p2_target, inp2, type)
        picture_p1_ships = updatePicture(picture_p1_ships, inp2, type)
        print(inp2 + " -> " + str(type))

        board1, picture_p2_target, picture_p1_ships = isShipDestroyed(board1, ship_locations1, picture_p2_target, picture_p1_ships)

        Image.fromarray(picture_p2_target.astype('uint8'), 'RGB').save("target2.png")
        Image.fromarray(picture_p1_ships.astype('uint8'), 'RGB').save("ships1.png")

    # placeShot(board1, "B1", prev_moves1)
    # placeShot(board1, "A2", prev_moves1)
    # placeShot(board1, "A3", prev_moves1)
    # placeShot(board1, "A4", prev_moves1)

Battleship()
