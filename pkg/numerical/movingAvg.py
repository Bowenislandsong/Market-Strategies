import numpy as np


class MovingAvg:
    def __init__(self,array):
        self.arr = np.array(array)
        # print(self.arr)

    def WindowSize(self,windowSize):
        w = np.ones(windowSize)
        self.avg = np.convolve(self.arr,w)/windowSize
        # print(self.avg)
        return self

    def IsIncreasing(self) -> bool:
        return np.all(np.diff(self.avg) > 0)

    def NeverDropBy(self,price) -> bool:
        # print(np.diff(self.avg))
        return np.all(np.diff(self.avg) > -price)