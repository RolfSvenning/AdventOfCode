import re
from numpy import array, column_stack, intp, sign, shape, where
import numpy as np
from numpy.core.numeric import zeros_like
from math import factorial


def part_one_and_two():
    enhancement, input = open("2021/input/20.txt").read().replace(".","0").replace("#","1").split("\n\n")
    enhancement = [int(s) for s in enhancement]
    input = np.array([[int(s) for s in r] for r in input.split("\n")], dtype=int)

    for r in range(50):
        n,d = np.shape(input)
        if r == 0 or enhancement[0] == 0:
            sides = np.zeros((n,2),dtype=int)
            top = np.zeros((2,d + 4),dtype=int)
        else:
            sides = np.zeros((n,1),dtype=int) + input[0,0]
            top = np.zeros((1,d + 2),dtype=int) + input[0,0]
        input_ = np.concatenate((top, np.concatenate((sides,input,sides),axis=1), top))
        n,d = np.shape(input_)
        output = np.zeros_like(input_)
        for i,j in [(i_,j_) for i_ in range(0,n) for j_ in range(0,d)]:
            if 0 < i < n - 1 and 0 < j < d-1: # not at boarder 
                bits = "".join([str(s) for s in input_[i-1:i+2,j-1:j+2].flatten().tolist()])
                output[i,j] = enhancement[int(bits,2)]
            elif enhancement[0] == 1:
                output[i,j] = input_[i,j] ^ 1
        input = output.copy()
        if r == 1: print("Part one, number of lit pixels after 2 rounds: ", np.sum(input))
    print("Part two, number of lit pixels after 50 rounds: ", np.sum(input))


if __name__ == '__main__':
    part_one_and_two()