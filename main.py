# coding: utf-8
import os
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.animation as animation

import imageio


def arcLength2angle(r, l):
    return l / r


def angle2xy(r, angle):
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    return x, y


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, int(np.sqrt(n)) + 2):
            if n % i == 0:
                return False
        return True


def png2gif(image_lst, fname='t.gif'):
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name + '.png'))
    # Save them as frames into a gif
    imageio.mimsave(fname, frames, 'GIF', duration=0.1)


if __name__ == '__main__':
    # 10, 100, 1000, 10000, 发现1000到10000太快，所以设定了1000到10000以k递增
    # for r in 10 ** np.arange(1, 5):
    for r in range(2000, 10000)[::1000]:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='polar')
        ax.set_rgrids(np.arange(0, r * 1.1, r * 1.1))
        ax.set_rlabel_position(0.0)  # 标签显示在0°
        ax.set_rlim(0.0, r * 1.1)  # 标签范围为[0, 5000)

        for i in range(2, r):
            if isPrime(i):
                ax.scatter(i, i, color='green', cmap='hsv', alpha=0.75)
        # 此处dpi可调低
        plt.savefig('imgs/{}.png'.format(r), dpi=1000)
        # plt.show()
