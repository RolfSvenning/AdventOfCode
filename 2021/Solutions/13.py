import numpy as np
import matplotlib.pyplot as plt


def part_one_and_two():
    coordinates = [line.strip().split(",") for line in open("2021/input/13.txt") if line[0] != "f" and line[0] != "\n"]
    coordinates = [[int(x),int(y)] for x,y in coordinates]
    paper = np.zeros((max([x for x,_ in coordinates]) + 1, max([y for _,y in coordinates]) + 1), dtype=int)
    for x,y in coordinates:
        paper[x,y] = 1
    folds = [line.strip().split(" ")[-1].split("=") for line in open("2021/input/13.txt") if line[0] == "f" and line[0] != "\n"]
    folds = [(a,int(b)) for a,b in folds]

    for i, (axis,c) in enumerate(folds):
        if axis == "x":
            paper = paper.T
        dotsToMove = [(x,y) for x,y in zip(np.where(paper == 1)[0], np.where(paper == 1)[1]) if y > c]
        for x, y in dotsToMove:
            _, d = np.shape(paper)
            paper[x, d - 1 - y] = 1
        paper = paper[:, :c]
        if axis == "x":
            paper = paper.T
        if i == 0:
            print("Part one, number of dots is: ", np.sum(paper))

    print("Part two, view image")
    plt.imshow(paper.T)
    plt.show()


if __name__ == '__main__':
    part_one_and_two()