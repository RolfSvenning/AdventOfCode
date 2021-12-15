import numpy as np

def part_one_and_two():
    lines = [[int(n) for n in line] for line in open("2021/input/15.txt").read().split("\n")]
    M = np.matrix(lines)
    n,d = np.shape(M)

    def getNeighbours(x,y):
        ns = [(a,b) for a,b in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] if 0 <= a < n and 0 <= b < d]
        print(ns)
                
    getNeighbours(0,0)
    getNeighbours(3,3)
    getNeighbours(9,5)
    getNeighbours(9,9)


    
           
if __name__ == '__main__':
    part_one_and_two()
