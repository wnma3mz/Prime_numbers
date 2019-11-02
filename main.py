# coding: utf-8
import os
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation;

import imageio

def arcLength2angle(r, l):
    # l = n * np.pi * r / 180
    n = l / r
    return n

def angle2xy(r, angle):
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return x, y

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(np.sqrt(n))+2):
            if n % i == 0:
                return False
        return True

def simData():
    r = 10000
    # list(filter(isPrime, range(2, r)))
    for n in range(2, r):
        if isPrime(n):
            # 将需要可视化的点x，y值传递给另一个函数
            yield n, n

if __name__ == '__main__':
    frames = []
    image_list = ['10', '100', '1000', '2000','3000', '4000', '5000','6000', '7000', '8000','9000','10000']
    for image_name in image_list:
        frames.append(imageio.imread(image_name + '.png'))
    # Save them as frames into a gif 
    imageio.mimsave('t.gif', frames, 'GIF', duration = 0.1)
    """
    # for r in 10 ** np.arange(1, 5):
    for r in range(2000, 10000)[::1000]:
    # r = 10000
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        ax.set_rgrids(np.arange(0, r*1.1, r*1.1))
        ax.set_rlabel_position(0.0)  # 标签显示在0°
        ax.set_rlim(0.0, r*1.1)  # 标签范围为[0, 5000)
        # ax.set_yticklabels(['0', '1000', '2000', '3000', '4000', '5000'])

        # point, = ax.scatter([], [], color='green', cmap='hsv', alpha=0.75)

        for i in range(2, r):
            if isPrime(i):
                ax.scatter(i, i, color='green', cmap='hsv', alpha=0.75)

        plt.savefig('{}.png'.format(r), dpi=1000)
        # plt.show()
    """
    