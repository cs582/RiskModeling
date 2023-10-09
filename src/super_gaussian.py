import numpy as np
import matplotlib.pyplot as plt

class SuperGaussianDistribution1D:
    def __init__(self, xlims, x_pow, coef):
        self.coef = coef
        self.x_pow = x_pow
        self.xlims = xlims
        self.x_mean = sum(xlims) / 2

    def plot_gaussian(self, ax=None):
        # Unpack values and create domain for the plot
        x0, xf = self.xlims
        x_range = xf - x0
        steps = 1000
        x = np.linspace(x0-5*x_range, xf+5*x_range, steps)

        # Figure plot
        if ax is None:
            plt.figure(figsize=(12, 7))
            plt.title(f"Super Gaussian\nrange={self.xlims}\nP={self.x_pow}")
            plt.plot(x, self.predict(x))
            plt.vlines([x0, xf], ymin=0, ymax=self.coef, colors='r')
            plt.show()
        else:
            ax.set_title(f"Super Gaussian\nrange={self.xlims}\nP={self.x_pow}")
            ax.plot(x, self.predict(x))
            ax.vlines([x0, xf], ymin=0, ymax=self.coef, colors='r')

    def predict(self, x):
        self.x_std = (max(self.xlims)-self.x_mean) / np.power(-2*np.log(0.95), 1/self.x_pow)
        return self.coef * np.exp( - np.power( np.power( (x - self.x_mean) / self.x_std, 2 ) / 2, self.x_pow ) )


class SuperGaussianDistribution3D:
    def __init__(self, xlims, ylims, zlims, shape):
        """
        This is a 3D Super Gaussian Distribution. Different from a Gaussian Distribution
        this function has a flattened top.

        Visually the graph looks like a two tailed CDF of a Normal distribution

        :param xlims:
        :param ylims:
        :param zlims:
        :param shape: Valid inputs 1 (for rectangular) or 2 (for elliptical).
        """
        self.xlims = xlims
        self.ylims = ylims
        self.zlims = zlims

        self.x_middle = sum(xlims) / 2
        self.y_middle = sum(ylims) / 2
        self.z_middle = sum(zlims) / 2

        self.xmin, self.xmax = xlims
        self.ymin, self.ymax = ylims
        self.zmin, self.zmax = zlims

        constant = -np.log(0.95)

        self.x_range = (self.xmax - self.xmin)
        self.x_pow = 2
        # self.x_std = (self.xmax - self.x_middle) / np.power(-np.log(0.5), 1/self.x_pow)
        self.x_std = (self.xmax-self.x_middle) / np.power(2 * np.sqrt(constant), 1/self.x_pow)

        self.y_range = (self.ymax - self.ymin)
        self.y_pow = 2
        # self.y_std = (self.ymax - self.y_middle) / np.power(-np.log(0.5), 1/self.y_pow)
        self.y_std = (self.ymax-self.y_middle) / np.power(2 * np.sqrt(constant), 1/self.y_pow)

        self.z_range = (self.zmax - self.zmin)
        self.z_pow = 2
        # self.z_std = (self.zmax - self.z_middle) / np.power(-np.log(0.5), 1/self.z_pow)
        self.z_std = (self.zmax-self.z_middle) / np.power(2 * np.sqrt(constant), 1/self.z_pow)

        self.shape = shape


    def plot_2d_slices(self, z_slices):

        x_domain = np.linspace(self.xmin-self.x_range, self.xmax+self.x_range, 100)
        y_domain = np.linspace(self.ymin-self.y_range, self.ymax+self.y_range, 100)

        X, Y = np.meshgrid(x_domain, y_domain)

        fig, ax = plt.subplots(len(z_slices), 1, figsize=(10, 10*len(z_slices)))

        for idx, z in enumerate(z_slices):
            risk = np.zeros_like(X)
            for i, x in enumerate(x_domain):
                for j, y in enumerate(y_domain):
                    risk[i, j] = self.predict(x, y, z)

            ax[idx].set_title(f"Risk at z = {z}")
            ax[idx].contourf(X, Y, risk, vmin=0.05, vmax=0.90)
            ax[idx].vlines([-1, 1], Y.min(), Y.max(), colors='r', linestyles='-')
            ax[idx].hlines([-2, 2], X.min(), X.max(), colors='r', linestyles='-')
            ax[idx].set_xlim(X.min(), X.max())
            ax[idx].set_ylim(Y.min(), Y.max())

        plt.savefig("tmp/figures/3DSuperGaussianSim.png")


    def predict(self, x, y, z):
        # Rectangular Gaussian Distribution
        if self.shape == 1:
            A = np.power( np.power( (x - self.x_middle)/self.x_std, 2 ) , self.x_pow)
            B = np.power( np.power( (y - self.y_middle)/self.y_std, 2 ) , self.y_pow)
            C = np.power( np.power( (z - self.z_middle)/self.z_std, 2 ) , self.z_pow)
            return np.exp(-A-B-C)

        # Elliptical Gaussian Distribution
        return x