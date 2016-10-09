# -*- coding: utf-8 -*-
#
desc = 'Simple $\sin$ plot with some labels'
phash = '5f34e1ce21c3e5c1'


def plot():
    from matplotlib import pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np

    pos = np.zeros((3, 10))
    pos[0] = np.arange(10)
    fig = plt.figure()
    ax = plt.gca(projection='3d')
    ax.scatter(pos[0], pos[1], pos[2], c=np.arange(pos.shape[1]))

    return fig
