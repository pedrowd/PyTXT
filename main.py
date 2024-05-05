# This is the python open-source version of the upcoming puzzle game TXT.
from dataclasses import dataclass

class PhaseThroughError(Exception):
    pass


class NoSizeNoPushError(Exception):
    pass


class UnequalClassError(Exception):
    pass


class QuitInterrupt(Exception):
    pass


@dataclass
class Object:
    appearance: str = ""
    pushable: bool = False
    collision: bool = False
    size: str = "Medium"
    position_x: int = 0
    position_y: int = 0
    def Check(self):
        if self.collision == False and self.pushable == True:
            raise PhaseThroughError
        if self.size == "None" and self.pushable == True:
            raise NoSizeNoPushError


#ALWAYS set instance "Player"'s position attributes to its position in the list "level".
Player = Object(appearance="P", pushable=True, size="Medium", collision=True, position_x=1, position_y=3)
Empty = Object(appearance=".", pushable=False, collision=False, size="None")
Wall = Object(appearance="#", pushable=False, collision=True, size="None")
Win = Object(appearance="W", pushable=False, collision=False, size="None", position_x=7, position_y=1)
Trap = Object(appearance="*", pushable=False, collision=False, size="None")
Spring = Object(appearance="@", pushable=False, collision=False, size="None")
SpringPositionsX = [2, 5]
SpringPositionsY = [1, 3]
SpringPositions = [(2, 1), (5, 3)]
TrapPositions = [(2, 3), (4, 2), (7, 3)]
Is_Jumping = False
turn = 0
level = [[Wall, Wall, Wall, Wall, Wall, Wall, Wall, Wall, Wall], [Wall, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Wall], [Wall, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Wall], [Wall, Empty, Empty, Empty, Empty, Empty, Empty, Empty, Wall], [Wall, Wall, Wall, Wall, Wall, Wall, Wall, Wall, Wall]]
def LevelPrint():
    global turn
    turn += 1
    print(turn)
    level[Player.position_y][Player.position_x] = Player
    level[Win.position_y][Win.position_x] = Win
    for a in range(len(TrapPositions)):
        level[TrapPositions[a][1]][TrapPositions[a][0]] = Trap
    for a in range(len(SpringPositions)):
        level[SpringPositions[a][1]][SpringPositions[a][0]] = Spring
    for x in range(len(level)):
        NowLine = []
        for y in range(len(level[x])):
            NowLine.append(level[x][y].appearance)
        print("".join(NowLine))


def PlayerMove(direction):
    global Is_Jumping
    if not Is_Jumping:
        if direction == "R" or direction == "Right" or direction == "RIGHT" or direction == "r" or direction == "right":
            Player.position_x += 1
            level[Player.position_y][Player.position_x - 1] = Empty
        elif direction == "L" or direction == "Left" or direction == "LEFT" or direction == "l" or direction == "left":
            Player.position_x -= 1
            level[Player.position_y][Player.position_x + 1] = Empty
        elif direction == "D" or direction == "Down" or direction == "DOWN" or direction == "d" or direction == "down":
            Player.position_y += 1
            level[Player.position_y - 1][Player.position_x] = Empty
        elif direction == "U" or direction == "Up" or direction == "UP" or direction == "u" or direction == "up":
            Player.position_y -= 1
            level[Player.position_y + 1][Player.position_x] = Empty
    else:
        if direction == "R" or direction == "Right" or direction == "RIGHT" or direction == "r" or direction == "right":
            Player.position_x += 2
            level[Player.position_y][Player.position_x - 2] = Empty
        elif direction == "L" or direction == "Left" or direction == "LEFT" or direction == "l" or direction == "left":
            Player.position_x -= 2
            level[Player.position_y][Player.position_x + 2] = Empty
        elif direction == "D" or direction == "Down" or direction == "DOWN" or direction == "d" or direction == "down":
            Player.position_y += 2
            level[Player.position_y - 2][Player.position_x] = Empty
        elif direction == "U" or direction == "Up" or direction == "UP" or direction == "u" or direction == "up":
            Player.position_y -= 2
            level[Player.position_y + 2][Player.position_x] = Empty
    if not (Player.position_x, Player.position_y) in SpringPositions:
        Is_Jumping = False


def PlayGame():
    global Is_Jumping
    failed = False
    while (not Player.position_x == Win.position_x) or (not Player.position_y == Win.position_y):
        if not failed:
            LevelPrint()
            if (Player.position_x, Player.position_y) in SpringPositions:
                Is_Jumping = True
            moving_into = input("Move in direction ")
            if moving_into == "quit" or moving_into == "q" or moving_into == "Quit" or moving_into == "Q" or moving_into == "QUIT":
                raise QuitInterrupt
            PlayerMove(moving_into)
            if (Player.position_x, Player.position_y) in TrapPositions:
                failed = True
        else:
            print("You lose!")
            break
    if not failed:
        print("You win!")


PlayGame()