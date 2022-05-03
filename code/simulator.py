# -*- encoding:utf-8 -*-

from argparse import ArgumentError
import numpy as np
import time

class Simulator:
    def __init__(self, split = 3) -> None:
        if (split <= 1):
            raise ArgumentError("Your split or number must be a positive integer and > 1 !")

        self.split = split

    # 切点生成器，参数是前面的split，一共split-1个切点，split是段数
    # splitPoint的第一个点是0.，最后一个点是1.，一共split+1个点（方便计算长度）
    # 默认的范围是[0, 1]，想要放大n倍把最后的结果乘以n就行了，最大值也要乘以n
    def __generator(self) -> np.array:
        splitPoint = np.empty(shape = (1, self.split + 1), dtype = float)[0]
        result = np.empty(shape = (1, self.split), dtype = float)[0]
        splitPoint[0] = 0
        splitPoint[self.split] = 1
        for i in range(self.split - 1):
            splitPoint[i+1] = np.random.rand(1,1)[0][0]
        splitPoint.sort()

        #print(splitPoint)
        return splitPoint

    # 获得每一段的长度，一共split段，从小到大排序，想要得到最小值直接找第一个[0]就可以
    def getMin(self) -> np.array:
        temp = np.empty(shape = (1, self.split), dtype = float)[0]
        points = self.__generator()

        for i in range(self.split):
            temp[i] = points[i+1] - points[i]

        temp.sort()
        # print(temp)
        return temp

    # 测试接口 返回(测试次数，最短一段的长度)
    def test(self, times) -> tuple:
        sum = 0
        for i in range(times):
            sum += self.getMin()[0]

        sum /= times
        print(sum)
        return (times, sum)  


# Sample
# 这个测试用例勉强能跑，到1e7就太慢了
def test():
    testCase = Simulator(split = 3)
    testCase.test(1000000)

if __name__ == '__main__':
    test()