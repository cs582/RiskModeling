import matplotlib.pyplot as plt
from src.super_gaussian import SuperGaussianDistribution3D

if __name__=="__main__":

    xlim = (-1, 1)
    ylim = (-2, 2)
    zlim = (-3, 3)

    model = SuperGaussianDistribution3D(xlims=xlim, ylims=ylim, zlims=zlim, shape=1)

    model.plot_2d_slices([-3.5, -3.1, -3, -2.9, -2, 0, 2, 2.9, 3, 3.1, 3.5])