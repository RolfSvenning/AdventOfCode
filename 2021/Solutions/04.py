import numpy as np


def part_one_and_two():
    input = [line.rstrip("\n") for line in open("2021/input/04.txt") if line != "\n"]
    numbers = [int(n) for n in input[0].split(",")]
    rows = [[int(number) for number in l.split()] for l in input[1:]]
    boards = [bingoBoard([a,b,c,d,e]) for a,b,c,d,e in zip(rows[0::5], rows[1::5], rows[2::5], rows[3::5], rows[4::5])]    

    firstBoardFound = False
    firstBoardRes = 0
    lastBoardRes = 0
    for n in numbers:
        for b in boards:
            if b.hasBingo is True:
                continue

            b.insertNumber(n)            
            if b.hasBingo is True:
                if not firstBoardFound:
                    firstBoardRes = b.boardSum() * n
                    firstBoardFound = True
                lastBoardRes = b.boardSum() * n

    return firstBoardRes, lastBoardRes

class bingoBoard:
    def __init__(self, rows):
        self.board = np.array(rows)
        self.hasBingo = False

    def __repr__(self):
        return str(self.board)
    
    def insertNumber(self, n):
        if n in self.board:
            self.board[np.where(self.board == n)] = -1
        if -5 in self.board.sum(axis=0) or -5 in self.board.sum(axis=1):
            self.board[self.board == -1] = 0
            self.hasBingo = True

    def boardSum(self):
        return np.sum(self.board)


if __name__ == "__main__":
    firstBoardRes, lastBoardRes = part_one_and_two()
    print("Sum of FIRST winning bingo board times 'n' is: ", firstBoardRes)
    print("Sum of LAST winning bingo board times 'n' is: ", lastBoardRes)
