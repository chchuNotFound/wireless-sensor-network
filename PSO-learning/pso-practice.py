import numpy as np
import matplotlib.pyplot as plt
import random
import math
from math import sqrt

# 适应度函数计算
# f(x,y) = sin(sqrt(x^2 + y^2)) / sqrt(x^2 + y^2) +
# e^((cos(2πx) + cos(2πy))/2) -
# 2.71289
def fun(x, y):
    res = math.sin(sqrt(x ** 2 + y ** 2)) / sqrt(x ** 2 + y ** 2)\
        + math.e ** (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y)) / 2\
        - 2.71289
    return res


if __name__ == '__main__':
    ## 参数初始化
    # 速度更新参数
    c1 = 1.49445
    c2 = 1.49445

    # 进化次数
    maxgen = 300
    # 种群规模
    sizepop = 20
    # 个体和速度的最大最小值
    popmax = 2
    popmin = -2
    Vmax = 0.5
    Vmin = -0.5

    # 适应度
    fitness = []
    pops = []
    Vs = []

    ## 随机产生初始粒子和速度
    for i in range(sizepop):
        # 初始种群，位置和速度
        currentPop = np.random.uniform(-2, 2,  (1, 2))
        pops.append(currentPop)

        currentV = np.random.uniform(-0.5, 0.5,  (1, 2))
        Vs.append(currentV)
        # 粒子适应度计算
        res = fun(currentPop[0][0], currentPop[0][1])
        fitness.append(res)
    fitness = np.array(fitness)
    bestfitness, bestindex = np.max(fitness), np.argmax(fitness)
    # 最优值对应个体(x,y)
    zbest = pops[bestindex]
    gbest = pops
    # 最优值f(x,y)
    fitnesszbest = bestfitness
    fitnessbest = fitness
    # print("zbest: %s" %(zbest))
    # print("gbest: %s" %(gbest))
    # print("fitnesszbest: %s" %(fitnesszbest))
    # print("fitnessbest: %s" %(fitnessbest))




